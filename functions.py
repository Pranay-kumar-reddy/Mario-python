'''functions'''
import sys
from colorama import Fore, Back, Style
from objects import Bricks, Clouds, Pipes
from config import A, XCOR, YCOR, POSITION, ENEMY1POSITION, FLAGPOSITION, LIFEH, COINH
from config import ENEMY2POSITION, PIPEPOSITION, LIFE, HOLEPOSITION, BRIDGEPOSITION, CLOUDPOSITION
from config import COINPOSITION, BRICKSH, BRICKSL, CLOUDSH, CLOUDSL, LIFEPOSITION
# from enemy import *
from player import image, Man


def getch():
    '''getch'''
    import sys
    import tty
    import termios
    fd_f = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd_f)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd_f, termios.TCSADRAIN, old_settings)
    return ch


def timeout(func, args=(), kwargs={}, timeout_duration=1.5, default=None):
    import signal

    class TimeoutError(Exception):
        '''toe'''
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
        global YCOR
        player = Man()
        s_s = Bricks()
        c_c = Clouds()
        p_p = Pipes()
        if result == "q":
            sys.exit()
        if result == "w":
            player.moving("w")
        if result == "e":
            player.moving("e")
        if result == "z":
            player.moving("z")
        if result == "a":
            player.moving("a")
        if result == "d":
            if YCOR[0] > 76:
                screenleft()
                s_s.newbrick()
                c_c.newcloud()
                p_p.newpipe()
            player.moving("d")
        image()

    except TimeoutError as exc:
        image()
    finally:
        signal.alarm(0)


def screenleft():
    '''screenleft'''
    global XCOR
    global YCOR
    if A[XCOR[0]][YCOR[0] + 3] == " ":
        l_l = len(POSITION)
        POSITION[:] = [x - 1 for x in POSITION]
        for i in range(l_l):
            if POSITION[i] + BRICKSL[i] + \
                    1 > 0 and POSITION[i] + BRICKSL[i] + 1 < 149:
                A[BRICKSH[i]][POSITION[i] + BRICKSL[i] + 1] = " "
                A[BRICKSH[i] + 1][POSITION[i] + BRICKSL[i] + 1] = " "
        for i in range(l_l):
            if POSITION[i] > 0 and POSITION[i] < 143:
                A[BRICKSH[i]][POSITION[i]] = Style.BRIGHT + Back.YELLOW + \
                    Fore.YELLOW + "#" + Fore.RESET + Back.RESET
                A[BRICKSH[i] + 1][POSITION[i]] = Style.BRIGHT + \
                    Back.YELLOW + Fore.YELLOW + "#" + Fore.RESET + Back.RESET
        lc_l = len(CLOUDPOSITION)
        CLOUDPOSITION[:] = [x - 1 for x in CLOUDPOSITION]
        for i in range(lc_l):
            if CLOUDPOSITION[i] + CLOUDSL[i] + \
                    1 > 0 and CLOUDPOSITION[i] + CLOUDSL[i] + 1 < 149:
                A[CLOUDSH[i]][CLOUDPOSITION[i] + CLOUDSL[i] + 1] = " "
                A[CLOUDSH[i] + 2][CLOUDPOSITION[i] + CLOUDSL[i] + 1] = " "
                A[CLOUDSH[i] + 1][CLOUDPOSITION[i] + CLOUDSL[i] + 2] = " "
        for i in range(lc_l):
            if CLOUDPOSITION[i] > 0 and CLOUDPOSITION[i] < 143:
                A[CLOUDSH[i]][CLOUDPOSITION[i] + 1] = Fore.BLUE + "/" + Fore.RESET
                A[CLOUDSH[i] + 1][CLOUDPOSITION[i]] = Fore.BLUE + "/" + Fore.RESET
                A[CLOUDSH[i] + 2][CLOUDPOSITION[i] +
                                  1] = Fore.BLUE + "/" + Fore.RESET

        lp_l = len(PIPEPOSITION)
        PIPEPOSITION[:] = [x - 1 for x in PIPEPOSITION]
        for i in range(lp_l):
            if PIPEPOSITION[i] + 5 > 0 and PIPEPOSITION[i] + 5 < 149:
                for j in range(33, 39, 1):
                    A[j][PIPEPOSITION[i] + 5] = " "
        for i in range(lp_l):
            if PIPEPOSITION[i] > 0 and PIPEPOSITION[i] < 143:
                for j in range(33, 39, 1):
                    A[j][PIPEPOSITION[i]] = Style.BRIGHT + Back.RED + \
                        Fore.RED + "#" + Fore.RESET + Back.RESET

        ll_l = len(LIFEPOSITION)
        LIFEPOSITION[:] = [x - 1 for x in LIFEPOSITION]
        for i in range(ll_l):
            if LIFEPOSITION[i] > 0 and LIFEPOSITION[i] + 1 < 149:
                A[LIFEH[i]][LIFEPOSITION[i] + 1] = " "
        for i in range(ll_l):
            if LIFEPOSITION[i] > 0 and LIFEPOSITION[i] < 149:
                A[LIFEH[i]][LIFEPOSITION[i]] = "@"

        le1_l = len(ENEMY1POSITION)
        ENEMY1POSITION[:] = [x - 1 for x in ENEMY1POSITION]
        for i in range(le1_l):
            if ENEMY1POSITION[i] > 0 and ENEMY1POSITION[i] + 1 < 149:
                for j in range(37, 39, 1):
                    A[j][ENEMY1POSITION[i] + 1] = " "
        for i in range(le1_l):
            if ENEMY1POSITION[i] > 0 and ENEMY1POSITION[i] < 146:
                for j in range(37, 39, 1):
                    A[j][ENEMY1POSITION[i]] = "M"

        le2_l = len(ENEMY2POSITION)
        ENEMY2POSITION[:] = [x - 1 for x in ENEMY2POSITION]
        for i in range(le2_l):
            if ENEMY2POSITION[i] + 2 > 0 and ENEMY2POSITION[i] + 2 < 149:
                for j in range(37, 39, 1):
                    A[j][ENEMY2POSITION[i] + 2] = " "
        for i in range(le2_l):
            if ENEMY2POSITION[i] > 0 and ENEMY2POSITION[i] < 146:
                for j in range(37, 39, 1):
                    A[j][ENEMY2POSITION[i]] = "M"
                if A[38][ENEMY2POSITION[i] - 1] == "I":
                    LIFE[0] -= 1
        lh_l = len(HOLEPOSITION)
        HOLEPOSITION[:] = [x - 1 for x in HOLEPOSITION]
        for i in range(lh_l):
            if HOLEPOSITION[i] > 0 and HOLEPOSITION[i] + 20 < 149:
                for j in range(39, 43, 1):
                    A[j][HOLEPOSITION[i] + 20] = Style.BRIGHT + Back.CYAN + \
                        Fore.CYAN + "x" + Fore.RESET + Back.RESET
        for i in range(lh_l):
            if HOLEPOSITION[i] > 0 and HOLEPOSITION[i] < 148:
                for j in range(39, 43, 1):
                    A[j][HOLEPOSITION[i]] = " "

        lbr_l = len(BRIDGEPOSITION)
        BRIDGEPOSITION[:] = [x - 1 for x in BRIDGEPOSITION]
        for i in range(lbr_l):
            if BRIDGEPOSITION[i] + 5 > 0 and BRIDGEPOSITION[i] + 13 < 149:
                A[33][BRIDGEPOSITION[i] + 13] = " "
                A[34][BRIDGEPOSITION[i] + 13] = " "
                A[35][BRIDGEPOSITION[i] + 13] = " "
        for i in range(lbr_l):
            if BRIDGEPOSITION[i] > 0 and BRIDGEPOSITION[i] < 148:
                A[33][BRIDGEPOSITION[i]] = Style.BRIGHT + Back.BLUE + \
                    Fore.BLUE + "x" + Fore.RESET + Back.RESET
                A[34][BRIDGEPOSITION[i]] = Style.BRIGHT + \
                    Fore.BLACK + "-" + Fore.RESET
                A[35][BRIDGEPOSITION[i]] = Style.BRIGHT + \
                    Fore.YELLOW + "|" + Fore.RESET

        lco_l = len(COINPOSITION)
        COINPOSITION[:] = [x - 1 for x in COINPOSITION]
        for i in range(lco_l):
            if COINPOSITION[i] > 0 and COINPOSITION[i] + 1 < 149:
                A[COINH[i]][COINPOSITION[i] + 1] = " "
        for i in range(lco_l):
            if COINPOSITION[i] > 0 and COINPOSITION[i] < 148:
                A[COINH[i]][COINPOSITION[i]] = "$"

        lf_l = len(FLAGPOSITION)
        FLAGPOSITION[:] = [x - 1 for x in FLAGPOSITION]
        for i in range(lf_l):
            if FLAGPOSITION[i] > 0 and FLAGPOSITION[i] + 2 < 149:
                for j in range(26, 39, 1):
                    A[j][FLAGPOSITION[i] + 2] = " "
        for i in range(lf_l):
            if FLAGPOSITION[i] > 0 and FLAGPOSITION[i] < 148:
                for j in range(26, 39, 1):
                    A[j][FLAGPOSITION[i]] = "|"
                    A[j][FLAGPOSITION[i] + 1] = "|"
