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
