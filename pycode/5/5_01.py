L, R = map(int,input().split())
s = "".join([str(i) for i in range(L, R+1)])
cnt = s.count(str(2))
print(cnt)

