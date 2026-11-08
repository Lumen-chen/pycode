for i in range(1,10):
    for j in range(1,i+1):
        num = i * j
        if num < 10:
            print(f"{j}*{i}= {i*j}",end=" ")
        else:
            print(f"{j}*{i}={i*j}",end=" ")
    print()