import math
n = int(input())

def move (n, x, y):
    def move(n, start, finish):
        if n > 0:
            temp = 6 — finish
            move(n — 1, start, temp)
            print(n, x, y)
            move(n — 1, temp, finish)
dsfjsbvj000000