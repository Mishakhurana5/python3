# Import necessary Modules
from abc import ABC, abstractmethod


# Create base class
class Absclass(ABC):

    # Function to print a value
    def print(self, x):
        print("Passed value: ", x)

    # Abstract Method
    @abstractmethod
    def task(self):
        print("We are inside Absclass task")


# Create sub class
class test_class(Absclass):

    def task(self):
        print("We are inside test_class task")


# object of test_class created
test_obj = test_class()
test_obj.task()
test_obj.print(100)


# import necessary packages
from abc import ABC, abstractmethod

# create a base class
class Animal(ABC):

    # abstract method
    # should be implemented by all sub-classes
    @abstractmethod
    def move(self):
        pass


# sub classes
class Human(Animal):

    def move(self):
        print("I can walk and run")


class Snake(Animal):

    def move(self):
        print("I can crawl")
class Dog(Animal):

    def move(self):
        print("I can bark")


class Lion(Animal):

    def move(self):
        print("I can roar")


# Driver code
R = Human()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()

K = Lion()
K.move()


class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")

class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")
obj_ind = India()
obj_usa = USA()

for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()