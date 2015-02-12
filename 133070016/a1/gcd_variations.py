def scan_in():
	try:
		a = raw_input()
		a = int(a)
	except ValueError:
		try:
			a = long(a)
		except ValueError:
			raise TypeError("Yo yo")
			#raise ValueError("ASDSSDS")
	return a
	
def gcd(a,b):
	#print a,b
	if a<b: 
		a,b = b,a
	if b==1:
		return 1
	elif b==0:
		return a
	else:
		return gcd(b, a%b )

#a = int(raw_input())
#b = int(raw_input())
i = 0
nums = []
while i < 2:
	t = scan_in()
	nums.append(t)
	i = i +1

c = gcd(nums[0],nums[1])
#print "gcd of " ,a," and ",b,"is :",c
print "gcd is ", c
