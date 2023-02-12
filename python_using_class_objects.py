#This code will ask the user to type two numbers after the user types in two numbers it will add them together.
from lesson_classes1 import add

try:
    x = add(int(input("Enter a number:")), int(input("Enter a number:")))
    print(x.add())
except ValueError as i:
    print(i)
    print("You need to enter a number.")
