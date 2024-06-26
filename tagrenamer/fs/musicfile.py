# -*- coding: utf-8 -*-
"""
Represent a file of a known music file format found on the file system.
"""
import hashlib
import taglib
from tagrenamer.app.safestring import SafeString
from tagrenamer.fs.file import File


music_extensions = ('mp3', 'MP3', 'ogg', 'OGG', 'flac', 'FLAC')


class MusicFile(File):
    """
    Represent a file of a known music file format found on the file system.

    Callbacks:
    - sanitize (obj)
    """

    def __init__(self, output, settings, path, extension,
                 callbacks={}, parent=None, dl=1):
        """Initialize the music file object."""
        self.relpath_new = ''
        self.artist = ''
        self.album = ''
        self.title = ''
        self.hash = None
        self.artist_s = ''
        self.album_s = ''
        self.title_s = ''
        self.hash_s = ''
        File.__init__(
            self,
            output,
            settings,
            path=path,
            extension=extension,
            callbacks=callbacks,
            parent=parent,
            dl=dl)

        # Set the extension if available.
        self.extension = ''
        if '.' in self.base:
            self.extension = extension

        self.extract()

    def extract(self):
        """Extract all meta data using the Taglib library."""
        self.out.log(str(self), '%s.extract' % self.type, self.dl)
        f = taglib.File(self.path)
        # Determine the value of what becomes the {{artist}} field:
        self.artist = ' '.join(f.tags.get('ARTIST', ['unknown_artist']))
        albumartist = ' '.join(f.tags.get('ALBUMARTIST', ['']))
        if not self.settings.albumartist and albumartist:
            self.out.runtime_error(
                "The following file has a albumartist tag set:\n\n"
                "File:        '%s'\n"
                "Artist:      '%s'\n"
                "Albumartist: '%s'\n"
                "\nPlease remove 'albumartist' tags from your files.\n"
                "\nRun with --albumartist if you are renaming VA albums!"
                % (self.relpath, self.artist, albumartist))
        elif self.settings.albumartist and albumartist:
            self.artist = albumartist
            self.out.log("Artst: '%s' (via albumartist)" % self.artist,
                         '%s.extract' % self.type, self.dl + 1)
        else:
            self.out.log("Artst: '%s'" % self.artist,
                         '%s.extract' % self.type, self.dl + 1)
        # Extract the other fields:
        self.album = ' '.join(f.tags.get('ALBUM', ['unknown_album']))
        self.title = ' '.join(f.tags.get('TITLE', ['unknown_title']))
        self.track = ' '.join(f.tags.get('TRACKNUMBER', ['unknown_track']))
        self.out.log("Album: '%s'" % self.album,
                     '%s.extract' % self.type, self.dl + 1)
        self.out.log("Title: '%s'" % self.title,
                     '%s.extract' % self.type, self.dl + 1)
        self.out.log("Track: '%s'" % self.track,
                     '%s.extract' % self.type, self.dl + 1)

    def sanitize(self):
        """Sanitize the extracted data ready for file system level usage."""
        self.out.log(str(self), '%s.sanitize' % self.type, self.dl)
        self.artist_s = str(SafeString(self.artist.strip()))
        self.album_s = str(SafeString(self.album.strip()))
        self.title_s = str(SafeString(self.title.strip()))
        self.track_s = str(SafeString(self.track.strip())).replace('/', '-')

        # Start validating the data, based on field length.
        if not len(self.artist_s):
            raise ValueError(self)
        elif not len(self.album_s):
            raise ValueError(self)
        elif not len(self.title_s):
            raise ValueError(self)
        elif not len(self.track_s):
            raise ValueError(self)

        # Generate a hash from each string to build  a unique file identifier.
        self.hash = hashlib.md5()
        self.hash.update(self.artist_s.encode('utf-8'))
        self.hash.update(self.album_s.encode('utf-8'))
        self.hash.update(self.title_s.encode('utf-8'))
        self.hash.update(self.track_s.encode('utf-8'))
        self.hash.update(self.extension.encode('utf-8'))
        self.hash_s = str(self.hash.hexdigest())

        # Print the sanitized metadata fields:
        self.out.log("{artist}: '%s'" % self.artist_s,
                     '%s.sanitize' % self.type, self.dl + 1)
        self.out.log("{album}: '%s'" % self.album_s,
                     '%s.sanitize' % self.type, self.dl + 1)
        self.out.log("{title}: '%s'" % self.title_s,
                     '%s.sanitize' % self.type, self.dl + 1)
        self.out.log("{track}: '%s'" % self.track_s,
                     '%s.sanitize' % self.type, self.dl + 1)
        self.out.log("{hash}: '%s'" % self.hash_s,
                     '%s.sanitize' % self.type, self.dl + 1)
        self.out.log("{ext}: '%s'" % self.extension,
                     '%s.sanitize' % self.type, self.dl + 1)

        # Invoke the sanitize callback, see main class description.
        self.invoke('sanitize', self)
