import sys
def solve():
    data = sys.stdin.read().split()
    T = int(data[0])
    for i in range(1, T * 2 + 1, 2):
        num1 = int(data[i])
        num2 = int(data[i + 1])
        print(num1 * num2)
solve()

    