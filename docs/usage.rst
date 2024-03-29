=====
Usage
=====

.. code-block:: console

   Usage: tagrenamer [OPTIONS] [DIRECTORY]/

   Options:
     --version            show program's version number and exit
     -h, --help           show this help message and exit
     -d, --dry-run        Perform a dry run and don't touch anything.
     -f F, --format=F     The format in which filenames will be rewritten.
     -l L, --leftovers=L  The directory where non-music files will be moved to.
     -S S, --stagedir=S   Temporary directory before music hits its final spot.
     -a, --albumartist    Use 'albumartist' tag when set to support VA albums.
     -s, --shell          Generate and print shell commands (implies -q and -d)
     -q, --quiet          Silence non-debugging output completely.
     -v, --verbose        The level of logging verbosity.

``--version``
-------------
Report the application version:

.. code-block:: console

   $ tagrenamer --version
   tagrenamer 0.0.3

``--dry-run``
-------------
Test if the renames will succeed without touching files:

.. code-block:: console

   $ tagrenamer --dry-run Music/
   - Tagrenamer version 0.0.3.
   - Leftovers directory '__LEFTOVERS/' created.
   - Stage directory '__STAGE/' created.
   - Traverse the collection and extract music tags.
   - Validating tag input and sanitizing variables.
   - Moving non music files to '__LEFTOVERS/'.
   - Moving music to new tree in stage directory '__STAGE/'.
   - Remove empty directories (except stage/leftover directories).
   - Move everything from stage into the final location.
   - Deleting the temporary stage directory '__STAGE/'.
   - Deleting the empty leftovers directory '__LEFTOVERS/'.
   - DONE! Processed 11 files.

Combine with ``-vvvvv`` to see how the structure looks like.

``--leftovers``
---------------
Name the leftovers directory differently:

.. code-block:: console

   $ tagrenamer --leftovers='garbage' Music/
   - Tagrenamer version 0.0.3.
   - Leftovers directory 'garbage/' created.
   - Stage directory '__STAGE/' created.
   - Traverse the collection and extract music tags.
   - Validating tag input and sanitizing variables.
   - Moving non music files to 'garbage/'.
   - Moving music to new tree in stage directory '__STAGE/'.
   - Remove empty directories (except stage/leftover directories).
   - Move everything from stage into the final location.
   - Deleting the temporary stage directory '__STAGE/'.
   - Deleting the empty leftovers directory 'garbage/'.
   - DONE! Processed 36 files.

``--stagedir``
--------------
Name the temporary staging directory differently:

.. code-block:: console

   $ tagrenamer --stagedir='.tmp' Music/
   - Tagrenamer version 0.0.3.
   - Leftovers directory '__LEFTOVERS/' created.
   - Stage directory '.tmp/' created.
   - Traverse the collection and extract music tags.
   - Validating tag input and sanitizing variables.
   - Moving non music files to '__LEFTOVERS/'.
   - Moving music to new tree in stage directory '.tmp/'.
   - Remove empty directories (except stage/leftover directories).
   - Move everything from stage into the final location.
   - Deleting the temporary stage directory '.tmp/'.
   - Deleting the empty leftovers directory '__LEFTOVERS/'.
   - DONE! Processed 36 files.

``--albumartist``
-----------------
Most music albums consist of songs of one and the same artist and thus each
track is expected to have the same value set as ``artist`` tag. Tagrenamer
operates upon this assumption by default and renames your files into your
preferred music tree layout, depending on how you set the ``--format``
parameter.

In the case of Various Artists (VA) albums or collection CDs, this default
behavior becomes problematic as Tagrenamer would extract a different
``{{artist}}`` field value for each track. So by default, a VA album would be
split up into many small folders like this using the default layout:

.. code-block:: console

   Music
   ├── alphaville
   │   └── back to the disco hits of the 80s - cd 1
   │       └── alphaville-31574918225b5d002d46aee87fc7aa67.mp3
   ├── arabesque
   │   └── back to the disco hits of the 80s - cd 1
   │       └── arabesque-ece33749f59d5e3e1626b8d3156c21c5.mp3
   ├── art company
   │   └── back to the disco hits of the 80s - cd 2
   │       └── art company-cfe0e9d57b00b5feb4e9a295d13bd211.mp3
   ├── baccara
   │   └── back to the disco hits of the 80s - cd 2
   │       └── baccara-de1ed352751402fd03180c18ed7595be.mp3
   ├── bad boys blue
   │   └── back to the disco hits of the 80s - cd 1
   │       └── bad boys blue-7eea98175e2a57b388b14635bf437cc8.mp3

This behavior is the default because Tagrenamer wasn't originally built with
Various Artists (VA) albums in mind and actually **actively recommends** you
to remove the ``albumartist`` ID3-tag for normal same-artist music albums. Quite
often, music software just set the same value to the ``albumartist`` tag as the
``artist`` tag, but worse, in some cases these tags diverge from each other and
often would lead to confusing end-users as these albums could then show up as
multiple artists in various music players.

For actual VA-albums you need to first check that the ``albumartist`` tag is set
to one and the same value for all files in the album. If you then run Tagrenamer
with the ``--albumartist`` flag passed, it will then try to use the album artist
as ``{artist}`` field when its set on the file:

.. code-block:: console

   Music
   ├── alphaville
   │   └── back to the disco hits of the 80s - cd 1
   │       └── alphaville-31574918225b5d002d46aee87fc7aa67.mp3
   ├── arabesque
   │   └── back to the disco hits of the 80s - cd 1
   │       └── arabesque-ece33749f59d5e3e1626b8d3156c21c5.mp3
   ├── art company
   │   └── back to the disco hits of the 80s - cd 2
   │       └── art company-cfe0e9d57b00b5feb4e9a295d13bd211.mp3
   ├── baccara
   │   └── back to the disco hits of the 80s - cd 2
   │       └── baccara-de1ed352751402fd03180c18ed7595be.mp3
   ├── bad boys blue
   │   └── back to the disco hits of the 80s - cd 1
   │       └── bad boys blue-7eea98175e2a57b388b14635bf437cc8.mp3

In case of doubt, run with the ``--shell`` parameter first to test.

``--shell``
-----------
Generate a list of shell commands that you can manually review and paste into
your terminal. Enabling ``--shell`` also implies ``--quiet`` and ``--dry-run``
and will never touch your files:

.. code-block:: console

   $ tagrenamer --format='{artist}/{album} - {title}.{ext}' --shell Music/
   mkdir -v "Music/__LEFTOVERS"
   mkdir -v "Music/__STAGE"
   mkdir -v "Music/__STAGE/rammstein"
   mv -v "Music/spieluhr.mp3" "Music/__STAGE/rammstein/mutter - spieluhr.mp3"
   mv -v "Music/links 2 3 4.mp3" "Music/__STAGE/rammstein/mutter - links 2 3 4.mp3"
   mv -v "Music/ich will.mp3" "Music/__STAGE/rammstein/mutter - ich will.mp3"
   mv -v "Music/sonne.mp3" "Music/__STAGE/rammstein/mutter - sonne.mp3"
   mv -v "Music/rein raus.mp3" "Music/__STAGE/rammstein/mutter - rein raus.mp3"
   mv -v "Music/nebel.mp3" "Music/__STAGE/rammstein/mutter - nebel.mp3"
   mv -v "Music/adios.mp3" "Music/__STAGE/rammstein/mutter - adios.mp3"
   mv -v "Music/zwitter.mp3" "Music/__STAGE/rammstein/mutter - zwitter.mp3"
   mv -v "Music/mein herz brennt.mp3" "Music/__STAGE/rammstein/mutter - mein herz brennt.mp3"
   mv -v "Music/mutter.mp3" "Music/__STAGE/rammstein/mutter - mutter.mp3"
   mv -v "Music/feuer frei.mp3" "Music/__STAGE/rammstein/mutter - feuer frei.mp3"
   mv -v "Music/__STAGE/rammstein" "Music/rammstein"
   rm -Rv "Music/__STAGE"
   rm -Rv "Music/__LEFTOVERS"

``--quiet``
-----------
Suppress all normal output:

.. code-block:: console

   $ tagrenamer --quiet Music/

.. code-block:: console

   Music
   └── rammstein
       └── mutter
           ├── rammstein-1777b3a4c02565cec36c3e5f71f40102.mp3
           ├── rammstein-2ec6d3d6fc625fa6ea93ae283175f13c.mp3
           ├── rammstein-5bd7b80dbc746b409bc8a6093b65d1c3.mp3
           └── rammstein-f3bd509bc5c6d5dd2968695d12293f09.mp3

``-v`` (debugging)
------------------
Tagrenamer ships with a very detailed debugging facility and this verbosity is
controlled using the ``-v`` parameter. The number of ``v``'s you pass,
determines the verbosity level which follows the debt of the processed
collection tree:

.. code-block:: console

   $ tagrenamer --dry-run --quiet -vvvvv Music/
   00:07:58  <__main__>
   00:07:58  <Collection.__init__>
   00:07:58  <Collection.initializeDirectories>
   00:07:58  <Directory.exists>               __LEFTOVERS
   00:07:58  <Directory.mkdir>                __LEFTOVERS
   00:07:58  <Directory.exists>               __STAGE
   00:07:58  <Directory.mkdir>                __STAGE
   00:07:58  <Collection.traverse>
   00:07:58  <Directory.traverse>          Music
   00:07:58  <Directory.exists>            Music
   00:07:58  <MusicFile.extract>                    spieluhr.mp3
   00:07:58  <MusicFile.extract>                    'links 2 3 4.mp3'
   00:07:58  <MusicFile.extract>                    'ich will.mp3'
   00:07:58  <MusicFile.extract>                    sonne.mp3
   00:07:58  <MusicFile.extract>                    'rein raus.mp3'
   00:07:58  <MusicFile.extract>                    nebel.mp3
   00:07:58  <MusicFile.extract>                    adios.mp3
   00:07:58  <MusicFile.extract>                    zwitter.mp3
   00:07:58  <MusicFile.extract>                    'mein herz brennt.mp3'
   00:07:58  <MusicFile.extract>                    mutter.mp3
   00:07:58  <MusicFile.extract>                    'feuer frei.mp3'
   00:07:58  <Collection.sanitize>
   00:07:58  <MusicFile.sanitize>                    spieluhr.mp3
   00:07:58  <MusicFile.sanitize>                    'links 2 3 4.mp3'
   00:07:58  <MusicFile.sanitize>                    'ich will.mp3'
   00:07:58  <MusicFile.sanitize>                    sonne.mp3
   00:07:58  <MusicFile.sanitize>                    'rein raus.mp3'
   00:07:58  <MusicFile.sanitize>                    nebel.mp3
   00:07:58  <MusicFile.sanitize>                    adios.mp3
   00:07:58  <MusicFile.sanitize>                    zwitter.mp3
   00:07:58  <MusicFile.sanitize>                    'mein herz brennt.mp3'
   00:07:58  <MusicFile.sanitize>                    mutter.mp3
   00:07:58  <MusicFile.sanitize>                    'feuer frei.mp3'
   00:07:58  <Collection.moveLeftovers>
   00:07:58  <Collection.moveMusicToStage>
   00:07:58  <Directory.mkdirs>
   00:07:58  <MusicFile.move>                    spieluhr.mp3
   00:07:58  <MusicFile.move>                    'links 2 3 4.mp3'
   00:07:58  <MusicFile.move>                    'ich will.mp3'
   00:07:58  <MusicFile.move>                    sonne.mp3
   00:07:58  <MusicFile.move>                    'rein raus.mp3'
   00:07:58  <MusicFile.move>                    nebel.mp3
   00:07:58  <MusicFile.move>                    adios.mp3
   00:07:58  <MusicFile.move>                    zwitter.mp3
   00:07:58  <MusicFile.move>                    'mein herz brennt.mp3'
   00:07:58  <MusicFile.move>                    mutter.mp3
   00:07:58  <MusicFile.move>                    'feuer frei.mp3'
   00:07:58  <Collection.removeEmptyDirectories>
   00:07:58  <Collection.moveFilesPermanently>
   00:07:58  <Collection.removeStageDirectory>
   00:07:58  <Directory.remove>                __STAGE
   00:07:58  <Collection.removeLeftoversDirectory>
   00:07:58  <Directory.remove>                __LEFTOVERS
   00:07:58  <Collection.finish>

``--format``
------------
Use ``--format`` to specify how your music folder should be organized.

Default format: hash-based naming
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The default behavior leverages unique MD5 hashes for large multi-terabyte music
collections and favors naming compatibility over readable filenames:

``{artist}/{album}/{artist}-{hash}.{ext}``

.. code-block:: console

   Music
   └── rammstein
       └── mutter
           ├── rammstein-1777b3a4c02565cec36c3e5f71f40102.mp3
           ├── rammstein-2ec6d3d6fc625fa6ea93ae283175f13c.mp3
           └── rammstein-5bd7b80dbc746b409bc8a6093b65d1c3.mp3

Conventional three-level
^^^^^^^^^^^^^^^^^^^^^^^^
``{artist}/{album}/{artist}-{title}.{ext}``

.. code-block:: console

   Music
   └── rammstein
       ├── mutter
       │   ├── rammstein-adios.mp3
       │   ├── rammstein-feuer frei.mp3
       │   ├── rammstein-ich will.mp3
       │   └── rammstein-zwitter.mp3
       ├── rosenrot
       │   ├── rammstein-benzin.mp3
       │   ├── rammstein-ein lied.mp3
       │   └── rammstein-feuer und wasser.mp3
       └── sehnsucht
           ├── rammstein-alter mann.mp3
           ├── rammstein-bestrafe mich.mp3
           ├── rammstein-bueck dich.mp3
           └── rammstein-tier.mp3

Two-level artist-only folders
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
``{artist}/{album}-{title}.{ext}``

.. code-block:: console

   Music
   └── rammstein
       ├── mutter-adios.mp3
       ├── mutter-feuer frei.mp3
       ├── mutter-zwitter.mp3
       ├── rosenrot-benzin.mp3
       ├── rosenrot-ein lied.mp3
       ├── rosenrot-feuer und wasser.mp3
       ├── sehnsucht-alter mann.mp3
       ├── sehnsucht-bestrafe mich.mp3
       └── sehnsucht-tier.mp3

Put it all in one folder because I'm crazy!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
``{artist}:{album} - {title}.{ext}``

.. code-block:: console

   Music/
   ├── rammstein:mutter - adios.mp3
   ├── rammstein:mutter - feuer frei.mp3
   ├── rammstein:mutter - ich will.mp3
   ├── rammstein:rosenrot - benzin.mp3
   ├── rammstein:rosenrot - ein lied.mp3
   ├── rammstein:rosenrot - feuer und wasser.mp3
   ├── rammstein:sehnsucht - alter mann.mp3
   ├── rammstein:sehnsucht - bestrafe mich.mp3
   └── rammstein:sehnsucht - tier.mp3
