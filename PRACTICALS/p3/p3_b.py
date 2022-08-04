# write a program that prints out all the elements of the list that are less than 5

a = (1,1,2,3,5,8,13,21,34,55,89)
def checklist(a):
    for x in a:
        if x < 5:
            print(x)
        
checklist(a)