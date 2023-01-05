#!/usr/bin/python3
# an empty class Rectangle that defines a rectangle
# You are not allowed to import any module
# for now we are going to add:
# prinvate attributes width and height with
# setter and getter methods
"""
    define class 'Rectangle'
"""


class Rectangle:
    """
        this is an empty class
    """
    def __init__(self, width=0, height=0):
        """
            this is an init method, it has 
            atributes height and width
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
            this is a getter method for width attribut
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            this method will help us to set and change the value
            of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            this method will help us to get the value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            this method is the one we will use to
            modify the value of height
        """
        if not isinstance(value, int):
            raise TypeError("height must an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
