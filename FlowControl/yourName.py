#program that is stuck in a loop unless given the input "your name"
yourName = ''
while (yourName != "your name"):
    yourName = input("Please enter 'your name': ")
print("Thank you!")