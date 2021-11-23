===========
Development
===========

Acquiring the source code
-------------------------

Clone the repository to your computer:

.. code-block:: console

    $ git clone git://github.com/nielsvm/tagrenamer

.. code-block:: console

    $ cd tagrenamer/

Or download the `tarball`_:

.. code-block:: console

    $ curl -OJL https://github.com/nielsvm/tagrenamer/tarball/master

.. _tarball: https://github.com/nielsvm/tagrenamer/tarball/master

Local installation
------------------

First install all dependencies:

.. code-block:: console

    $ pip3 install -r requirements.txt

.. code-block:: console

    $ pip3 install -r requirements_dev.txt


Then, install ``tagrenamer`` locally like this:

.. code-block:: console

    python3 setup.py install --user


Uninstall:

.. code-block:: console

    $ pip3 uninstall tagrenamer

Documentation
-------------

Loop documentation building using:

.. code-block:: console

    $ make servedocs

One-off build:

.. code-block:: console

    $ make clean
    $ make docs

