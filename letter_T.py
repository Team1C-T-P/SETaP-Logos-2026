import turtle
def drawT(startx, starty, turtle: turtle.Turtle):
    t = turtle
    
    t.goto(startx, starty)
    t.fillcolor("lightblue")
    t.begin_fill()
    t.forward(100)
    t.right(90)
    t.forward(15)
    t.right(90)
    t.forward(40)
    t.left(90)
    t.forward(85)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(85)
    t.left(90)
    t.forward(40)
    t.right(90)
    t.forward(15)
    t.end_fill()
 

turtle.done()