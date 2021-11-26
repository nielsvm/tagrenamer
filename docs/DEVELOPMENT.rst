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

Install Tagrenamer into your home folder like this:

.. code-block:: console

    $ pip3 install -r requirements.txt
    $ python3 setup.py install --user

.. code-block:: console

    $ tagrenamer --help

Development installation
------------------------

.. code-block:: console

    $ make venv
    $ source venv/bin/activate
    $ python3 setup.py develop --user

.. code-block:: console

    $ tagrenamer --help

Uninstall
---------

Regardless of how you installed it, uninstall using ``pip``:

.. code-block:: console

    $ pip3 uninstall tagrenamer

Documentation
-------------

.. code-block:: console

    $ make venv
    $ source venv/bin/activate
    $ make docs

Constant documentation build during editing:

.. code-block:: console

    $ make servedocs

Release
-------

.. code-block:: console

    $ bumpversion --allow-dirty --new-version x.x.x major
    $ nano CHANGELOG.rst
    $ git add -p
    $ git commit -m "version bump"

.. code-block:: console

    $ git tag x.x.x
    $ git push --tags

.. code-block:: console

    $ make venv
    $ source venv/bin/activate

.. code-block:: console

    $ make dist
    $ make release

.. code-block:: console

    $ curl -X POST -d "branches=master" -d "token=..." https://readthedocs.org/api/v2/webhook/tagrenamer/.../
