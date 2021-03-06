"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

def method_1():
	n = 1
	m = 2
	max_value = 4000000
	sum = 2
	while n < max_value:
		n = n + m
		m = n + m
		if n < max_value and n % 2 == 0:
			sum = sum + n
		if m < max_value and m % 2 == 0:
			sum = sum + m 

	print(sum)

def method_2():
	

method_1()