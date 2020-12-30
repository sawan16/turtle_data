import turtle
import random


t = turtle.Turtle()

t.pensize(2)
t.speed(15)
while True:
	for i in range(10):
		t.pencolor((random.random(),random.random(),random.random()))
		t.circle(5+10*i)
		t.right(90)
		t.forward(10)
	t.clear()

turtle.exitonclick()
