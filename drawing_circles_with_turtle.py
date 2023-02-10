import turtle
from time import sleep
from random import randint
from random import choice
from math import pi

run = input("Press enter to run the program:")
if run == "":
    print("ok")
    print("3...")
    sleep(1)
    print("2...")
    sleep(1)
    print("1...")
    print("The program has started...")
else:
    print("ok")
    quit()
t = turtle.Pen()
t.shape("turtle")
colours = ["red", "orange", "blue", "black", "green", "purple", "yellow", "white"]
fillcolours = ["red", "orange", "blue", "black", "green", "purple", "yellow", "white"]
rando = 0
while rando <= 10:
    stop = input("Enter stop if you want to stop the program:")
    if stop == "stop":
        quit()
    else:
        print("ok...")
    t.penup()
    choices = choice(colours)
    t.color(choices)
    fills = choice(fillcolours)
    t.fillcolor(fills)
    x = randint(-400, 400)
    y = randint(-400, 400)
    t.goto(x, y)
    print("The turtle is at(%d, %d)" % (x, y))
    randomise = randint(1, 200)
    turtle.circle(randomise)
    print("This radius of the %d circle was %d pixels." % (rando + 1, randomise))
    area = pi * randomise ** 2
    print("The area of the circle is %f square pixels." % (area))
    circumference = pi * randomise * 2
    print("The circumference of the circle is %f square pixels." % (circumference))
    rando += 1
