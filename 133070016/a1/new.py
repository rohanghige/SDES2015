import gcd

def test_gcd():
	assert gcd.gcd(3,5) == 1
	assert gcd.gcd(13,14) == 1
	assert gcd.gcd(12,14) == 2

test_gcd()
