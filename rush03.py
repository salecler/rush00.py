from ast import arg
from mailbox import linesep
from re import L, X
import sys

if (len(sys.argv) == 3):
    x = int(sys.argv[1]) # Lines
    y = int(sys.argv[2]) # Columns
    c = 1
    while (c <= y) and (x > 0) and (y > 0):
        l = 1
        while l <= x:
            if (l == 1 and c == 1) or (l == 1 and c == y) or (l == x and c == 1) or (l == x and c == y):
                print('o', end="")
            elif (c > 1 and c < y) and (l == 1 or l == x):
                print('|', end="")
            elif (l > 1 and l < x) and (c == 1 or c == y):
                print('-', end="")
            else:
                print(' ', end="")
            l = l + 1
        print("")
        c = c + 1