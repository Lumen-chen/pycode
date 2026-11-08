import sys
def day(year,month):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    else:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 29
        else:
            return 28    
def solve():
    for line in sys.stdin:
        line = line.strip()
        if not line:           # 空行跳过
            continue
        y, m, x = map(int, line.split())
        cnt = 0
        for d in range(1,day(y, m)+1):
            s = f"{y:04d}, {m:02d}, {d:02d}"
            cnt += s.count(str(x))
        print(cnt)
solve()