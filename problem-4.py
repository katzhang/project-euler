"""
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
def is_palindrome(n):
	return str(n) == str(n)[::-1]

print(is_palindrome(12930))
print(is_palindrome(1234321))

def find_palindrome():
	result = 0
	for n in range(999, -1, -1):
		for m in range(999, -1, -1):
			if (is_palindrome(n * m)) and result < n * m:
				result = n * m
	return result

print(find_palindrome())