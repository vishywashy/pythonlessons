# This is a class it requires the object to be initialised
# The constructor takes in two parameters
class add:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
#The add method takes in adds the class variables(num1, num2) and returns the integer.
    def add(self):
        adding = self.num1 + self.num2
        return adding
