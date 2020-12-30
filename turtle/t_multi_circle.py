import turtle
import random


t = turtle.Turtle()

t.pensize(2)
t.speed(20)
while True:
	for i in range(20):
		t.penup()
		t.setposition((0,-10*i))
		t.pendown()
		t.pencolor((random.random(),random.random(),random.random()))
		t.circle(5+10*i)
	t.clear()

#turtle.hideturtle()

turtle.exitonclick()
