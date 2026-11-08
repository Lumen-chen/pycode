import sys
rules2 = {
    '13': '2', '31': '2','46': '5', '64': '5',
    '79': '8', '97': '8','17': '4', '71': '4',
    '28': '5', '82': '5','39': '6', '93': '6',
    '19': '5', '91': '5','37': '5', '73': '5'
}
def solve():
    data = sys.stdin.read().split()
    for s in data:
        if len(set(s)) != len(s):       #rules1,去重
            print("NO")
            continue
        else:
            visted = set()
            visted.add(s[0])
            is_valid = True
            for i in range(1,len(s)):
                s1 = s[i-1] + s[i]
                if s1 in rules2:
                    if rules2[s1] not in visted:
                        is_valid = False
                        break
                visted.add(s[i])
            if is_valid:
                print("YES")
            else:
                print("NO")
solve()