n = int(input())
if 1 <= n <= 10 ** 5:
    if n % 2 != 0:
        fn = 3 * n + 1
    else:
        fn = n // 2
    print(fn)
else:
    print("error")