n = int(input("Enter the value of terms: "))
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i+1
print("\nSum = ", sum)


num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if num == sum: 
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

i = 0
while i <= 0:
    print("I WILL RUN FOREVER")
