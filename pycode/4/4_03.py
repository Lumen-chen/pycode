n, k, m = map(int, input().split())
data = list(range(0, n))
i = k
while len(data) > 1:
    i = (i + m - 1) % len(data)
    data.pop(i)
print(data[0])


