import math
from copy import deepcopy

def check_size(c,a,cols,rows):
	for i in range(len(c)):
		if rows <= c[i]:
			rows = c[i] + 1
		if cols <= a[i]:
			cols = a[i] + 1
	return cols-1, rows-1

def plot(c,a, cols = 80,rows = 30):
	#rows = rows + 1
	#cols = cols + 1
	
	#print cols, rows
	#print c
	#print a
	cols, rows = check_size(c,a,cols,rows)
	#print cols, rows
	cols = cols + 1
	rows = rows + 1
	#print cols, rows
	A = []
	for i in range(rows):
		A.append([])
		for j in range(cols):
			A[i].append(" ")
			#print '',join(A[i])
	#print A
	for i in range(len(c)):
		#print c[i], a[i]
		A[c[i]][a[i]] = "*"
	
	#print A
	#B = A
	B = deepcopy(A)
	for i in range(rows):
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
		temp = int(math.floor	(	(int((x-1)/2 ))	*		math.sin(b[i])			))
		#temp = int(math.floor	(	((x)/2 - 1)	*		math.cos(b[i])			))
		temp2 = int((x)/2) - temp
		c.append(temp2)

	plot(c,a)

