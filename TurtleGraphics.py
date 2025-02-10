#TurtleGraphics.py
#Name:Brooks Conway
#Date:2/10/25
#Assignment:

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

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
    # drawPolygon(myTurtle, 8) #draws an octogon

    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
