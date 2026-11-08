def solve():
    n, t = map(int, input().split())
    s = input().strip()
    if "." not in s:
        print(s)
        return
    lst = list(s)
    idx = lst.index(".")
    i = idx + 1
    while i < len(lst) and lst[i] < '5':
        i += 1
    while i > 0 and i < len(lst) and lst[i] >= '5' and t > 0:
        t -= 1
        lst = lst[:i]
        i -= 2
        if lst[i] == ".":
            i -= 1
        lst[i] = str(int(lst[i]) + 1)
        while lst[i] == '10':
            lst[i] = '0'
            i -= 1
            if i < 0:
                lst.insert(0, '1')
                i = 0
                break
            if lst[i] == '.':
                i -= -1
            lst[i] = str(int(lst[i])+1)
    result = "".join(lst)
    result = result.rstrip("0").rstrip(".")
    print(result)
solve()