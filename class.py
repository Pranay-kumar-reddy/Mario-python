'''class'''
import os
import sys
from time import sleep, time
#import numpy
A = [["x" for i in range(75)] for j in range(40)]
XCOR = 36
YCOR = 1
BRICKSH = [32, 27, 27, 22, 27, 32, 27, 22, 17, 17, 12, 17,
           27, 27, 22, 22, 27, 32, 27, 27, 22, 17, 22, 22, 27]
BRICKSL = [5, 7, 6, 5, 7, 5, 7, 6, 6, 5, 7,
           6, 5, 7, 6, 5, 7, 6, 5, 6, 7, 5, 6, 7, 5]
CLOUDSH = [1, 5, 5, 1, 5, 1, 5, 5, 1, 1, 1,
           5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 1, 5, 1, 5]
CLOUDSL = [3, 4, 5, 3, 3, 4, 5, 5, 4, 3, 4,
           5, 3, 4, 5, 3, 4, 3, 3, 5, 5, 5, 4, 3, 5]
POSITION = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180,
            195, 210, 225, 240, 255, 270, 285, 300, 315, 330, 345, 360, 375]
CLOUDPOSITION = [
    20,
    40,
    60,
    80,
    100,
    120,
    140,
    160,
    180,
    200,
    220,
    240,
    260,
    280,
    300,
    320,
    340,
    360,
    380,
    400,
    420,
    440,
    460,
    480,
    500]
PIPEPOSITION = [135, 180, 240, 315]
RIGHTC = 0
ELIST1 = []
ELIST2 = []
LEFTTIME = 0
NEWTIME1 = 0
NEWTIME2 = 0
CHECK = 0
ECHECK = 0
k = 0


class Board:
    '''Board'''

    def __init__(self, l_l=75, h_h=40):
        '''init'''
        self.l_l = l_l
        self.h_h = h_h
        global A
        for i in range(1, 39, 1):
            for j in range(1, 74, 1):
                A[i][j] = " "
        self.A = A

    def print(self):
        '''printing'''
        for i in range(40):
            for j in range(75):
                print(A[i][j], end=' ')
            print()


BOR = Board()


def getch():
    '''get character'''
    import tty
    import termios
    fd_f = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd_f)
    try:
        tty.setraw(sys.stdin.fileno())
        ch_c = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd_f, termios.TCSADRAIN, old_settings)
    return ch_c


class Man():
    '''man'''
    def __init__(self):
        '''init'''
        # super().__init__(l,h,A)
        self.x = XCOR
        self.y = YCOR

    def moving(self, key):
        '''moving'''
        global XCOR
        global YCOR
        global RIGHTC
        if key == "a" and self.y != 1:
            if A[self.x][self.y - 1] != "#" and A[self.x + 1][self.y - 1] != "#":
                if A[self.x + 2][self.y - 1] != "#":
                    for i in range(3):
                        A[self.x + i][self.y + 2] = " "
                    self.y = self.y - 1
                    YCOR = self.y
            while True:
                if A[self.x +
                     3][self.y +
                        2] == "#" or A[self.x +
                                       3][self.y +
                                          2] == "x":
                    break
                sleep(0.03)
                for i in range(3):
                    A[self.x][self.y + i] = " "
                self.x = self.x + 1
                PLAYER.image()
                PLAYER.printing()
        if key == "d" and self.y < 60:
            if A[self.x][self.y + 3] != "#" and A[self.x + 1][self.y + 3] != "#":
                if A[self.x + 2][self.y + 3] != "#":
                    if self.y < 39:
                        for i in range(3):
                            A[self.x + i][self.y] = " "
                        self.y = self.y + 1
                        YCOR = self.y
            if A[self.x + 3][self.y] == "#" or A[self.x + 3][self.y + 2] == "#":
                for i in range(3):
                    A[self.x + i][self.y] = " "
                self.y = self.y + 1
                YCOR = self.y
            while True:
                if A[self.x + 3][self.y] == "#" or A[self.x + 3][self.y] == "x":
                    break
                sleep(0.03)
                for i in range(3):
                    A[self.x][self.y + i] = " "
                self.x = self.x + 1
                PLAYER.image()
                PLAYER.printing()
        if key == "z" and self.x > 6 and self.y > 10:
            for i in range(10):
                sleep(0.03)
                s_x = self.x
                s_y = self.y
                if A[s_x -
                     1][s_y -
                        1] != "#" and A[s_x -
                                        1][s_y +
                                           1] != "#" and A[s_x -
                                                           1][s_y +
                                                              2] != "#" and A[s_x -
                                                                              1][s_y -
                                                                                 1] != "#":
                    if A[s_x][s_y -
                              1] != "#" and A[s_x +
                                              1][s_y -
                                                 1] != "#" and A[s_x +
                                                                 2][s_y -
                                                                    1] != "#" and A[s_x +
                                                                                    3][s_y -
                                                                                       1] != "#":
                        for i_i in range(3):
                            A[self.x + i_i][self.y + 2] = " "
                            A[self.x + 2][self.y + i_i] = " "
                        self.x = self.x - 1
                        self.y = self.y - 1
                        RIGHTC = RIGHTC - 1
                        PLAYER.image()
                        PLAYER.printing()

            while True:
                if A[self.x + 3][self.y] == "#" or A[self.x + 3][self.y + \
                    2] == "#" or A[self.x + 3][self.y + 2] == "x":
                    break
                sleep(0.03)
                if A[self.x][self.y - 1] == "x":
                    PLAYER.moving("d")
                    break
                for i in range(3):
                    A[self.x][self.y + i] = " "
                    A[self.x + i][self.y + 2] = " "
                self.x = self.x + 1
                self.y = self.y - 1
                RIGHTC = RIGHTC - 1

                PLAYER.image()
                PLAYER.printing()
        if key == "w" and self.x > 6 and self.y < 40:
            for i in range(10):
                sleep(0.03)
                if A[self.x -
                     1][self.y] != "#" and A[self.x -
                                             1][self.y +
                                                1] != "#":
                    if A[self.x -
                         1][self.y +
                            2] != "#" and A[self.x -
                                            1][self.y +
                                               3] != "#":
                        if A[self.x][self.y + 3] != "#" and A[self.x +
                                                              1][self.y + 3] != "#":
                            if A[self.x +
                                 2][self.y +
                                    3] != "#" and A[self.x +
                                                    3][self.y +
                                                       3] != "#":
                                for i_i in range(3):
                                    A[self.x + i_i][self.y] = " "
                                    A[self.x + 2][self.y + i_i] = " "
                                self.x = self.x - 1
                                self.y = self.y + 1
                                RIGHTC = RIGHTC + 1
                                PLAYER.image()
                                PLAYER.printing()

            while True:
                if A[self.x + 3][self.y] == "#" or A[self.x + 3][self.y + \
                    2] == "#" or A[self.x + 3][self.y + 2] == "x":
                    break
                sleep(0.03)
                for i in range(3):
                    A[self.x][self.y + i] = " "
                    A[self.x + i][self.y] = " "
                self.x = self.x + 1
                self.y = self.y + 1
                RIGHTC = RIGHTC + 1
                PLAYER.image()
                PLAYER.printing()

    def image(self):
        '''image'''
        for i in range(self.x, self.x + 3, 1):
            for j in range(self.y, self.y + 3, 1):
                A[i][j] = " "
        A[self.x][self.y + 1] = "O"
        for k_k in range(3):
            A[self.x + 1][self.y + k_k] = "H"
        A[self.x + 2][self.y] = "I"
        A[self.x + 2][self.y + 2] = "I"

    def printing(self):
        '''printing'''
        for i in range(40):
            for j in range(75):
                print(A[i][j], end=' ')
            print()


class Bricks:
    '''Bricks'''
    def __init__(self):
        '''init'''
        pass

    def newbrick(self):
        '''newbrick'''
        for k_k in range(25):
            if POSITION[k_k] == 66:
                for i in range(BRICKSH[k_k], BRICKSH[k_k] + 2, 1):
                    for j in range(POSITION[k_k], POSITION[k_k] + BRICKSL[k_k], 1):
                        A[i][j] = "#"


class Clouds:
    '''Clouds'''

    def __init__(self):
        '''init'''
        pass

    def newcloud(self):
        '''newcloud'''
        for l_l in range(25):
            if CLOUDPOSITION[l_l] == 66:
                for i in range(CLOUDSH[l_l], CLOUDSH[l_l] + 3, 1):
                    for j in range(
                            CLOUDPOSITION[l_l],
                            CLOUDPOSITION[l_l] +
                            CLOUDSL[l_l] -
                            1,
                            1):

                        A[i][j] = "/"
                A[CLOUDSH[l_l] + 1][CLOUDPOSITION[l_l]] = "/"
                A[CLOUDSH[l_l] + 1][CLOUDPOSITION[l_l] + CLOUDSL[k] - 1] = "/"


class Pipes:
    '''Pipes'''

    def __init__(self):
        '''init'''
        pass

    def newpipe(self):
        '''newpipe'''
        for p_p in range(4):
            if PIPEPOSITION[p_p] == 66:
                for i in range(33, 39, 1):
                    for j in range(PIPEPOSITION[p_p], PIPEPOSITION[p_p] + 4, 1):
                        A[i][j] = "#"


PLAYER = Man()
S = Bricks()
C = Clouds()
P = Pipes()


class Enemy:
    '''Enemy'''
    def __init__(self, speed, elist):
        '''init'''
        self.speed = speed
        self.elist = elist
        # self.LEFTTIME=LEFTTIME

    def eleft(self):
        '''eleft'''
        global LEFTTIME
        global CHECK
        if CHECK == 0:
            if int(time() * self.speed) % 3 == 2:
                CHECK = 1
                self.elist[:] = [x - 1 for x in self.elist]
        if CHECK == 1:
            if int(time() * self.speed) % 3 == 1:
                CHECK = 0
                self.elist[:] = [x - 1 for x in self.elist]

    def newenemy(self):
        '''newenwmy'''
        self.elist.append(73)


class Enemy1(Enemy):
    '''Enemy1'''
    def __init__(self, speed, elist):
        '''init'''
        super().__init__(speed, elist)
        l_l = len(self.elist)
        for i in range(l_l):
            if self.elist[i] > -1 and self.elist[i] < 73:
                A[38][self.elist[i] + 1] = " "
            if self.elist[i] > 0:
                A[38][self.elist[i]] = "M"

    def cenemy1(self):
        '''create Enemy1'''
        global NEWTIME1
        global ECHECK
        if ECHECK == 1:
            if int(time()) % 10 == 0:
                ECHECK = 0
                Enemy.newenemy(self)


class Enemy2(Enemy):
    '''Enemy2'''

    def __init__(self, speed, elist):
        '''init'''
        super().__init__(speed, elist)
        l_l = len(elist)
        for i in range(l_l):
            if self.elist[i] > -1 and self.elist[i] < 73:
                A[37][self.elist[i] + 1] = " "
                A[38][self.elist[i] + 1] = " "
            if elist[i] > 0:
                A[37][self.elist[i]] = "M"
                A[38][self.elist[i]] = "M"

    def cenemy2(self):
        '''create Enemy2'''
        global NEWTIME2
        global ECHECK
        if ECHECK == 0:
            if int(time()) % 10 == 5:
                ECHECK = 1
                Enemy.newenemy(self)


def timeout(func, args=(), kwargs={}, timeout_duration=2, default=None):
    '''timeout'''
    import signal

    class TimeoutError(Exception):
        '''timeouterror'''
        pass

    def handler(signum, frame):
        '''handler'''
        raise TimeoutError()

    # set the timeout handler
    signal.signal(signal.SIGALRM, handler)
    # signal.alarm(timeout_duration)
    signal.setitimer(signal.ITIMER_REAL, timeout_duration)
    try:
        result = func(*args, **kwargs)
        if result == "q":
            sys.exit()
        if result == "w":
            PLAYER.moving("w")
        if result == "z":
            PLAYER.moving("z")
        if result == "a":
            PLAYER.moving("A")
        if result == "d":
            if YCOR > 38:
                screenleft()
                S.newbrick()
                C.newcloud()
                P.newpipe()
            PLAYER.moving("d")
        a_a = Enemy1(5, ELIST1)
        a_a.cenemy1()
        a_a.eleft()
        b_b = Enemy2(10, ELIST2)
        b_b.cenemy2()
        b_b.eleft()
        PLAYER.image()

    except TimeoutError as exc:
        a_a = Enemy1(5, ELIST1)
        a_a.eleft()
        b_b = Enemy2(10, ELIST2)
        b_b.eleft()

        PLAYER.image()
    finally:
        signal.alarm(0)


def screenleft():
    '''move screen'''
    if A[XCOR][YCOR + 3] != "#":
        l_p = len(POSITION)
        POSITION[:] = [x - 1 for x in POSITION]
        for i in range(l_p):
            if POSITION[i] + BRICKSL[i] + \
                    1 > 0 and POSITION[i] + BRICKSL[i] + 1 < 74:
                A[BRICKSH[i]][POSITION[i] + BRICKSL[i] + 1] = " "
                A[BRICKSH[i] + 1][POSITION[i] + BRICKSL[i] + 1] = " "
        for i in range(l_p):
            if POSITION[i] > 0 and POSITION[i] < 67:
                A[BRICKSH[i]][POSITION[i]] = "#"
                A[BRICKSH[i] + 1][POSITION[i]] = "#"
        lc_p = len(CLOUDPOSITION)
        CLOUDPOSITION[:] = [x - 1 for x in CLOUDPOSITION]
        for i in range(lc_p):
            if CLOUDPOSITION[i] + CLOUDSL[i] + \
                    1 > 0 and CLOUDPOSITION[i] + CLOUDSL[i] + 1 < 74:
                A[CLOUDSH[i]][CLOUDPOSITION[i] + CLOUDSL[i] + 1] = " "
                A[CLOUDSH[i] + 2][CLOUDPOSITION[i] + CLOUDSL[i] + 1] = " "
                A[CLOUDSH[i] + 1][CLOUDPOSITION[i] + CLOUDSL[i] + 2] = " "
        for i in range(lc_p):
            if CLOUDPOSITION[i] > 0 and CLOUDPOSITION[i] < 67:
                A[CLOUDSH[i]][CLOUDPOSITION[i] + 1] = "/"
                A[CLOUDSH[i] + 1][CLOUDPOSITION[i]] = "/"
                A[CLOUDSH[i] + 2][CLOUDPOSITION[i] + 1] = "/"

        lp_p = len(PIPEPOSITION)
        PIPEPOSITION[:] = [x - 1 for x in PIPEPOSITION]
        for i in range(lp_p):
            if PIPEPOSITION[i] + 5 > 0 and PIPEPOSITION[i] + 5 < 74:
                for j in range(33, 39, 1):
                    A[j][PIPEPOSITION[i] + 5] = " "
        for i in range(lp_p):
            if PIPEPOSITION[i] > 0 and PIPEPOSITION[i] < 67:
                for j in range(33, 39, 1):
                    A[j][PIPEPOSITION[i]] = "#"


while True:
    timeout(getch)
    os.system("clear")
    for ii in range(40):
        for jj in range(75):
            print(A[ii][jj], end=' ')
        print()
