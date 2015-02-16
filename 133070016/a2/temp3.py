import math
from copy import deepcopy

def plot(c,a):
	x = 30
	y = 80
	A = []
	for i in range(x):
		A.append([])
		for j in range(y):
			A[i].append(" ")
			#print '',join(A[i])
	
	#print A
	
	for i in range(len(c)):
		#print c[i], a[i]
		A[c[i]][a[i]] = "*"
	
	#print A
	#B = A
	B = deepcopy(A)
	for i in range(x):
		#print "YYYYYYYYYYYYY"
		print ''.join(B[i])
	
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
		#temp = int(math.floor	(	((x)/2 - 1)	*		math.cos(b[i])			))
		temp2 = (x)/2 - temp
		c.append(temp2)

	plot(c,a)

