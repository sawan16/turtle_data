import turtle
import random 
t = turtle.Turtle()

t.pensize(3)
t.speed(15)

while True:
	for i in range(10):
		t.pencolor((random.random(),random.random(),random.random()))
		t.fd(100+i*5)
		t.rt(90)
		t.fd(100+i*5)
		t.rt(90)
		t.fd(100+i*5)
		t.rt(90)
		t.fd(100+i*5)
	t.clear()

turtle.exitonclick()
