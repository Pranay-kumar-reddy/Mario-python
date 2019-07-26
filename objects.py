'''objects'''
from colorama import Fore, Back, Style
from config import A, POSITION, BRICKSH, BRICKSL, CLOUDSH, CLOUDSL, CLOUDPOSITION, PIPEPOSITION


class Bricks:
    '''bricks'''
    def __init__(self):
        '''init'''
        pass

    def newbrick(self):
        '''newbrick'''
        for k_k in range(23):
            if POSITION[k_k] == 143:
                for i in range(BRICKSH[k_k], BRICKSH[k_k] + 2, 1):
                    for j in range(POSITION[k_k], POSITION[k_k] + BRICKSL[k_k], 1):
                        A[i][j] = Style.BRIGHT + Back.YELLOW + \
                            Fore.YELLOW + "#" + Fore.RESET + Back.RESET


class Clouds:
    '''clouds'''
    def __init__(self):
        '''init'''
        pass

    def newcloud(self):
        '''new cloud'''
        for l_l in range(17):
            if CLOUDPOSITION[l_l] == 143:
                for i in range(CLOUDSH[l_l], CLOUDSH[l_l] + 3, 1):
                    for j in range(
                            CLOUDPOSITION[l_l],
                            CLOUDPOSITION[l_l] +
                            CLOUDSL[l_l] -
                            1,
                            1):
                        A[i][j] = Fore.BLUE + "/" + Fore.RESET
                A[CLOUDSH[l_l] + 1][CLOUDPOSITION[l_l]] = Fore.BLUE + "/" + Fore.RESET
                A[CLOUDSH[l_l] + 1][CLOUDPOSITION[l_l] + \
                    CLOUDSL[l_l] - 1] = Fore.BLUE + "/" + Fore.RESET


class Pipes:
    '''pipes'''
    def __init__(self):
        '''init'''
        pass

    def newpipe(self):
        '''newpipe'''
        for p_p in range(4):
            if PIPEPOSITION[p_p] == 143:
                for i in range(33, 39, 1):
                    for j in range(PIPEPOSITION[p_p], PIPEPOSITION[p_p] + 4, 1):
                        A[i][j] = Style.BRIGHT + Back.RED + \
                            Fore.RED + "#" + Fore.RESET + Back.RESET
