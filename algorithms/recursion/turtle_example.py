#https://runestone.academy/runestone/static/pythonds/Recursion/pythondsintro-VisualizingRecursion.html
import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, lineLen, count):
    if count > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(30)
        drawSpiral(myTurtle,lineLen, count-1)
    else:
        lineLen = lineLen - 3
        if lineLen < 0:
            return
        else:
            drawSpiral(myTurtle,lineLen,12)

drawSpiral(myTurtle,50, 12)
myWin.exitonclick()
