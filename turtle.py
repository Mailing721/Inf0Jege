from turtle import *
tracer(0)
m = 25
pd()
right(135)
for i in range(7):
	forward(7*m)
	right(45)
	forward(8*m)
	right(135)
pu()
for x in range(-20, 20):
	for y in range(-20, 20):
		goto(x*m, y*m)
		dot(3, 'red')
done()