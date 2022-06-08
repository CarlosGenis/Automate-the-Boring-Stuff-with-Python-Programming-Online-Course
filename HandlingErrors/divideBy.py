#division program with try and except statements
def divide42by(number):
    try:
        return 42 / number
    except:
        print("Cannot divide by zero")
print(divide42by(5))
print(divide42by(0))