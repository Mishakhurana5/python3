a = 5
print("type of a:", type(a))

b = 2.5
print("type of b:", type(b))

c = "coding"
print("type of c", type(c))

d = True
print("type of d:", type(d))


name = "Penguin"
age = 11
is_student = True
weight = 38.5

print("Name :", name)
print("Datatype of name is ", type(name))

print("Age :", age)
print("Datatype of age is ", type(age))

print("is_student :", is_student)
print("Datatype of is_student is ", type(is_student))

print("weight :", weight)
print("Datatype of weight is ", type(weight))

print("\n after Typecasting... ")
age = str(age)
print(age)
print("Datatype of age is ", type(age))

weight = int(weight)
print(weight)
print("Datatype of weight is ", type(weight))


text = str(input("Enter a string :"))
revtext = text [::-1]
text = revtext
print("reverse of given string is :")
print (text)