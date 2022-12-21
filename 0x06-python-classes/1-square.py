#!/usr/bin/python3
# an empty class Square that defines a square
# for now we will add a private attribute 'size'
"""
    define class 'Square'
"""


class Square:
    """
	this class has private instance attribute 'size'
    """
    def __init__(self, size):
	"""
	    this is an init method
	"""
	self.__size = size
