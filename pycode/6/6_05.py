
s = input()
lst = []
def solve():
    for ch in s:
        lst.append(ch)
        if len(lst) >= 2 and lst[-1] == 'b' and lst[-2] == 'a':
            lst.pop()
            lst.pop()
    if len(lst) == 0:
        print("Good")
    else:
        print("Bad")
solve()




