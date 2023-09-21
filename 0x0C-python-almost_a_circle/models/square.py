#!/usr/bin/python3

"""Program to create the square object of the model package."""


from .rectangle import Rectangle


class Square(Rectangle):

    """The square class of the model package
    it inherits from the rectangle class.
    All square objects instantiate from here.
    """

    def __init__(self, size, x=0, y=0, id=None):

        """Initializes all square objects."""

        super().__init__(size, size, x, y, id)

    def __str__(self):

        """Returns the informal string format of the rectangle object."""

        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):

        """Gets the size of the square."""

        return self.width

    @size.setter
    def size(self, size):

        """Sets the width and height of the square object."""

        self.width = size
        self.height = size

    def update(self, *args, **kwargs):

        """Updates the attributes of the rectangle class using variable
        length parameters."""

        if args and len(args) > 0:
            if args[0]:
                self.id = args[0]
            if args[1]:
                self.width = args[1]
                self.height = args[1]
            if args[3]:
                self.x = args[2]
            if args[4]:
                self.y = args[3]
        else:
            if kwargs is not None and kwargs != {}:
                for key in kwargs:
                    if key == "id":
                        self.id = kwargs[key]
                    if key == "size":
                        self.width = kwargs[key]
                        self.height = kwargs[key]
                    if key == "x":
                        self.x = kwargs[key]
                    if key == "y":
                        self.y = kwargs[key]

    def to_dictionary(self):

        """Instance method to return the dict representation of a square
        instance."""

        return dict(id=self.id, size=self.width, x=self.__x, y=self.__y)
