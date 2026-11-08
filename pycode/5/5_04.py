x, y = map(int, input().split())
def five(a, b):
    if a > b:
        a, b = b, a
    cnt = 0
    for i in range(a + 1, b):
        s = sum(int(j) for j in str(i))
        if s % 5 == 0:
            cnt += 1
    print(cnt)
five(x, y)
