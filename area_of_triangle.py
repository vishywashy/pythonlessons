#This code asks the user to type the size of the base and height of the shape.Based on this this program will calculate the area.

def info():
    base = input("how long is the base:")
    height = input("What is the height of the triangle:")
    calclist=[base, height]
    return calclist


def calculate(num):
    area = float(num[0]) / 2 * float(num[1])
    print(str(area)+" is the area of the triangle.")





try:
   calc=info()
   calculate(calc)

except ValueError as value:
    print(value)
    print("You must enter a number.")
