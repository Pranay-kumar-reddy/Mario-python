'''making Board'''
from config import A


class Board:
    '''Board'''

    def __init__(self, l_b=149, h_b=39):
        '''init'''
        self.l_b = l_b
        self.h_b = h_b
        for i in range(1, self.h_b, 1):
            for j in range(1, self.l_b, 1):
                A[i][j] = " "

    def print(self):
        '''print'''
        self.q_q = 0
        for i in range(43):
            for j in range(150):
                print(A[i][j], end=' ')
            print()
        self.q_q = 1    
