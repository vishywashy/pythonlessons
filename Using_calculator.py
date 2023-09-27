#imports the file Calculator.py and the class Calculator.
from Calculator import Calculator
#object which takes in two arguements.
number = Calculator(input("Enter a number:"),  input("Enter a number:"))

try:
    #Depending on what sign the user enters it will perform a calculation.
    sign = input("Enter a sign?:")
    if sign == "+":
        print(number.addition())
    elif sign == "-":
        print(number.subtraction())
    elif sign == "*":
        print(number.multiplication())
    elif sign == "/":
        print(number.division())
    else:
        print("Error")
#This line of code helps you handle the error.
except ValueError as i:
    #This will display the error as i is a variable and is assigned to the Value error generated.
    print(i)
    print("Enter a number.")