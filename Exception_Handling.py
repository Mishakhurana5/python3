try:
    number = int(input("Please enter a number: "))
    print("The number you entered is :", number)

except ValueError as ex:
    print("Exception")

try:
    num1, num2 = eval(input("Please enter two numbers seprated by a comma:"))
    result = num1/num2
    print("The result is:", result)

except ZeroDivisionError:
    print("Exception: division by zero is an error")

except SyntaxError:
    print("Exception: please enter two numbers seperated by a comma like this: 1,2")

except:
    print("Wrong input, try again")

else: 
    print("No exceptions")

finally:
    print("This will always execute")

valid = False
while not valid:
    try:
        n = int(input("Please enter a number:"))
        while n%2==0:
        
           print("Bye!")
        valid = True
    except ValueError:
        print("Please enter a even number")