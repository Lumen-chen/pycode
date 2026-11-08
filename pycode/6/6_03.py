n = int(input())
data = list(map(int, input().split()))
data.sort()
def solve():
    for i in range(n - 2):
        a = data[i]
        b = data[i + 1]
        c = data[i + 2]
        if a + b > c:
            print(f"{a} {b} {c}")
            return
    print("No solution")
solve()