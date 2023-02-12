#This code will ask for the first side and the second side.Based on the numbers you typed it will calculate the perimeter and area.
def side():
    global side1, side2
    side1 = input("Give me the first side:")
    side2 = input("Give me the second side:")


def area_and_perimeter():
    perimeter = int(side1) + int(side1) + int(side2) + int(side2)
    area = int(side1) * int(side2)
    print("the perimeter is " + str(perimeter))

    print("the area is " + str(area))

try:
  side()
  area_and_perimeter()
except:
    print("You need to enter a number")