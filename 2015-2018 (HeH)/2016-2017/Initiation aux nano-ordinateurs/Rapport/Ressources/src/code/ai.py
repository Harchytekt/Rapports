class Ai(object):
    """
    Creates a new type of object: 'Ai'.
    """

    def __init__(self, paddle):
        """
        Constructs a new 'Ai' object.

        :param paddle: The ai paddle
        """
        self.paddle = paddle


    def distance(self, ball, paddle):
        """
        Calculates the distance between the paddle and the ball.

        :param ball:   The ball
        :param paddle: The ai paddle

        :return: Returns the distance between the paddle
                 and the ball.
        """
        return ball.y - paddle.y


    def goLeftUp(self, ball, paddle):
        """
        Verifies if the paddle can go up.

        :param ball:   The ball
        :param paddle: The ai paddle

        :return: return: Returns true if the paddle can go up,
                         false otherwise.
        """
        return ball.x < paddle.x




    def goLeftDown(self, ball, paddle):
        """
        Verifies if the paddle can go down.

        :param ball:   The ball
        :param paddle: The ai paddle

        :return: return: Returns true if the paddle can go down,
                         false otherwise.
        """
        return ball.x > paddle.x


    def debug(self, ball, paddle):
        """
        Useful debug method by displaying infos about the ai.

        :param ball:   The ball
        :param paddle: The ai paddle
        """
        print(' ' * 5 + '[ AI Mode ]' + ' ' * 5 + '\n')
        if (self.goLeftUp(ball, paddle)):
            print('Direction to take: UP')
        else:
            print('Direction to take: DOWN')
        print('Distance from the ball: ',
        str(self.distance(ball, paddle)) + '\n')

    def play(self, ball, paddle):
        """
        Makes the ai play the game.

        :param ball:   The ball
        :param paddle: The ai paddle
        """
        if self.paddle.ID == 'Left' and ball.y <= 3:
            # self.debug(ball, paddle)
            if self.goLeftUp(ball, paddle):
                paddle.x = paddle.x - 1
            elif self.goLeftDown(ball, paddle):
                paddle.x = paddle.x + 1
        elif self.paddle.ID == 'Right' and ball.y >= 3:
            if self.goLeftUp(ball, paddle):
                paddle.x = paddle.x - 1
            elif self.goLeftDown(ball, paddle):
                paddle.x = paddle.x + 1
