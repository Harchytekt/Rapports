from component import *
from random import randrange

class Ball(Component):
    """
    Creates a new type of object: 'Ball'.
    """

    SYMBOL = 'o'
    NAME   = 'Ball'

    def __init__(self, x, y, side, speed, color):
        """
        Constructs a new 'Ball' object.

        :param x:     X-Axis of the ball
        :param y:     Y-Axis of the ball
        :param side:  Size of the ball
        :param speed: Speed of the ball
        :param color: Color of the ball
        """
        super(self.__class__, self).__init__(x, y, self.SYMBOL, color)
        self.side         = side
        self.dx           = 0
        self.dy           = 0
        t                 = [-135, 135]
        self.angle        = t[randrange(2)]
        self.InitialSpeed = speed
        self.speed        = speed
        self.setDirection()


    def __str__(self):
        """
        Displays the ball.
        """
        return str(self.color + self.SYMBOL + self.DEFAULT_COLOR)


    def __repr__(self):
        """
        Represents the ball.
        """
        return str(self.color + self.SYMBOL + self.DEFAULT_COLOR)


    def setDirection(self):
        """
        Sets the direction the ball according to an angle.

          dx: vertical   (-1: up; 0: none; 1: down)
          dy: horizontal (-1: left; 0: none; 1: right)
        """
        if self.angle == -135:
            self.dx = 1
            self.dy = -1
        elif self.angle == -45:
            self.dx = 1
            self.dy = 1
        elif self.angle == 45:
            self.dx = -1
            self.dy = 1
        else:
            self.dx = -1
            self.dy = -1


    def move(self):
        """
        Moves the ball according to the calculated direction.
        """
        self.x += self.dx
        self.y += self.dy
