for i in range(1,7):
    if i < 3:
        print(" " * 5 + "*" * 2,end="") 
    elif 3<=i<=4:
        print("*"*12,end="")
    else:
        print(" " * 4 + "*  *",end="")
    print()