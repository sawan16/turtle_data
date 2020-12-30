import turtle
import time
t = turtle.Turtle()

t.pencolor("red")
t.fillcolor("orange")
t.pensize(5)
t.speed(9)
while True:
	t.begin_fill()
	t.circle(60)
	t.end_fill()
	time.sleep(2)
	t.clear()

turtle.exitonclick()
