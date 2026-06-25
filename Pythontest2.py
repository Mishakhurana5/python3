def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

pick_your_operation = input("Please select a, b, c, or d : a.Add b.Subtract c.Multiply d.Divide: ")

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if pick_your_operation == "a" or pick_your_operation == "A":
        print("Result:", add(num1, num2))
    elif pick_your_operation == "b" or pick_your_operation == "B":
        print("Result:", subtract(num1, num2))
    elif pick_your_operation == "c" or pick_your_operation == "C":
        print("Result:", multiply(num1, num2))
    elif pick_your_operation == "d" or pick_your_operation == "D":
        print("Result:", divide(num1, num2))
    else:
        print("Invalid input, you have to select from a,b,c or d")

except ValueError:
    print("Please enter only numbers!")
except ZeroDivisionError:
    print("You can't divide by zero!")
