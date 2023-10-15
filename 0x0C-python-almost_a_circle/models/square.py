#!/usr/bin/python3
"Import from models directory"
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class

    Args:
        Rectangle (class): inherit
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square

        Args:
            size (int): size of square
            x (int): Defaults to 0.
            y (int): Defaults to 0.
            id (int): id Base
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of the square

        Returns:
            str: string represent
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """Getter size

        Returns:
            int: size of Square
        """
        return self.width

    @size.setter
    def size(self, value):
        """Setter size

        Args:
            value (int): size of square
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square assigns attributes"""

        if args and len(args) != 0:
            check = 0
            for arg in args:
                if check == 0:
                    self.id = arg
                elif check == 1:
                    self.size = arg
                elif check == 2:
                    self.x = arg
                elif check == 3:
                    self.y = arg
                check += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Public method def dictionary

        Returns:
            dict: dictionary representaion of a rectangle
        """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
