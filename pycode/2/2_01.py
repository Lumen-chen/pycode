a, b = map(int, input().split())
if a >= 1 and b <= 10 ** 4:
    if a < b:
        print("<")
    elif a > b:
        print(">")
    else:
        print("=")
else:
    print("error")
