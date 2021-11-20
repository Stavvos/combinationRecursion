#Written by liam henry 20/11/2021

def combination(n,r): #combination function
	c = factorial(n) // (factorial (r) * factorial(n - r)) #double // to avoid decimal answers
	return c

def factorial (x): #factorial function
	if x == 1: #base case
		return x 
	else:	   #recursive case
		return x * factorial(x - 1)


print (combination(6,2))

#c = n!/(r!(n-r)!)
#c = combination
#n = number of items in set
#r = number of choosing items from the set