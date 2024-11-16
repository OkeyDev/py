import sys

sys.setrecursionlimit(10000)

def f(n: int):  
    if n == 1:  
        return 1  
    return n * f(n - 1)  
    
print((f(2000) - f(1999)) // f(1998)) # 3996001