#30th June 2022
c = 1
for i in range(6,0,-1):
    for j in range(0,i):
        if c%2==0:
            print("1",end="")
        else:
            print("0",end="")
        c+=1
    print()