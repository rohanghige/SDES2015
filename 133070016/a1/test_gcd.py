from gcd import gcd

def test_gcd():
	assert gcd(3.0,5.0) == 1
	assert gcd(False,True) == 1
	assert gcd(13,14) == 1
	assert gcd(12,14) == 2

test_gcd()
