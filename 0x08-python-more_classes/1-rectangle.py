#!/usr/bin/python3

"""Create a rectangle class to create rectangle objects."""


class Rectangle:

    """Creates a rectangle object."""


    def __init__(self, width=0, height=0):
        
        """Initailizes every rectangle object."""
        
        	
        self.__width = width
        self.__height = height

    @property
    def width(self):
             
        """Returns(gets) the width of rectangle."""
        
        return self.__width
    
    @width.setter
    def width(self, value):
        
        """Sets the width of the rectangle object."""

        if type(value) != type(0):
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

        if type(value) != type(0):
            raise TypeError("height must be integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

if __name__ == "__main__":
    a = Rectangle(10, 20)
    print(a.height)
    print(a.width)
    a.height = 5
    a.width = 10 
    a.height = 10.5
    a.width = 5.5
    a.height = -10
    a.width = -5
