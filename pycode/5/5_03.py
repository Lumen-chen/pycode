import math
def is_prime(x):
    is_prime = 1
    if x < 2:
        is_prime = 0
    elif x == 2:
        is_prime = 1
    elif x % 2 == 0:
        is_prime = 0
    else:
        for i in range(3,int(math.sqrt(x)),2):
            if x % i == 0:
                is_prime = 0
    return is_prime
    
def hw(t):
    s = str(t)
    s1 = s + s[-2::-1] 
    return int(s1)
def solve():
    t = int(input())
    t1 = hw(t)
    if is_prime(t1):
        print("prime")
    else:
        print("noprime")
solve()
    
