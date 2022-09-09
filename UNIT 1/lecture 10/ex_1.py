#9th July 2022

#function to display the cumulative sum of numbers entered

def calc():
    sum = 0
    character = 'y'
    while(character != 'x' and character != 'X'):
        character = input("Enter value :")
        if(character == 'x' or character == 'X'):
            print(sum)
        else:
            character = int(character)
            sum = sum + character
    
calc()