#This program says hello and asks for the users name
print("Hello World!")
name = input("Enter your name: ")
#print(name)
#greet the user
print("It is nice to meet you, " + name + "!")
#get length of string
lengthOfName = len(name)
print("There are " + str(lengthOfName) + " letters in your name")
#get users age 
age = int(input("Enter your age: "))
#print(age)
#get their age in a year
age += 1
print("You will be " + str(age) + " next year!")