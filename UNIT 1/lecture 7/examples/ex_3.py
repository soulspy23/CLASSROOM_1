#accept a input from player 1 and player 2 for rock/paper/scissors and display the winner

print("rock = r \npaper = p \nscissors = s")
p1 = input("Player 1: ")
p2 = input("Player 2: ")
if p1 == p2:
    print("Draw")
elif (p1 == "r" and p2 == "s" or p1 == "s" and p2 == "p" or p1 == "p" and p2 == "r"):
    print("Player 1 wins")
elif (p2 == "r" and p1 == "s" or p2 == "s" and p1 == "p" or p2 == "p" and p1 == "r"):
    print("Player 2 wins")
else:
    print("Invalid input")