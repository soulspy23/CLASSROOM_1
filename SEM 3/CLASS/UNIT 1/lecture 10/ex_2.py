#9th July 2022

#function to calculate the percentage and grade of a student based on 3 subject marks

s1 = input("Enter your marks for s1 :")
s2 = input("Enter your marks for s2 :")
s3 = input("Enter your marks for s3 :")

percentage = ((s1/s2/s3)/300)*100
print("Your percentage is :",percentage)

if(s1<40 or s2<40 or s3<40):
    print("You have failed")
elif(percentage>=90 and percentage<=100):
    print("You have got A")
elif(percentage>=60):
    print("You have got B")
elif(percentage>=40):
    print("You have got C")
else:
    print("You have failed")