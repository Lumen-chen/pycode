n = int(input())
if 1 <= n <= 1000:
    num = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            num += 1
            print(f"{num:<4d}", end=" ")
        print()
else:
    print("error")

