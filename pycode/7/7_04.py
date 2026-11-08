def solve():
    T = int(input())
    for _ in range(T):
        s = input().strip()
        res = []
        i = 0
        while i < len(s):
            if s[i] in '02469':
                res.append(s[i])
                i += 1
            elif s[i:i+3] == 'two':
                    res.append('2')
                    i += 3
            elif s[i:i+3] == 'six':
                    res.append('6')
                    i += 3
            elif s[i:i+4] == 'zero':
                    res.append('0')
                    i += 4
            elif s[i:i+4] == 'four':
                    res.append('4')
                    i += 4
            elif s[i:i+4] == 'nine':
                    res.append('9')
                    i += 4
            else:
                    i += 1
        print("".join(res))
solve()