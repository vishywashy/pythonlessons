#creates a class called Calculator
class Calculator:
    #Constructor with 3 parameters self num1 and num2 to initialise num1 and num2.
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    #Defines a subroutine called addition which takes in a parameter self
    def addition(self):
            #Casts the instance attributes of num1 and num2 into a float and then returns the sum.
            return float(self.num1) + float(self.num2)


    #Defines a subroutine called subtraction which takes in a parameter self
    def subtraction(self):
        #Casts the instance attributes of num1 and num2 into a float and then returns the difference.
            return float(self.num1)-float(self.num2)

    #Defines a subroutine called multiplication which takes in a parameter self
    def multiplication(self):
            #Returns the product of the instance attributes of num1 and num2
            return float(self.num1)*float(self.num2)

    #Defines a subroutine called subtraction which takes in a parameter self.
    def division(self):
            #Casts the instance attributes of num1 and num2 into a float and then returns the quotient of the instance attributes of num1 and num2.
            return float(self.num1)/float(self.num2)

















