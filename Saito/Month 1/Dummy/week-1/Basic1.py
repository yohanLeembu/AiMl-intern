# variables
"""
name = "saito"
age = 22
print(name, age)
print("hello my name is", name, "and i am", age)
"""

# practice
"""
number  = 4
float = 3.14
text = "python"
status = True

print(type(number))
print(type(float))
print(type(text))
print(type(status)) 
"""
# operators
"""
a = 10
b = 5

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
"""
#input and output
"""
name = input("Enter your name: ")
time = input("Enter time: ")

print ("Hello", name, "the time is", time)
"""
#if else
"""
age = 20
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
"""

#loops
"""
for i in range(3):
    print(i)
"""

#while loop
"""
count = 1 
while count <= 3:
    print(count)
    count += 1
"""

#functions
"""
def add(a,b):
    return a + b
print(add(1, 5))
"""

# dictionary
"""
student = {
    "name": "saito",
    "age": 22,
    "major": "computer"
}
print(student["name"], student["age"], student["major"])
"""


# file handling
"""
with open('filehandling.txt', 'w') as file:
    file.write("Hello, this is a test file.\n")
    file.write("This file is created for file handling\n")


with open("filehandling.txt","r") as file:
    print(file.read())
"""

# modules
"""
import math
import random

print(math.sqrt(25))
print(random.randint(1, 10))
"""

#classes (bassic Oop)

class Student:
    def __init__(self,name):
        self.name = name

    def display(self):
        print(self.name)

s = Student("Saito")
s.display()


