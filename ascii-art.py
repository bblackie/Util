import os
import math
import time

A = 0
B = 0
while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    z = [0] * 1760
    b = [' '] * 1760
    for j in range(0, 628, 7):
        for i in range(0, 628, 2):
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(A)
            f = math.sin(j)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
            x = int(40 + 30 * D * (l * h * m - t * n))
            y = int(12 + 15 * D * (l * h * n + t * m))
            o = int(x + 80 * y)
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
            if 1760 > o > 0 and D > z[o]:
                z[o] = D
                b[o] = ".,-~:;=!*#$@"[N if N > 0 else 0]

    print('\x1b[H', end='')
    for k in range(1760):
        print(b[k], end=(' ' if k % 80 else ''))
    A += 0.04
    B += 0.03
    time.sleep(0.03)
