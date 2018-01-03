from component import *

class Paddle(Component):
    """
    Creates a new type of object: 'Paddle'.
    """

    SYMBOL = '|'
    NAME   = 'Paddle'


    def __init__(self, x, y, ID, size, color):
        """
        Constructs a new 'Paddle' object.

        :param x:     X-Axis of the paddle
        :param y:     Y-Axis of the paddle
        :param ID:    ID of the paddle
        :param size:  Size of the paddle
        :param color: Color of the paddle
        """
        super(self.__class__, self).__init__(x, y, self.SYMBOL, color)
        self.ID        = ID
        self.size      = size
        self.direction = 1 #-1: up; 1: down; 0 fixe

    def __str__(self):
        """
        Displays the paddle.
        """
        return str(self.color + self.SYMBOL + self.DEFAULT_COLOR)

    def __repr__(self):
        """
        Represents the paddle.
        """
        return str(self.color + self.SYMBOL + self.DEFAULT_COLOR)

    def move(self):
        """
        Moves the paddle.
        """
        self.y += self.direction
