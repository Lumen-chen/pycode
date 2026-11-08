lst = []                                        #初始化
for a in range(1,50):                           
    for b in range(a,2000):                     
        c = a * b                               
        if c > 9999:                            
            break
        s = str(a) + str(b) + str(c)            #字符串拼接，判断数字违规情况
        if '0' not in s and len(set(s)) == 9:       #式子中1~9每个数字正好出现一次
            lst.append((c, a, b))
    lst.sort(key = lambda x: (x[0],x[1]))
for c, a, b in lst:
    print(f"{c} = {a} x {b}")