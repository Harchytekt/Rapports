#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '/usr/lib/python2.7/dist-packages/sense_hat')
from sense_emu import SenseHat

from ball import *
from paddle import *
from ground import *
from ai import *

import time
import os

#
# Copyright (C) 2017 Terencio Agozzino <terencio.agozzino@gmail.com>
#                Alexandre Ducobu  <alexandre.ducobu@yahoo.be>
#
# PyPong is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyPong is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

YELLOW = "\033[1;33m"
sense = SenseHat()
sense.low_light = True


def displayInfo(fps, timeElapsed, timeStart):
    """
    Useful to get information about the game.

    :param fps:        Frames per second of the game
    :param timeStart:   Time start for the processus.
    :param timeElapsed: Time elapsed for the processus.
    :param timeEnd:    Time end for the processus.
    """
    print(' ' * 5 + '[ Game Info ]' + ' ' * 5 + '\n' * 2
         + 'FPS: ' + str(fps) + '\n'
         + 'Time Elapsed: ' + str(timeElapsed) + '\n'
         + 'Time Start: ' + str(timeStart) + '\n')


def render(ground):
    """
    Renders the game.

    :param ground: ground of the game
    """

    game = ground.update()
    printArray(ground.array)
    time.sleep(ground.ball.speed)
    ground.ball.speed = ground.ball.InitialSpeed
    os.system('clear')
    return game

def printArray(array):
    """
    Displays an array.

    :param array: Array
    """
    for j in range(len(array)):
       for i in range(len(array)):
          if array[i][j] == 0:
             sense.set_pixel(j, i, [0, 0, 0])
          elif isinstance(array[i][j], Ball):
             sense.set_pixel(j, i, [255,255,255])
          else:
             sense.set_pixel(j, i, [173, 0, 0])

def start():
    """
    Starts the game.
    """

    level = 1

    frames = []
    timeStart = time.process_time()

    game = True

    sense.show_message("PyPong")
    time.sleep(0.2)
    sense.show_message("3")
    time.sleep(0.1)
    sense.show_message("2")
    time.sleep(0.1)
    sense.show_message("1")
    time.sleep(0.1)
    sense.show_message("Go!")

    player1 = 0
    player2 = 0

    speed = 0.6
    games = 0

    while (player1 != 3 and player2 != 3):
        games += 1
        ball = Ball(4, 4, 1, speed, YELLOW)
        ground = Ground(8, 8, ball, level)
        sense.stick.direction_up = ground.pushed_up
        sense.stick.direction_down = ground.pushed_down
        gameIsOn = True
        while (gameIsOn):
            gameIsOn, result = render(ground)
            if gameIsOn:
                timeEnd = time.process_time()
                timeElapsed = timeEnd - timeStart

                timeStart = timeEnd

                frames.append(timeElapsed)
                frames = frames[-20:]
                fps = len(frames) / sum(frames)

        if level < 3:
            sense.show_message(str(result))
            sense.show_message('points')
            if games == 3:
               level += 1
               speed -= 0.01
               games = 0
               sense.show_message('Level ' + str(level) + '!')
        else:
            if result == 1:
               player1 = player1 + 1
            else:
               player2 = player2 + 1
            sense.show_message(str(player1) + ':' + str(player2))
        speed -= 0.02

        time.sleep(1)
    sense.show_message("End")

if __name__ == '__main__':
    start()
