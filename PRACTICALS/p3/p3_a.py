#q8th July
# write a function to check a sentence to see if it is a pangram or not.

def pangram(string):
    str='abcdefghijklmnopqrstuvwxyz'
    for x in str:
        if x not in string:
            return False
    return True

string = input("enter a value:")
if (pangram(string.lower())):
    print("it is a pangram")
else:
    print("it is not a pangram")
