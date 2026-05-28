string = input("Please enter your name: ")
char = input("Please enter a character: ")
i = 0
count = 0
while (i < len(string)):
    if (string[i] == char):
        count = count + 1
    i = i + 1
print("The total number of times", char, "has occurred =", count)

# is the number a prime number or not
lower = int(input("Enter the lower range: "))
upper = int(input("Enter the upper range: "))
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

# Mid product of four numbers

# Input a number

num = int(input("Enter a 4 digit number : "))

t = num
numLen = 0

# iterate the loop
while t > 0:
    numLen = numLen + 1
    t = int(t / 10)

if numLen >= 4:   # condition 1

    numLen = int(numLen / 2)
    chk = 0

    while num > 0:   # iterate loop

        rem = num % 10

        if chk == numLen:   # nested condition 1
            midOne = rem

        elif chk == (numLen - 1):
            midTwo = rem

        num = int(num / 10)
        chk = chk + 1

    prod = midOne * midTwo   # product of middle digits

    # display the result
    print("\nProduct of Mid digits (" + str(midOne) + "*" + str(midTwo) + ") = ", prod)
else:
    print("\nNumber should have at least 4 digits")