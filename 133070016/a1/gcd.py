def scan_in(a):
	if a < 0:
		raise ValueError
		
	if type(a) == int:
		return a
	elif type(a) == long:
		return a
	else:
		raise TypeError
	
def gcd(a,b):
	#print a,b
	#print type(a)
	#print type(b)
	a = scan_in(a)
	b = scan_in(b)
	#print type(a)
	#print type(b)
	#print a,b
	if a<b: 
		a,b = b,a
	if b==1:
		return 1
	elif b==0:
		return a
	else:
		return gcd(b, a%b )

#a = raw_input()
#b = raw_input()
#c = gcd(a,b)
#print c
