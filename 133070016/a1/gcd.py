def scan_in(a):
	try:
		#a = raw_input()
		a = int(a)
		#print "Batata"
		if a < 0:
			raise TypeError
		return a
	except ValueError:
		try:
			a = long(a)
			if a < 0:
				raise TypeError
		except ValueError:
			raise TypeError
			#raise ValueError("ASDSSDS")
		return a
	
def gcd(a,b):
	#print a,b
	a = scan_in(a)
	b = scan_in(b)
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
#gcd(a,b)
