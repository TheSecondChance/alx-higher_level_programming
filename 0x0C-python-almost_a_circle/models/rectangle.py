#!/usr/bin/python3
"""Import from models dirctory"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor

        Args:
            width (int): width of Rectangle
            height (int): height of Rectangle
            x (int): Defaults to 0.
            y (int): Defaults to 0.
            id (int, _type_): The number of instantiat of the base.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Width Getter

        Returns:
            int: private attribute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Width Setter

        Args:
            value (int): Rectangle width value
        Raises:
            TypeError: value must be int
            ValueError: value must be >= 0
        """
        if type(value) is not int:
            raise TypeError(f"width must be an integer")
        if value <= 0:
            raise ValueError(f"width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Height Getter

        Returns:
            int: private attribute height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Height Setter

        Args:
            value (int): Rectangle height value
        Raises:
            TypeError: value must be int
            ValueError: value must be >= 0
        """
        if type(value) is not int:
            raise TypeError(f"height must be an integer")
        if value <= 0:
            raise ValueError(f"height must be > 0")
        self.__height = value

    @property
    def x(self):
        """X Getter

        Returns:
            int: private attribute x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """X Setter

        Args:
            value (int): Rectangle X value
        """
        if type(value) is not int:
            raise TypeError(f"x must be an integer")
        if value < 0:
            raise ValueError(f"x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Y Getter

        Returns:
            int: private attribute y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Y Setter

        Args:
            value (int): Rectangle Y value
        """
        if type(value) is not int:
            raise TypeError(f"y must be an integer")
        if value < 0:
            raise ValueError(f"y must be >= 0")
        self.__y = value

    def area(self):
        """The Area of Rectangle

        Returns:
            int: the area of the Rectangle"""
        return self.width * self.height

    def display(self):
        """Print in stdout the Rectangle,
        instance with the character #
        """
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("") for y in range(self.y)]
        for hei in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for wid in range(self.width)]
            print("")

    def __str__(self):
        """String representation of Rectangle

        Returns:
            str: representation of Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                    self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args and len(args) != 0:
            check = 0
            for arg in args:
                if check == 0:
                    self.id = arg
                elif check == 1:
                    self.width = arg
                elif check == 2:
                    self.height = arg
                elif check == 3:
                    self.x = arg
                elif check == 4:
                    self.y = arg
                check += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Public method def dictionary

        Returns:
            dict: dictionary representaion of a rectangle
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
