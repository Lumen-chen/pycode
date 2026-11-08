import sys
data = list(map(int,sys.stdin.read().split()))
T = data[0]
for j in range(1,T+1):
    n = data[j]
    for i in range(1, n // 2 + 2):
        print(" " * (n // 2 + 1 - i) + "*" * (2 *i - 1))
    for i in range(n // 2 ,0, -1):
        print(" " * (n // 2 + 1 - i) + "*" * (2 * i - 1))