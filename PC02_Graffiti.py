#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

turtle.right(90)

turtle.forward(100)

turtle.right(90)

turtle.forward(100)

turtle.right(90)

turtle.forward(100)

turtle.goto(-90,90)

turtle.circle(100)

turtle.goto(90,-100)

turtle.goto(100,-150)

turtle.right(90)

turtle.forward(60)

turtle.setheading(30)

turtle.setheading(90)

turtle.setheading(180)

turtle.setheading(30)

turtle.setheading(280)

turtle.forward(30)

turtle.setheading(280)

turtle.setheading(90)

turtle.setheading(180)

turtle.setheading(200)

turtle.forward(30)

turtle.forward(30)

turtle.setheading(90)

turtle.forward(90)

turtle.backward(25)

turtle.goto(90,90)

turtle.setheading(30)

turtle.setheading(20)

turtle.setheading(45)

turtle.forward(60)

turtle.setheading(0)

turtle.forward(60)

turtle.setheading(315)

turtle.forward(60)

turtle.setheading(270)

turtle.forward(60)

turtle.setheading(225)

turtle.forward(60)

turtle.setheading(180)

turtle.forward(60)

turtle.setheading(135)

turtle.forward(60)

turtle.setheading(90)

turtle.forward(60)

turtle.goto(-100,100)

turtle.goto(100,100)

turtle.goto(-150,-200)

turtle.color("blue")

turtle.pensize(6)

turtle.begin_fill()

turtle.forward(100)

turtle.setheading(280)

turtle.setheading(180)

turtle.forward(100)

turtle.setheading(270)

turtle.forward(100)

turtle.setheading(0)

turtle.forward(100)

turtle.end_fill()



#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
#turtle.done()
