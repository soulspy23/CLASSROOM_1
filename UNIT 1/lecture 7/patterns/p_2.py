for i in range(6,0,-1):
    for j in range(0,i):
        if(i%2==0):
            print("@",end="")
        else:
            print("#",end="")
    print()