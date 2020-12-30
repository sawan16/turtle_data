import turtle
from numpy.random import randn 
t = turtle.Turtle()

while True:
	t.goto(int(randn(1)[0]*100),int(randn(1)[0]*100))

turtle.exitonclick()
