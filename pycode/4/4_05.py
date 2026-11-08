n = int(input())
data = list(map(int, input().split()))
last1 = data[-1]
if last1 == 15:
    print("DOWN")
elif last1 == 0:
    print("UP")
elif n == 1:
    print("-1")
elif last1 > data[-2]:
    print("UP")
else:
    print("DOWN")