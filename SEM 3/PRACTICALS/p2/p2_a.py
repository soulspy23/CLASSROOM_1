#18th July
# Write a function that takes a character (i.e. a string of length 1) and returns Trueif it is a vowel, False otherwise.

print("**************************************************")
print("Program to detect if a character is a vowel or not")
print("**************************************************\n")

def vowels(ch):
    if (ch == "a" or ch == "A" or ch == "e" or ch == "E" or ch == "i" or ch == "I" or ch == "o" or ch == "O" or ch == "u" or ch == "U"):
        return True
    else:
        return False 
ch = input("enter a value:")
while (not(ch.isalpha())):
    ch = input("enter a value:") 
if(vowels(ch)):
    print("vowel")
else:
     print("consonant")