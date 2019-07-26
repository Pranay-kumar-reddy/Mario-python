'''config'''
from colorama import Fore, Back, Style
A = [[Style.BRIGHT + Back.CYAN + Fore.CYAN + "x" + Fore.RESET +
      Back.RESET for i in range(150)] for j in range(43)]
XCOR = [36, ]
YCOR = [1, ]
BRICKSH = [32, 27, 27, 22, 27, 32, 27, 22, 17, 17, 22,
           17, 22, 27, 27, 22, 22, 27, 32, 27, 22, 22, 17]
BRICKSL = [5, 7, 6, 5, 7, 5, 7, 6, 6, 5, 7,
           6, 5, 7, 6, 5, 7, 6, 5, 6, 7, 5, 6, 7, 5]
LIFEH = [21, 16, 21]
CLOUDSH = [1, 5, 5, 1, 5, 1, 5, 5, 1, 1, 1, 5, 1, 5, 1, 5, 1, 5, 1]
CLOUDSL = [3, 4, 5, 3, 3, 4, 5, 5, 4, 3, 4, 5, 3, 4, 5, 3, 4, 3, 3]
COINH = [
    26,
    26,
    26,
    21,
    21,
    21,
    16,
    16,
    16,
    16,
    16,
    16,
    26,
    26,
    26,
    21,
    21,
    21,
    26,
    26,
    26]
POSITION = []
CLOUDPOSITION = []
for i in range(1, 24, 1):
    POSITION.append(15 * i)
for i in range(1, 18, 1):
    CLOUDPOSITION.append(20 * i)
PIPEPOSITION = [135, 180, 240, 315]
LIFEPOSITION = [63, 153, 243]
HOLEPOSITION = [80, 155, 260, 345]
ENEMY1POSITION = [40, 120, 220, 305]
ENEMY2POSITION = [60, 155, 200, 295]
BRIDGEPOSITION = [158]
COINPOSITION = [46, 48, 50, 61, 63, 65, 136, 138, 140, 181,
                183, 185, 226, 228, 230, 256, 258, 260, 271, 273, 275]
RIGHTC = 0
m = 0
ELIST1 = []
ELIST2 = []
TIME1 = 0
TIME2 = 0
POINTS = [0, ]
E1 = 0
E2 = 0
LIFE = [3, ]
FLAGPOSITION = [390, ]
