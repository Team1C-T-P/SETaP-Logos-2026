import turtle
from letter_F import drawF
from letter_H import drawH
from letter_T import drawT
from letter_r import drawR
from hanger import drawHanger
t = turtle.Turtle()

t.pensize(5)
t.speed(5)

drawT(-500, 100, t)
drawH(-400, 100, t)
drawR(-300, 100, t)
drawF(-100, 100, t)