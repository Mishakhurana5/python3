x = 5
if(type(x) is int):
    print ("true")
else:
    print("false")

    x = 5.5
if(type(x) is not float):
    print("true")
else:
    print("false")

x = 20 
y = 20
if (x is y):
    print("x and y same idetity")
y = 30
if (x is not y):
    print ("x and y have different identitys")



a = 10
b = -10
print('a >> 1 =', a >> 1)
print('b >> 1 =', b >> 1)

a = 5
b = -10
print('a << 1 =', a << 1)
print('b << 1 =', b << 1)



print("Marks obtained in 5 subjects:")

mark1 = int(input())
mark2 = int(input())
mark3 = int(input())
mark4 = int(input())
mark5 = int(input())

tot = mark1 + mark2 + mark3 + mark4 + mark5
avg = tot/5
validrange = range(0,101)

if avg not in validrange:
    print("invalid input!")
elif avg in range(91, 101):
    print("Your grade is A1")
elif avg in range(81, 91):
    print("Your grade is A2")
elif avg in range(71, 81):
    print("Your grade is B1")
elif avg in range(61, 71):
    print("Your grade is B2")
elif avg in range(51, 61):
    print("Your grade is C1")
elif avg in range(41, 51):
    print("Your grade is C2")
elif avg in range(31, 41):
    print("Your grade is D1")
elif avg in range(31, 21):
    print("Your grade is D2")
else:
    print("Your grade is F")