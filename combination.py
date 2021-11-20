def combination(n,r):
	c = factorial(n) / (factorial (r) * factorial(n - r))
	return c

def factorial (x):
	if x == 1:
		return x
	else:
		return x * factorial(x - 1)


print (combination(6,2))