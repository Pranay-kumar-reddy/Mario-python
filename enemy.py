'''Enemy.py'''
from time import time
from config import XCOR, YCOR, TIME1, E1, E2, A, TIME2, LIFE
from player import fall


class Enemy:
    '''enemy'''

    def __init__(self, speed, elist):
        '''init'''
        self.speed = speed
        self.elist = elist
        # self.lefttime=lefttime

    def eleft(self):
        '''eleft'''
        l_l = len(self.elist)
        for i in range(l_l):
            if self.elist[i] > 1 and self.elist[i] < 148 and A[38][self.elist[i] - 1] != "#":
                if A[38][self.elist[i] - 1] == "I":
                    LIFE[0] -= 1
                    if YCOR[0] > 0:
                        for k in range(XCOR[0], XCOR[0] + 3, 1):
                            for j in range(YCOR[0], YCOR[0] + 3, 1):
                                A[k][j] = " "
                        YCOR[0] = YCOR[0] - 2
                        XCOR[0] = XCOR[0] - 30
                        fall()
                self.elist[i] = self.elist[i] - 1

    def eright(self):
        '''eright'''
        l_l = len(self.elist)
        for i in range(l_l):
            if self.elist[i] > 1 and self.elist[i] < 148 and A[38][self.elist[i] - 1] != "#":
                if A[38][self.elist[i] + 2] == "I":
                    LIFE[0] -= 1
                    if YCOR[0] > 0:
                        for k in range(XCOR[0], XCOR[0] + 3, 1):
                            for j in range(YCOR[0], YCOR[0] + 3, 1):
                                A[k][j] = " "
                        YCOR[0] = YCOR[0] - 2
                        XCOR[0] = XCOR[0] - 30
                        fall()
                self.elist[i] = self.elist[i] + 1

    def newenemy(self):
        '''newenemy'''
        self.elist.append(72)


class Enemy1(Enemy):
    '''enemy1'''

    def __init__(self, speed, elist):
        super().__init__(speed, elist)
        global TIME1
        global A
        global E1
        if time() - TIME1 > self.speed:
            TIME1 = time()
            E1 = E1 + 1
            if E1 % 16 > 8:
                Enemy.eleft(self)
                l_l = len(self.elist)
                for i in range(l_l):
                    if self.elist[i] > -1 and self.elist[i] + 1 < 149:
                        if A[37][self.elist[i]] != "#":
                            if A[38][self.elist[i]] != "#":
                                A[37][self.elist[i] + 1] = " "
                                A[38][self.elist[i] + 1] = " "
                                if self.elist[i] > 0:
                                    A[37][self.elist[i]] = "M"
                                    A[38][self.elist[i]] = "M"
            if E1 % 16 < 8:
                Enemy.eright(self)
                l_l = len(self.elist)
                for i in range(l_l):
                    if self.elist[i] - 1 > 0 and self.elist[i] < 149:
                        if A[37][self.elist[i]] != "#":
                            if A[38][self.elist[i]] != "#":
                                A[37][self.elist[i] - 1] = " "
                                A[38][self.elist[i] - 1] = " "
                                if self.elist[i] > 0:
                                    A[37][self.elist[i]] = "M"
                                    A[38][self.elist[i]] = "M"


class Enemy2(Enemy):
    '''ememy2'''

    def __init__(self, speed, elist):
        super().__init__(speed, elist)
        global TIME2
        global A
        global E2
        if time() - TIME2 > self.speed:
            TIME2 = time()
            E2 = E2 + 1
            if E2 % 16 < 8:
                Enemy.eleft(self)
                l_l = len(self.elist)

                for i in range(l_l):
                    if self.elist[i] > -1 and self.elist[i] + 2 < 149:
                        if A[37][self.elist[i]] != "#":
                            if A[38][self.elist[i]] != "#":
                                A[37][self.elist[i] + 2] = " "
                                A[38][self.elist[i] + 2] = " "
                                if elist[i] > 0:
                                    A[37][self.elist[i]] = "M"
                                    A[38][self.elist[i]] = "M"
                                    A[37][self.elist[i] + 1] = "M"
                                    A[38][self.elist[i] + 1] = "M"

            if E2 % 16 > 8:
                l_l = len(self.elist)
                Enemy.eright(self)
                for i in range(l_l):
                    if self.elist[i] - 1 > 0 and self.elist[i] < 149:
                        if A[37][self.elist[i]] != "#":
                            if A[38][self.elist[i]] != "#":
                                A[37][self.elist[i] - 1] = " "
                                A[38][self.elist[i] - 1] = " "
                                if elist[i] > 0:
                                    A[37][self.elist[i]] = "M"
                                    A[38][self.elist[i]] = "M"
                                    A[37][self.elist[i] + 1] = "M"
                                    A[38][self.elist[i] + 1] = "M"
