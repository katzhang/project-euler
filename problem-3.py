"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
def check_prime(n):
	prime = True
	for divisor in range(2, n):
		if n % divisor == 0:
			prime = False
			break
	return prime


def find_prime_factor(n):
	indicator = True
	startnumber = 1
	while startnumber < n and indicator:
		if n % startnumber == 0 and check_prime(int(n/startnumber)):
			indicator = False
			return n/startnumber
		else:
			startnumber = startnumber + 1


def find_prime_factor2(n):
	d = 3
	while (d * d < n):
	    if n % d == 0: 
	    	n /= d
	    else: 
	    	d += 2
	return n

print(find_prime_factor2(600851475143))