#This code asks the user to type the size of the base and height of the shape.Based on this this program will calculate the area.

def info():
    global base, height
    repeat = int(input("How many times do you want to repeat this program:"))
    while int(repeat) > 0:
        base = input("how long is the base:")
        height = input("What is the height of the triangle:")
        calculate()
        repeat -= 1


def calculate():
    area = int(base) / 2 * int(height)
    print(area)

try:
   info()
except:
    print("You must enter a number")
