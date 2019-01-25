import math

def num_coeff(x1,x2,x3,y1,y2,y3):

	a=(x1*(y3 - y2) + x2*(y1 - y3) + x3*(y2 - y1))/((x1 - x2)*(x1 - x3)*(x2 - x3))
	b=((y2-y1) / (x2-x1))- (a*(x1+x2))
	c=y1 - a*x1*x1 - b*x1
	print(a)
	print(b)
	print(c)

num_coeff(0.0759,0.0540,0.5308,0.7792,0.9340,0.1299)
