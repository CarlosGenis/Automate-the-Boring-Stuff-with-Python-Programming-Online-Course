#this program asks the user how many pets they have and then validates their input
numOfPets = input("Enter number of pets: ")
try:
    if (int(numOfPets) >= 4):
        print("That is a lot of pets")
    elif (int(numOfPets) < 4 and int(numOfPets) > 0 ):
        print("That is not too many pets")
    else:
        print("You have no pets")
except ValueError:
    print("You did not enter a number")