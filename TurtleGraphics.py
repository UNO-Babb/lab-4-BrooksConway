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
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
