#!usr/bin/python3

"""Program to create a rectangle class."""

from .base import Base


class Rectangle(Base):

    """Creates a rectangle class that inherits from
    the base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):

        """Initialiazes every rectangle object."""

        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):

        """Gets the private width attribute of a rectangle instance."""

        return self.__width

    @width.setter
    def width(self, width):

        """Sets the private width attribute of a rectangle instance."""

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):

        """Gets the private height attribute of a rectangle instance."""

        return self.__height

    @height.setter
    def height(self, height):

        """Sets the private height attribute of a rectangle instance."""

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):

        """Gets the private x attribute of a rectangle instance."""

        return self.__x

    @x.setter
    def x(self, x):

        """Sets the private x attribte of a rectangle instance."""

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):

        """Gets the private y attribute of a rectangle instance."""

        return self.__y

    @y.setter
    def y(self, y):

        """Sets the private y attribute of a rectangle instance."""

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):

        """Routine to calculate the area of a rectangle."""

        return (self.__width * self.__length)

    def display(self):

        """Draws a rectangle on the command line using # based on
        the width and height."""

        # handles y by printing newlines
        for s in range(self.__y):
            print()
        # handles the height
        for i in range(self.__height):
            # handles the width
            for j in range(self.__width):
                # handles the x attribute by printing spaces
                for k in range(self.__x):
                    print(' ', end='')
                print('#', end='')
            print()

    def __str__(self):

        """Returns the informal string format of the rectangle object."""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):

        """Updates the attributes of the rectangle class using variable
        length parameters."""

        if args and len(args) > 0:
            if args[0]:
                self.id = args[0]
            if args[1]:
                self.__width = args[1]
            if args[2]:
                self.__height = args[2]
            if args[3]:
                self.__x = args[3]
            if args[4]:
                self.__y = args[4]
        else:
            if kwargs is not None and kwargs != {}:
                for key in kwargs:
                    if key == "id":
                        self.id = kwargs[key]
                    if key == "width":
                        self.__width = kwargs[key]
                    if key == "height":
                        self.__height = kwargs[key]
                    if key == "x":
                        self.__x = kwargs[key]
                    if key == "y":
                        self.__y = kwargs[key]
