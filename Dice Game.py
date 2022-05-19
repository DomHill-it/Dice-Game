# dicebettingrand by Dominique Hill

from random import randrange

# Rules of the dicebettingrand Game
print("Welcome to Dicebettingrand. In this game you be using a betting simulation.")
print("The user will tell me how much they would like to bet.")
print("After the bet a random number between 1 and 6.")
print("If the users random number is higher than the computer user wins $")
print("if the users random number lower than the computer user losses $$")
print("I will keep track of the users win/loss total.")
print("After each bet I will ask you (the user) if you want to continue.")

# User types in amount to bet
userbet = input('Hello user. Enter the amount that you want to bet')

# Generate random number for user
userrandom = randrange(1, 7)
print("Hello user your number is ", userrandom)

# Generate random number for computer
computerrandom = randrange(1, 7)
print("Hello computer your number is ", computerrandom)

# if statements: If user random is higher than computer random number (user wins/computer loss).
# If statements: If user random is lower  than computer random number (user loss/computer wins).
if userrandom > computerrandom:
    print("User wins", userbet, "Computer losses", userbet)
if userrandom < computerrandom:
    print("User Loses", userbet, "Computer wins", userbet)

print("Total Win/Loss=", userbet)

# playagain variable
playagain = "yes"

# While Loop to allow the user to keep playing the game
while playagain == "yes":
    if userrandom > computerrandom:
        print("User wins", userbet, "Computer losses", userbet)
    if userrandom < computerrandom:
        print("User Loses", userbet, "Computer wins", userbet)
    playagain = input("Would you like to play. Enter yes/no")

if playagain != "yes":
    print("Thanks for playing")
    print("Game Ends Here")

