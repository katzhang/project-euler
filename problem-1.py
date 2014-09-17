"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
# method 1
def method_1():
	nums = list(range(1000))
	sum = 0
	for n in nums:
		if n % 3 == 0 or n % 5 == 0:
			sum = sum + n
	return sum


print(method_1())


#method 2: use list comprehension
sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0])