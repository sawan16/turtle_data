import turtle
import random 
t = turtle.Turtle()

t.speed(15)
t.pensize(3)
while True:
	for i in range(10):
		t.circle(1+5*i)
		t.pencolor((random.random(),random.random(),random.random()))
		t.goto(i*10,i*10)
	for i in range(10):
		t.circle(1+5*i)
		t.pencolor((random.random(),random.random(),random.random()))
		t.goto(i*10,-i*10)
	for i in range(10):
		t.circle(1+5*i)
		t.pencolor((random.random(),random.random(),random.random()))
		t.goto(-i*10,-i*10)
	for i in range(10):
		t.circle(1+5*i)
		t.pencolor((random.random(),random.random(),random.random()))
		t.goto(-i*10,i*10)
	t.clear()

turtle.exitonclick()
