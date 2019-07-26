'''main file'''
import os
from player import Man
import board
from board import Board
from enemy import Enemy2, Enemy1
from config import A, ENEMY1POSITION, ENEMY2POSITION, XCOR, YCOR, LIFE, POINTS
from functions import screenleft, timeout, getch
# from player import *

BOR = board.Board()
PLAYER = Man()
for i in range(20):
    screenleft()

while True:
    timeout(getch)
    P = Enemy1(1, ENEMY1POSITION)
    B = Enemy2(1.5, ENEMY2POSITION)
    os.system("clear")
    for i in range(43):
        for j in range(150):
            print(A[i][j], end='')
        print()

    print("lives=", LIFE[0], "              POINTS=", POINTS[0])
    if A[XCOR[0] + 2][YCOR[0] + 3] == "|":
        print("----------CONGRAGULATIONS!!!YOU HAVE COMPLETED THE GAME-----------")
        break
    if LIFE[0] == 0:
        print("GAMEOVER")
        break

    # print(ENEMY1POSITION)
    # print(ENEMY2POSITION)
    # print(PIPEPOSITION)
    # print(HOLEPOSITION)
    # print(XCOR)
    # print(YCOR)
    # print(COINPOSITION)
