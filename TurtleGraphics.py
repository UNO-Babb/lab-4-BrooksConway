#TurtleGraphics.py
#Name:Brooks Conway
#Date:2/10/25
#Assignment: Turtle Graphics

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

hideturtle() 
def drawSquare(myTurtle):
  for i in range(4):
    myTurtle.forward(100)
    myTurtle.right(90)
bob = turtle.Turtle()
drawSquare(bob)
def drawSquare(myTurtle, size):
  for i in range(4):
    myTurtle.forward(size)
    myTurtle.right(90)

def main():
    myTurtle = turtle.Turtle()
    # drawPolygon(myTurtle, 5) #draws a pentagon
hideturtle()
  num_sides = 5
  side_length = 100
  penup()
  left(90)
  forward(50)
  right(90)
  pendown()
  for i in range(num_sides):
    forward(side_length)
    right(360 / num_sides)
    # drawPolygon(myTurtle, 8) #draws an octogon
hideturtle()
  num_sides = 8
  side_length = 100
  penup()
  left(90)
  forward(50)
  right(90)
  pendown()
  for i in range(num_sides):
    forward(side_length)
    right(360 / num_sides)

    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    def drawSquare(myTurtle):
  for i in range(4):
    myTurtle.forward(100)
    myTurtle.right(90)
bob = turtle.Turtle()
drawSquare(bob)
def drawSquare(myTurtle, size):
  for i in range(4):
    myTurtle.forward(size)
    myTurtle.right(90)
forward(50)
right(90)
begin_fill()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.
def drawSquare(myTurtle):
  for i in range(4):
    myTurtle.forward(100)
    myTurtle.right(90)
bob = turtle.Turtle()
drawSquare(bob)
def drawSquare(myTurtle, size):
  for i in range(4):
    myTurtle.forward(size)
    myTurtle.right(90)
right(90)
forward(50)
begin_fill()
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()
    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares

    penup()
back(50)
left(90)
forward(50)
pendown()
right(90)
forward(200)
right(90)
forward(200)
right(90)
forward(200)
right(90)
forward(200)
penup()
back(20)
right(90)
forward(20)
pendown()
forward(160)
right(90)
forward(160)
right(90)
forward(160)
right(90)
forward(160)
penup()
back(20)
right(90)
forward(20)
pendown()
forward(120)
right(90)
forward(120)
right(90)
forward(120)
right(90)
forward(120)
penup()
back(20)
right(90)
forward(20)
pendown()
forward(80)
right(90)
forward(80)
right(90)
forward(80)
right(90)
forward(80)
penup()
back(20)
right(90)
forward(20)
pendown()
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)

    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares
    forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
penup()
back(10)
right(90)
forward(10)
pendown()
forward(80)
right(90)
forward(80)
right(90)
forward(80)
right(90)
forward(80)
penup()
back(10)
right(90)
forward(10)
pendown()
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
penup()


main()
