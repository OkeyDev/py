import sys

sys.setrecursionlimit(10)

def f(n: int):
    if n == 1:
        return 0
    return n * f(n * 2 - 9)

for i in range(-100, 101):
    if i == 1:
        continue
    try:
        f(i)
        print(i)
    except RecursionError:
        pass

# 5 7 8