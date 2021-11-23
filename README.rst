==========
tagrenamer
==========

.. image:: https://img.shields.io/github/languages/top/nielsvm/tagrenamer.svg

.. image:: https://img.shields.io/github/license/nielsvm/tagrenamer.svg
        :target: https://raw.githubusercontent.com/nielsvm/tagrenamer/master/LICENSE

.. image:: https://img.shields.io/pypi/v/tagrenamer.svg
        :target: https://pypi.python.org/pypi/tagrenamer

.. image:: https://img.shields.io/github/v/release/nielsvm/tagrenamer.svg
        :target: https://github.com/nielsvm/tagrenamer/releases

*Mass music collection renamer.*

**Tagrenamer completely cleans up your music folder for you, all you need**
**to do is to make sure all music files have the right tags.**

Imagine this is inside your music folder:

.. code-block:: bash

   Music/
   ├── MUTTER (2001) - Adios.mp3
   ├── MUTTER (2001) - Feuer Frei.mp3
   ├── MUTTER (2001) - Ich Will.mp3
   ├── MUTTER (2001) - Links 2 3 4.mp3
   ├── MUTTER (2001) - Mein Herz Brennt.mp3
   ├── MUTTER (2001) - Mutter.mp3
   ├── MUTTER (2001) - Nebel.mp3
   ├── MUTTER (2001) - Rein Raus.mp3
   ├── MUTTER (2001) - Sonne.mp3
   ├── MUTTER (2001) - Spieluhr.mp3
   └── MUTTER (2001) - Zwitter.mp3

What a mess, let's clean it up:

.. code-block:: bash

   $ tagrenamer --format '{artist}/{album}/{artist}-{title}.{ext}' Music/
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

.. code-block:: bash

   Music/
   └── rammstein
       └── mutter
           ├── rammstein-adios.mp3
           ├── rammstein-feuer frei.mp3
           ├── rammstein-ich will.mp3
           ├── rammstein-links 2 3 4.mp3
           ├── rammstein-mein herz brennt.mp3
           ├── rammstein-mutter.mp3
           ├── rammstein-nebel.mp3
           ├── rammstein-rein raus.mp3
           ├── rammstein-sonne.mp3
           ├── rammstein-spieluhr.mp3
           └── rammstein-zwitter.mp3

Features
--------

#. **Python**

   Pure Python command-line application that is cross-platform and strives to
   meet all modern quality criteria such as PEP8-compliance and test coverage.
#. **Formats**

   Supports ``.mp3``, ``.ogg`` and ``.flac`` files and more are easy to add.

#. **Only deals with music**

   Files that are not music, are moved into a folder named ``__LEFTOVERS/``
   which contains the original structure they were originally in. Letting you
   decide what to do with them.

#. **Fail-safe**

   Tagrenamer leverages an internal staging process in which it detects failures
   before it touched a single file. The paranoid can combine ``--dry-run`` and
   ``-vvvv`` to see what is going on under the hood or even run with ``--shell``
   to generate Shell commands for you to inspect without renaming anything.

#. **Scalability**

   Renames a few music albums as well as a 2Tb music collection.

Installation
------------

Follow these instructions:

* ``git clone https://github.com/nielsvm/tagrenamer.git``
* ``pip3 install -r requirements.txt``
* ``cd tagrenamer/``
* ``./tagrenamer --help``

Development
^^^^^^^^^^^

* ``pip3 install -r requirements_dev.txt``

Usage
-----

.. code-block:: bash

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

Formatting
^^^^^^^^^^
Use ``--format`` to specify how your music folder should be organized.

Default format: hash-based naming
"""""""""""""""""""""""""""""""""
The default behavior leverages unique MD5 hashes for large multi-terabyte music
collections and favors naming compatibility over readable filenames:

``{artist}/{album}/{artist}-{hash}.{ext}``

.. code-block:: bash

   Music
   └── rammstein
       └── mutter
           ├── rammstein-1777b3a4c02565cec36c3e5f71f40102.mp3
           ├── rammstein-2ec6d3d6fc625fa6ea93ae283175f13c.mp3
           └── rammstein-5bd7b80dbc746b409bc8a6093b65d1c3.mp3

Conventional three-level
""""""""""""""""""""""""
``{artist}/{album}/{artist}-{title}.{ext}``

.. code-block:: bash

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
"""""""""""""""""""""""""""""
``{artist}/{album}-{title}.{ext}``

.. code-block:: bash

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
"""""""""""""""""""""""""""""""""""""""""""
``{artist}:{album} - {title}.{ext}``

.. code-block:: bash

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
