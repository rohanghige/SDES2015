from gcd import gcd

def test_gcd():
	try:
		assert gcd(3L,5.0) == 1
	except TypeError:
		pass
	#assert gcd(13L,14) == 1
	#assert gcd(12,14) == 2
	try:
		assert gcd(12,-14) == 2
	except ValueError:
		pass
		
	try:
		assert gcd(-1,23) == 1
	except ValueError:
		pass
		
	

test_gcd()
