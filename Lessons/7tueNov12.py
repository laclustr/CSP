def pow(x, n):
	result = 1

	while n > 0:
		result *= x
		n -= 1

	return result

def fib(n):
	if n == 1:
		return 1

	num1 = 0
	num2 = 1

	i = 2

	while i <= n:
		temp = num2
		num2 += num1
		num1 = temp
		
		i += 1

	return num2

print(fib(7))