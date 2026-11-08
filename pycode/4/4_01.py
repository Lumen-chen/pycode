T = int(input())
for i in range(1, T + 1): 
    n = int(input())
    lst = list(map(int, input().split()))
    sum1 = sum(lst)
    ptp1 = max(lst) - min(lst)
    mean1 = sum1 / n
    sum2 = 0
    for j in lst:
        sum2 += ((j -mean1) ** 2) 
    var1 = sum2 / n
    print(f"{ptp1} {var1:.3f}")
