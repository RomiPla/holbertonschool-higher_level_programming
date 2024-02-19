#!/usr/bin/python3
"""
Creation of the class 
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor of Square """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Roo"""

        return("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width))

    @property
    def size(self):
        """Roo"""

        return self.width

    @size.setter
    def size(self, value):
        """Roo"""

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Roo"""

        if len(args) > 0:

            for i in range(len(args)):

                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                    self.height = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]

        else:

            if len(kwargs) > 0:

                k = kwargs.keys()

                for i in k:

                    if i == 'id':
                        self.id = kwargs['id']
                    if i == 'size':
                        self.width = kwargs['size']
                        self.height = kwargs['size']
                    if i == 'x':
                        self.x = kwargs['x']
                    if i == 'y':
                        self.y = kwargs['y']

    def to_dictionary(self):
        """Roo"""

        dictionary = {}
        dictionary['id'] = self.id
        dictionary['size'] = self.width
        dictionary['x'] = self.x
        dictionary['y'] = self.y
        return dictionary