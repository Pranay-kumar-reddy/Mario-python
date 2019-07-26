'''player'''
import os
from time import sleep
from config import LIFE, POINTS, XCOR, YCOR, A, RIGHTC, LIFEPOSITION, COINPOSITION, ENEMY1POSITION, ENEMY2POSITION


class Man():
    '''Man'''

    def __init__(self):
        '''init'''
        self.x_x = XCOR[0]
        self.y_y = YCOR[0]
        global A

    def moving(self, key):
        '''moving'''
        global XCOR
        global YCOR
        global RIGHTC
        if key == "a":
            if A[self.x_x + 2][self.y_y - 1] == "@":
                A[self.x_x + 2][self.y_y - 1] = " "
                LIFE[0] = LIFE[0] + 1
                for i in range(len(LIFEPOSITION)):
                    if LIFEPOSITION[i] == self.y_y - 1:
                        A[self.x_x + 2][self.y_y - 1] = " "
                        LIFEPOSITION[i] = -2
                        printing()

            if A[self.x_x + 2][self.y_y - 1] == "$":
                A[self.x_x + 2][self.y_y - 1] = " "
                POINTS[0] = POINTS[0] + 10
                for i in range(len(COINPOSITION)):
                    if COINPOSITION[i] == self.y_y - 1:
                        A[self.x_x + 2][COINPOSITION[i]] = " "
                        COINPOSITION[i] = -2
                        printing()

            if A[self.x_x][self.y_y -
                           1] == " " and A[self.x_x +
                                           1][self.y_y -
                                              1] == " " and A[self.x_x +
                                                              2][self.y_y -
                                                                 1] == " ":
                for i in range(3):
                    A[self.x_x + i][self.y_y + 2] = " "
                self.y_y = self.y_y - 1
                YCOR[0] = self.y_y

            image()
            printing()
            fall()

        if key == "d" and self.y_y < 149:
            if A[self.x_x + 2][self.y_y + 3] == "@":
                LIFE[0] = LIFE[0] + 1
                for i in range(len(LIFEPOSITION)):
                    if LIFEPOSITION[i] == self.y_y + \
                            3 or LIFEPOSITION[i] == self.y_y + 4:
                        A[self.x_x + 2][LIFEPOSITION[i]] = " "
                        LIFEPOSITION[i] = -2
                        printing()

            if A[self.x_x + 2][self.y_y + 3] == "$":
                POINTS[0] = POINTS[0] + 10
                for i in range(len(COINPOSITION)):
                    if COINPOSITION[i] == self.y_y + 3:
                        A[self.x_x + 2][COINPOSITION[i]] = " "
                        COINPOSITION[i] = -2
                        printing()

            if A[self.x_x][self.y_y + 3] == " " and A[self.x_x + 1][self.y_y +
                                                                    3] == " ":
                if A[self.x_x + 2][self.y_y + 3] == " ":
                    if self.y_y < 78:
                        for i in range(3):
                            A[self.x_x + i][self.y_y] = " "
                        self.y_y = self.y_y + 1
                        YCOR[0] = self.y_y

                    if A[self.x_x +
                         3][self.y_y] == "#" or A[self.x_x +
                                                  3][self.y_y +
                                                     1] == "#" or A[self.x_x +
                                                                    3][self.y_y +
                                                                       2] == "#":
                        for i in range(3):
                            A[self.x_x + i][self.y_y] = " "
                        self.y_y = self.y_y + 1
                        YCOR[0] = self.y_y

            image()
            printing()
            fall()
        if key == "z" and self.x_x > 6:
            for i in range(9):
                if i % 2 == 0:
                    sleep(0.03)
                if A[self.x_x - 1][self.y_y - 1] == " " and A[self.x_x -
                                                              1][self.y_y] == " ":
                    if A[self.x_x - 1][self.y_y + 1] == " ":
                        if A[self.x_x - 1][self.y_y +
                                           2] == " " and A[self.x_x][self.y_y - 1] == " ":
                            if A[self.x_x +
                                 1][self.y_y -
                                    1] == " " and A[self.x_x +
                                                    2][self.y_y -
                                                       1] == " ":
                                for i_i in range(3):
                                    A[self.x_x + i_i][self.y_y + 2] = " "
                                    A[self.x_x + 2][self.y_y + i_i] = " "
                                self.x_x = self.x_x - 1
                                self.y_y = self.y_y - 1
                                XCOR[0] = self.x_x
                                YCOR[0] = self.y_y
                                RIGHTC = RIGHTC - 1
                                image()
                                printing()
            k_1 = 1
            while True:
                if A[self.x_x][self.y_y -
                               1] == " " and A[self.x_x +
                                               1][self.y_y -
                                                  1] == " " and A[self.x_x +
                                                                  2][self.y_y -
                                                                     1] == " ":
                    if A[self.x_x +
                         3][self.y_y -
                            1] == " " and A[self.x_x +
                                            3][self.y_y] == " ":
                        if A[self.x_x + 3][self.y_y +
                                           1] == " " and A[self.x_x +
                                                           3][self.y_y +
                                                              2] == " ":
                            if k_1 % 2 == 0:
                                sleep(0.03)
                            k_1 = k_1 + 1
                            for i in range(3):
                                A[self.x_x][self.y_y + i] = " "
                                A[self.x_x + i][self.y_y + 2] = " "
                            self.x_x = self.x_x + 1
                            self.y_y = self.y_y - 1
                            XCOR[0] = self.x_x
                            YCOR[0] = self.y_y
                            RIGHTC = RIGHTC - 1
                            image()
                            printing()
                            if self.x_x >= 38:
                                fall()
                else:
                    break
            fall()

        if key == "w":
            for i in range(9):
                if i % 2 == 0:
                    sleep(0.03)
                if A[self.x_x -
                     1][self.y_y] == " " and A[self.x_x -
                                               1][self.y_y +
                                                  1] == " " and A[self.x_x -
                                                                  1][self.y_y +
                                                                     2] == " ":
                    for i_i in range(3):
                        A[self.x_x + 2][self.y_y + i_i] = " "
                    self.x_x = self.x_x - 1
                    XCOR[0] = self.x_x
                    YCOR[0] = self.y_y
                    RIGHTC = RIGHTC - 1
                    # timeout(getch)
                    image()
                    printing()
            fall()
        if key == "e" and self.x_x > 6 and self.y_y < 79:
            for i in range(9):
                if i % 2 == 0:
                    sleep(0.03)
                if A[self.x_x -
                     1][self.y_y] == " " and A[self.x_x -
                                               1][self.y_y +
                                                  1] == " " and A[self.x_x -
                                                                  1][self.y_y +
                                                                     2] == " ":
                    if A[self.x_x - 1][self.y_y +
                                       3] == " " and A[self.x_x][self.y_y + 3] == " ":
                        if A[self.x_x +
                             1][self.y_y +
                                3] == " " and A[self.x_x +
                                                2][self.y_y +
                                                   3] == " ":
                            for i_i in range(3):
                                A[self.x_x + i_i][self.y_y] = " "
                                A[self.x_x + 2][self.y_y + i_i] = " "
                            self.x_x = self.x_x - 1
                            self.y_y = self.y_y + 1
                            XCOR[0] = self.x_x
                            YCOR[0] = self.y_y
                            RIGHTC = RIGHTC + 1
                            image()
                            printing()
            k_2 = 1
            while True:
                if A[self.x_x +
                     3][self.y_y] == " " and A[self.x_x +
                                               3][self.y_y +
                                                  1] == " " and A[self.x_x +
                                                                  3][self.y_y +
                                                                     2] == " ":
                    if A[self.x_x +
                         3][self.y_y +
                            3] == " " and A[self.x_x +
                                            2][self.y_y +
                                               3] == " ":
                        if A[self.x_x + 1][self.y_y +
                                           3] == " " and A[self.x_x][self.y_y + 3] == " ":
                            if k_2 % 2 == 0:
                                sleep(0.03)
                            k_2 = k_2 + 1
                            for i in range(3):
                                A[self.x_x][self.y_y + i] = " "
                                A[self.x_x + i][self.y_y] = " "
                            self.x_x = self.x_x + 1
                            self.y_y = self.y_y + 1
                            XCOR[0] = self.x_x
                            YCOR[0] = self.y_y
                            RIGHTC = RIGHTC + 1
                            image()
                            printing()
                            if self.x_x >= 38:
                                fall()
                else:
                    break
            fall()


def fall():
    '''falling'''
    while True:
        if XCOR[0] >= 38:
            for i in range(XCOR[0], XCOR[0] + 3, 1):
                for j in range(YCOR[0], YCOR[0] + 3, 1):
                    A[i][j] = " "

            LIFE[0] = LIFE[0] - 1
            XCOR[0] = XCOR[0] - 30
            YCOR[0] = YCOR[0] - 5
            image()
            printing()
        elif A[XCOR[0] + 3][YCOR[0]] == "M" or A[XCOR[0] + 3][YCOR[0] + 1] == "M" or A[XCOR[0] + 3][YCOR[0] + 2] == "M":
            l_1 = len(ENEMY1POSITION)
            for i in range(l_1):
                if ENEMY1POSITION[i] == YCOR[0] or ENEMY1POSITION[i] == YCOR[0] + \
                        1 or ENEMY1POSITION[i] == YCOR[0] + 2:
                    A[38][ENEMY1POSITION[i]] = " "
                    A[37][ENEMY1POSITION[i]] = " "
                    ENEMY1POSITION[i] = -2
                    POINTS[0] = POINTS[0] + 25
            l_2 = len(ENEMY2POSITION)
            for i in range(l_2):
                if ENEMY2POSITION[i] == YCOR[0] - 1 or ENEMY2POSITION[i] == YCOR[0] or ENEMY2POSITION[i] == YCOR[0] + \
                        1 or ENEMY2POSITION[i] == YCOR[0] + 2:
                    A[38][ENEMY2POSITION[i]] = " "
                    A[37][ENEMY2POSITION[i]] = " "
                    A[38][ENEMY2POSITION[i] + 1] = " "
                    A[37][ENEMY2POSITION[i] + 1] = " "
                    ENEMY1POSITION.append(YCOR[0] - 3)
                    POINTS[0] = POINTS[0] + 50
                    ENEMY2POSITION[i] = -2

        elif A[XCOR[0] + 3][YCOR[0]] == "@" or A[XCOR[0] + 3][YCOR[0] + 1] == "@" or A[XCOR[0] + 3][YCOR[0] + 2] == "@":
            for i in range(len(LIFEPOSITION)):
                if LIFEPOSITION[i] == YCOR[0] or LIFEPOSITION[i] == YCOR[0] + \
                        1 or LIFEPOSITION[i] == YCOR[0] + 2:
                    A[XCOR[0] + 3][LIFEPOSITION[i]] = " "
                    LIFE[0] = LIFE[0] + 1
                    LIFEPOSITION[i] = -2

        elif A[XCOR[0] + 3][YCOR[0]] == "$" or A[XCOR[0] + 3][YCOR[0] + 1] == "$" or A[XCOR[0] + 3][YCOR[0] + 2] == "$":
            for i in range(len(COINPOSITION)):
                if COINPOSITION[i] == YCOR[0] or COINPOSITION[i] == YCOR[0] + \
                        1 or COINPOSITION[i] == YCOR[0] + 2:
                    A[XCOR[0] + 3][COINPOSITION[i]] = " "
                    POINTS[0] = POINTS[0] + 10
                    COINPOSITION[i] = -2

        elif A[XCOR[0] + 3][YCOR[0]] == " " and A[XCOR[0] + 3][YCOR[0] + 1] == " ":
            if A[XCOR[0] + 3][YCOR[0] + 2] == " ":
                sleep(0.02)
                for i in range(3):
                    A[XCOR[0]][YCOR[0] + i] = " "
                XCOR[0] = XCOR[0] + 1
                image()
                printing()
        else:
            break


def image():
    '''image'''
    for i_i in range(XCOR[0], XCOR[0] + 3, 1):
        for j_j in range(YCOR[0], YCOR[0] + 3, 1):
            A[i_i][j_j] = " "
    A[XCOR[0]][YCOR[0] + 1] = "O"
    for k in range(3):
        A[XCOR[0] + 1][YCOR[0] + k] = "H"
    A[XCOR[0] + 2][YCOR[0]] = "I"
    A[XCOR[0] + 2][YCOR[0] + 2] = "I"


def printing():
    '''printing'''
    os.system("clear")
    for i_i in range(43):
        for j_j in range(150):
            print(A[i_i][j_j], end='')
        print()
