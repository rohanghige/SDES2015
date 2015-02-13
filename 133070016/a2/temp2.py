import math

def plot(c,a):
	x = 30
	y = 80
	A = []
	for i in range(x):
		A.append([])
		for j in range(y):
			A[i].append(0)
	
	print A
	
	for i in range(len(c)):
		print c[i], a[i]
		A[c[i]][a[i]] = 1
	
	print A
	for i in range(x):
		for j in range(y):
			if A[i][j] == 1:
				print
	
if __name__=="__main__":
	x = 30
	y = 80
	a = range(y)
	b = []
	for i in a:
		b.append(float(math.pi*2*i)/y)

	#print a
	#print b

	c = []
	d = []
	for i in a:
		#d.append(float(math.pi)*b[i])
		temp = int(math.floor	(	((x)/2 - 1)	*		math.sin(b[i])			))
		temp2 = (x)/2 - temp
		c.append(temp2)

	plot(c,a)

