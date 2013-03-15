Tagrenamer
==============

*Tagrenamer does one thing and attempts to do it well, it rewrites trees of music
files - e.g. your collection - based on metadata and puts apart anything else. This
allows music puritans to organize the filesystem structure without having to
depend on a specific music organizer as the directories and filenames will be
rewritten by tagrenamer without the need of a database.*

Features
--------------
Tagrenamer has been designed with a very specific set of functional needs and
has been rewritten in private space (TM) multiple times throughout the years,
these are its features:

- **Clean:** Pure python based, cross-platform oriented and a true command line application.
- **Scalable:** Renames a couple of files but tens of thousands of them just as easily.
- **Fail-safe:** Full atomic operation, doesn't touch a single file if something is wrong.
- **Supports** MP3, OGG and FLAC files.
- **None-music files** are regarded as *left-overs* and are put in a subdirectory, original directory structure is kept.
- **--dry-run** emulates its operation and can be used with *-vv* for verbose debugging.
- **--shell** doesn't touch your files but generates shell commands (*rm* and *mv*) that rename the files for you.

Installation
--------------
Currently there is no packaging, system-wide installation or installer to set it
up for you. Although all of these are planned for the future setting it up is
still fairly simple:

- Ensure you have Python 2.7 and *tagpy* installed, e.g.: apt-get install python-tagpy
- $ git clone https://github.com/nielsvm/tagrenamer.git
- cd tagrenamer/
- ./tagrenamer --help

Usage
--------------
    Usage: tagrenamer [OPTIONS]... [DIRECTORY]

    Options:
      -h, --help           show this help message and exit
      -d, --dry-run        Perform a dry run and don't touch anything.
      -f F, --format=F     The format in which filenames will be rewritten.
      -l L, --leftovers=L  The directory where non-music files will be moved to.
      -S S, --stagedir=S   Temporary directory before music hits its final spot.
      -s, --shell          Generate and print shell commands (implies -q and -d)
      -q, --quiet          Silence all output completely, including debugging.
      -v, --verbose        The level of logging verbosity, up to 5 v's.

### The --format parameter
This parameter defines exactly how the files should be renamed and how the
directories should be named and works with simple fields that you can put
in the order you like. The field values are lowercased by design, don't have
beginning or trailing spaces and omit any character that could be dangerous for
your file system.

#### Fields explained
- **{artist}** '*the rolling stones*'
- **{album}** '*classic hits*'
- **{title}** '*satisfaction*'
- **{hash} ** '*feda09b72be7cba338dd421ba8f92442*' (unique combination of all fields)
- **{ext}** '*mp3*'

#### Default behavior: {artist}/{album}/{artist}-{title}.{ext}
    rowwen heze/
    rowwen heze/saus
    rowwen heze/saus/rowwen heze-shannon song.mp3
    rowwen heze/saus/rowwen heze-que paso.mp3
    rowwen heze/saus/rowwen heze-auto vliegtuig.mp3
    rowwen heze/saus/rowwen heze-de neus omhoeg.mp3
    rowwen heze/saus/rowwen heze-samen met ow.mp3
    rowwen heze/saus/rowwen heze-t roeie klied.mp3
    rowwen heze/saus/rowwen heze-vur altied is vurbeej.mp3
    rowwen heze/saus/rowwen heze-50 joar.mp3
    rowwen heze/saus/rowwen heze-november.mp3
    rowwen heze/saus/rowwen heze-de moan.mp3
    rowwen heze/saus/rowwen heze-heilige anthonius.mp3
    rowwen heze/saus/rowwen heze-de peel in brand.mp3
    rowwen heze/saus/rowwen heze-dag geluk.mp3
    rowwen heze/saus/rowwen heze-bestel mar.mp3
    rowwen heze/saus/rowwen heze-limburg.mp3
    rowwen heze/saus/rowwen heze-kilomeaters.mp3
    rowwen heze/saus/rowwen heze-welcome in the saus.mp3

#### Hash based approach: {artist}/{artist}-{hash}.{ext}
    rowwen heze/
    rowwen heze/saus
    rowwen heze/saus/rowwen heze-2c3046935e4519306898f23865d81da8.mp3
    rowwen heze/saus/rowwen heze-610e31d118c815526dc516d55c5bb066.mp3
    rowwen heze/saus/rowwen heze-bd6f9b57842d421db145e06c1f04e93b.mp3
    ...

#### Flat structure: {artist}-{album}-{title}.{ext}
    rowwen heze-saus-shannon song.mp3
    rowwen heze-saus-november.mp3
    rowwen heze-saus-50 joar.mp3
    ...
