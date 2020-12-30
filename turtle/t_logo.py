import turtle
from numpy.random import randn
import random 
t = turtle.Turtle()
t.speed(50)
t.pensize(1)

while True:
	t.penup()
	t.setposition((randn(1)[0]*100,randn(1)[0]*100))
	t.pendown()
	t.pencolor((random.random(),random.random(),random.random()))
	turtle.bgcolor((random.random(),random.random(),random.random()))
	for i in range(20):
		t.forward(40)
		t.left(170)
	t.clear()

turtle.exitonclick()
