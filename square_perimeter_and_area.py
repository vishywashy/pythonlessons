#This code will ask for the first side and the second side.Based on the numbers you typed it will calculate the perimeter and area.
def side():
    side1 = input("Give me the first side of the square:")
    return side1
def area_and_perimeter(side):
    perimeter = int(side) * 4
    area = int(side) ** 2
    print("the perimeter is " + str(perimeter))

    print("the area is " + str(area))

try:
  calc=side()
  area_and_perimeter(calc)
except:
    print("You need to enter a number.")