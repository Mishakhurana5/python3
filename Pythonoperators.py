tree1 = 98
tree2 = 94
tree3 = 41
tree4 = 95
tree5 = 11

sum = tree1+tree2+tree3+tree4+tree5
print("The sum of all 5 trees is:", sum)

average = sum/5
print("The average of all the trees is:", average)



amount = int(input("Please enter the amount to withdraw:"))

note1 = amount//100
note2 = (amount%100)//50
note3 = ((amount%100)%50)//10

print("Notes of 100 rupee ", note1)
print("Notes of 50 rupee ", note2)
print("Notes of 10 rupee ", note3)



print("Enter Marks Obtained in 4 Subjects: ")
math = int(input("maths :"))
english = int(input("english :"))
science = int(input("science :"))
hindi = int(input("hindi :"))

sum = math + english + science + hindi
print("sum of math,english,science and hindi = ", sum)

perc = (sum/400)*100

print(end="Percentage Mark = ")
print(perc)