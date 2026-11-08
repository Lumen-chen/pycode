# set去重
L, M = map(int, input().split())
removed = set()               
for i in range(1, M + 1):
    l, r = map(int, input().split())
    removed.update(range(l, r + 1))
trees = L + 1 - len(removed)
print(trees)

"""
布尔数组标记：砍False，没砍
读取
初始化：trees = [True] * (L + 1)
遍历：砍掉的标记为False
sum(trees)
"""