from ball import *
from paddle import *
from ai import *

import time

class Ground(object):
    """
    Creates a new type of object: 'Ground'.
    """

    RED     = "\033[1;31m"
    BLUE    = "\033[1;34m"
    YELLOW  = "\033[1;33m"
    CYAN    = "\033[1;36m"
    GREEN   = "\033[0;32m"
    DEFAULT = "\033[0;0m"
    BOLD    = "\033[;1m"
    stickMove = 0


    def __init__(self, row, column, ball, level):
        """
        Constructs a new 'Ground' object.

        :param row:    X-Axis length of the ground
        :param column: Y-Axis length of the ground
        :param ball:   Ball of the ground
        :param level:  Level of the ground
        """
        self.row         = row
        self.column      = column

        self.ball        = ball

        self.level       = level
        self.result      = 0

        if self.level < 3:
            self.paddle      = Paddle((self.row // 2) + 1,
                self.column-2, 'Right', 2, self.RED)
            self.components  = [self.ball, self.paddle]
            self.positions   = [ball.y, ball.x, self.paddle.y,
                self.paddle.x]

        else:
            self.paddleLeft  = Paddle(self.row // 2, 1, 'Left',
                2, self.RED)
            self.paddleRight = Paddle((self.row // 2) + 1,
                self.column-2, 'Right', 2, self.CYAN)
            self.components  = [self.ball, self.paddleLeft,
                self.paddleRight]
            self.positions   = [ball.y, ball.x, self.paddleLeft.y,
                self.paddleLeft.x, self.paddleRight.x,
                self.paddleRight.y]
            self.ai          = Ai(self.paddleLeft)

        self.array       = self.generateGround(row, column)

        self.initComponents(self.components)


    def _str__(self):
        """
        Displays the ground.
        """
        return str(self.array[i])


    def cleanPositions(self):
        """
        Removes the old positions of the components.
        """
        self.array[self.positions[0]][self.positions[1]] = 0
        self.array[self.positions[2]][self.positions[3]] = 0
        if self.level == 3:
            self.array[self.positions[4]][self.positions[5]] = 0

    def debug(self, components):
        """
        Useful debug method by displaying X-Axis and Y-Axis
        of components.

        :param components: List of components
        """
        print(' ' * 5 + '[ Debug Mode ]' + ' ' * 5 + '\n')
        for component in components:
            print(component.NAME + "(x=" + str(component.x)
                                 + ", y=" + str(component.y) + ")")
        print('\n')


    def generateGround(self, row, column):
        """
        Generates the ground.

        :param row:    Number of rows for the ground
        :param column: Number of columns for the ground
        """
        return [[0 for i in range(row)] for j in range(column)]


    def initComponents(self, components):
        """
        Initializes the components in the array.

        :param components: List of components
        """
        for component in components:
            self.array[component.x][component.y] = component


    def isWinner(self):
        """
        Returns the result of the current game.

        :return: Returns the score if the level is lower than 3,
                 1 if the first player wins, 2 for the second.
        """
        if self.level < 3:
            return self.result
        if self.ball.y < 0:
            return 2
        elif self.ball.y > 7:
            return 1


    def isPaddleCollision(self):
        """
        If there is a collision with a paddle,
        the direction of the ball changes et the score is upgraded.
        """
        if self.level < 3:
            if self.ball.y == self.column - 2 and
                self.ball.x == self.paddle.x:
                self.ball.dy = -self.ball.dy
                self.result += 2
                self.ball.speed -= 0.15
        else:
            if (self.ball.y == 1 and
              self.ball.x == self.paddleLeft.x) or
              (self.ball.y == self.column - 2 and
              self.ball.x == self.paddleRight.x):
                self.ball.dy = -self.ball.dy
                self.ball.speed -= 0.15


    def isOut(self):
        """
        Detects if the ball is out of bounds.

        :return: Returns true if the ball is out of bounds,
                         false otherwise.
        """
        if self.level < 3:
            return self.ball.y == self.column - 1
        return self.ball.y == 0 or self.ball.y == self.column - 1


    def isWallCollision(self):
        """
        Detects if there is a collision with the ball
        and the bottom or top of the wall or with the
        right side of the ground.
        """
        if self.level < 3:
            if self.ball.x == 0 or self.ball.x == self.row - 1:
                #Roof
                self.ball.dx = -self.ball.dx
                self.result += 3
                self.ball.speed -= 0.1
            if self.ball.y == 0:
                #Left side
                self.ball.dy = -self.ball.dy
                self.result += 3
                self.ball.speed -= 0.1
        else:
            if self.ball.x == 0 or self.ball.x == self.row - 1:
                #Roof
                self.ball.dx = -self.ball.dx
                self.ball.speed -= 0.1


    def pushedUp(self):
        """
        If the joystick of the Sense HAT is pushed up,
        the paddle is moved upwards.
        """
        self.stickMove = -1


    def pushedDown(self):
        """
        If the joystick of the Sense HAT is pushed down,
        the paddle is moved downwards.
        """
        self.stickMove = 1


    def movePaddle(self, move):
        """
        Verifies if the paddle can move.
        If it can, it'll from the direction given by the Sense HAT.
        """
        if self.level < 3:
            if not ((self.paddle.x == 0 and self.stickMove == -1)
              or (self.paddle.x == self.row-1
              and self.stickMove == 1)):
                self.paddle.x += move
        else:
            if not ((self.paddleRight.x == 0 and
              self.stickMove == -1) or
              (self.paddleRight.x == self.row-1 and
              self.stickMove == 1)):
                self.paddleRight.x += move


    def update(self):
        """
        Updates the game.
        """
        self.cleanPositions()
        out = True

        if self.isOut():
            out = False

        if self.level < 3:
            self.movePaddle(self.stickMove)

            if out:
                self.isWallCollision()
                self.isPaddleCollision()

            self.positions[0] = self.ball.x
            self.positions[1] = self.ball.y

            self.positions[2] = self.paddle.x
            self.positions[3] = self.paddle.y

            self.array[self.positions[2]][self.positions[3]] =
                self.paddle
        else:
            self.movePaddle(self.stickMove)

            self.isWallCollision()
            self.isPaddleCollision()

            self.positions[0] = self.ball.x
            self.positions[1] = self.ball.y

            self.positions[2] = self.paddleLeft.x
            self.positions[3] = self.paddleLeft.y
            self.positions[4] = self.paddleRight.x
            self.positions[5] = self.paddleRight.y

            self.array[self.positions[2]][self.positions[3]] =
                self.paddleLeft
            self.array[self.positions[4]][self.positions[5]] =
                self.paddleRight

        self.array[self.positions[0]][self.positions[1]] = self.ball

        self.ball.move()
        if self.level == 3:
            self.ai.play(self.ball, self.paddleLeft)
            winner = self.isWinner()
        else:
            winner = self.isWinner()

        self.stickMove = 0

        return out, winner
