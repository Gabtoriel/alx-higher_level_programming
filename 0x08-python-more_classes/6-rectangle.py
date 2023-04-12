#!/usr/bin/python3

"""Create a rectangle class to create rectangle objects."""


class Rectangle:

    """Creates a rectangle object."""

    # Holds the number of object instances created
    number_of_instances = 0

    def __init__(self, width=0, height=0):

        """Initailizes every rectangle object."""

        self.__width = self.width = width
        self.__height = self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):

        """Returns(gets) the width of rectangle."""

        return self.__width

    @width.setter
    def width(self, value):

        """Sets the width of the rectangle object."""

        if not (isinstance(value, int)):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):

        """Gets or returns the height of the rectangle."""

        return self.__height

    @height.setter
    def height(self, value):

        """Sets the height of the rectangle."""

        if not (isinstance(value, int)):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):

        """Calculates the area of a rectangle."""

        return self.height * self.width

    def perimeter(self):

        """Calculates the perimeter of the rectangle"""

        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):

        """Returns the informal string format of the rectangle object."""

        if self.width == 0 or self.height == 0:
            return ""

        line = '#'
        i = 0
        while i < self.height:
            len_line = 0
            while len_line < self.width:
                if len_line == (self.width - 1) and i == (self.height - 1):
                    break
                elif len_line == (self.width - 1):
                    line += '\n'
                    line += '#'
                    break
                line = line + "#"
                len_line += 1
            i = i + 1
        return line

    def __repr__(self):

        """Returns an official string format of an instance."""

        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):

        """Detects the deletion of the rectangle class."""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")


if __name__ == "__main__":
    a = Rectangle(10, 20)
    b = Rectangle(20, 5)
    print("No of instances {:d}".format(Rectangle.number_of_instances))
    del b
    print("No of instances {:d}".format(Rectangle.number_of_instances))
    print("Program ends here")
