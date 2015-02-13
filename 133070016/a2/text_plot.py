import matplotlib.pyplot as plt
import math

def plot(x,y):
	plt.plot(x,y,'*')
	#plt.plot(x,y,'ro')
	plt.show()
	
if __name__=="__main__":
	N = 100
	a = range(N)
	b = []
	for i in a:
		b.append(float(a[i])/N)

	#print a
	#print b

	c = []
	d = []
	for i in a:
		d.append(float(math.pi)*b[i])
		c.append(math.sin(float(math.pi*2)*b[i]))

	plot(d,c)
