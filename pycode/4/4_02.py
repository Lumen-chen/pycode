n, x = map(int, input().split())
data = list(range(1, n + 1))
cnt = 0
data1 = [int(ch) for num in data for ch in str(num)]
for i in data1:
    if i == x:
        cnt += 1
print(cnt)

"""
a="".join([str[i]] for i in range(1, n + 1)])
sum = a.count(str(x)) 
用字符串计数
"""
