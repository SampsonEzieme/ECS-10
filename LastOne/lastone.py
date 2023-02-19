## lastone.py
## all of us
## October 3, 2016
##
## plays last one loses

## still to do :
## give magic number 4 a name
## clean up duplicate pieces of program
## verify that choice A is 1,2, or 3
## verify that input is an integer
## fix the grammar
## pause between print statements
## restart game if player wants to play again

stack = 9 # number of pennies

## start the game

print("Let's play Last One Loses.")

print("You go first.")

## player A moves

print("There are", stack, "pennies")

a_choice = int(input("Choose 1, 2, or 3 pennies from the stack: "))

## Need to validate that A says 1, 2, or 3
## not yet

print("You chose", a_choice, "pennies.")

print("I choose", 4 - a_choice, "pennies.")

stack = stack - 4

print("There are", stack, "many pennies left")

a_choice_2 = int(input("Choose again. Only 1, 2, or 3 pennies from the stack: "))

print("You chose", a_choice_2, "pennies.")

print("I choose", 4 - a_choice_2, "pennies.")

stack = stack -4

print("There are", stack, "many pennies left")

print("You Lose.")

print("Player B wins the game")


    

