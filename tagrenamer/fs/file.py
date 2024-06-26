# -*- coding: utf-8 -*-
"""
Represent an ordinary file found on the file system.
"""
from tagrenamer.fs.node import Node


class File(Node):
    """
    Represent an ordinary file found on the file system.
    """

    def __init__(self, output, settings, path, extension,
                 callbacks={}, parent=None, dl=1):
        """Initialize the file object."""
        Node.__init__(
            self,
            output=output,
            settings=settings,
            path=path,
            callbacks=callbacks,
            parent=parent,
            dl=dl)

        # Set the extension if available.
        self.extension = ''
        if '.' in self.base:
            self.extension = extension
