n, K = map(int, input().split())
dataA = list(map(int, input().split()))
dataB = list(map(int, input().split()))
base = sum(dataB)                       # 假设全在晚上，设置基础值
diff = sorted([dataA[i] - dataB[i] for i in range(n)], reverse=True) # 补差，挑最多的
print(base + sum(diff[0:K]))
