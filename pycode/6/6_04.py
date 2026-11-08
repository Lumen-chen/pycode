from functools import cmp_to_key
n = int(input())
data = input().split()
def compare(x, y):                  # 自定义排序规则
    if x + y > y + x:
        return -1                   # 负数第一个参数x排前面
    elif x + y < y + x:
        return 1
    else:
        return 0
data.sort(key=cmp_to_key(compare))
s = "".join(data)
if s[0] == '0':
    print('0')
else:
    print(s)