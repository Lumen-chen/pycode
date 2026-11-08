import sys
lst = list(map(int,sys.stdin.read().split()))
for item in lst:
    #n = int(item)
    if 2 <= item <= 9:
        for i in range(1,item + 1):                        #上三角
            print(" " * (item - i) + "*" * (2 * i - 1))
        for i in range(item - 1, 0 , -1):                  #下三角
            print(" " * (item - i) + "*" * (2 * i - 1))
    else:
        print("error")