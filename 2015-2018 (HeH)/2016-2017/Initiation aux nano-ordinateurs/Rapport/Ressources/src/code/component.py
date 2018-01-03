from abc import ABC, abstractmethod

class Component(ABC):
    """
    Creates a new type of object: 'Component'.
    """

    DEFAULT_COLOR = '\033[0;0m'

    def __init__(self, x, y, symbol, color):
        """
        Constructs a new 'Component' object.

        :param x:      X-Axis of the component
        :param y:      Y-Axis of the component
        :param symbol: Symbol of the component
        :param color:  Color of the component
        """
        self.x      = x
        self.y      = y
        self.symbol = symbol
        self.color  = color


    def __str__(self):
        """
        Displays the component.
        """
        return str(self.color + self.SYMBOL + self.DEFAULT_COLOR)


    def __repr__(self):
        """
        Represents the component.
        """
        return str(self.color + self.SYMBOL + self.DEFAULT_COLOR)


    @abstractmethod
    def move(self):
        """
        Moves the component according to the X-Axis and Y-Axis.
        """
        pass
