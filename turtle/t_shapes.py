import turtle
import time

t = turtle.Turtle()
while True:
	t.shape("turtle")
	time.sleep(1)
	t.shape("arrow")
	time.sleep(1)
	t.shape("circle")
	time.sleep(1)
	t.shape("square")
	time.sleep(1)
	t.shape("classic")

turtle.exitonclick()
