import sys 
sys.setrecursionlimit(10000) 

counter = 0 
def f(n: int): 
    global counter 
    counter += 1 
    if n == 1 : 
        return 1 
    return n * f(n - 1) 

f(2024) 
print(counter) # 2024 