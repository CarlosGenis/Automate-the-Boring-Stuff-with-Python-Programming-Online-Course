#this program is a guessing game
import random
getName = input("Enter your name: ")
print("Hey " + getName + " this is a guessing game. I'm thinking of a number between 1-20")
#generate the number 
randomNumber = random.randint(1,20)
#print(randomNumberfsfdfsaffafdf)
#give users 6 chances to guess
for turnsTaken in range(1,7):
    guess = int(input("Guess the number: "))
    if (guess < randomNumber):
        print("Too low!")
    elif (guess > randomNumber):
        print("Too high!")
    else:
        #this happens when the number guessed is the same as the random number
        break
if (guess == randomNumber):
    print("Well done " + getName + "! It took you " + str(turnsTaken) + " guesses to get the number")
else:
    print("Nice try but I was thinking of " + str(randomNumber))