import sys
data = list(map(int,sys.stdin.read().split()))
for n in data:
    for i in range(1, n + 2):
        print(" " * (2 * (n - i) + 2) + "*" * i)
    for i in range(n, 0,-1):
        print(" " * (2 * (n - i) + 2) + "*" * i)