#PATTERNS
import turtle
from random import randint
from random import choice

def reset():
    turtle.reset()

def setUp():
    turtle.speed(50)
    turtle.setup(1000, 800)

def drawRectanglePattern(xPos, yPos, height, width, offset, count, rotation):
    countAng = 360 / count
    turtle.penup()
    turtle.goto(xPos + offset, yPos)

    for i in range(0, count):
        turtle.penup()
        turtle.circle(offset, countAng)
        head = turtle.heading()
        turtle.right(rotation)
        turtle.pendown()
        drawRectangle(height, width)
        turtle.seth(head)

    return drawRectanglePattern

def drawRectangle(height, width):
    turtle.pendown()
    turtle.color(setRandomColor())
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    return drawRectangle

def setRandomColor():
    num = randint(0, 4)
    color = "blue"
    if num == 0:
        color = 'blue'
    elif num == 1:
        color = 'red'
    elif num == 2:
        color = 'green'
    else:
        color = 'orange'
    return color

def done():
    turtle.done()

def drawCirclePattern(xPos, yPos, radius, offset, count):
    countAng = 360 / count
    turtle.speed(50)
    turtle.setup(1000, 800)
    turtle.penup()
    turtle.goto(xPos + offset, yPos)

    for i in range(0, count):
        turtle.pendown()
        turtle.circle(-offset, countAng)
        turtle.pendown()
        turtle.color(setRandomColor())
        turtle.circle(radius)

    return drawCirclePattern

def drawSuperPattern(number):
    for i in range(number):
        xPos = randint(0, 500)
        yPos = randint(0, 500)
        radius = randint(0, 200)
        offset = randint(0, 100)
        count = randint(0, 50)
        height = randint(0, 500)
        width = randint(0, 500)
        rotation = randint(0, 45)

        for choice in range(0, 2):
            if choice == 0:
                drawRectanglePattern(xPos, yPos, height, width, offset, count, rotation)
            elif choice == 1:
                drawCirclePattern(xPos, yPos, radius, offset, count)
