#Written by liam henry 20/11/2021

def combination(n,r): #Combination function.
	c = factorial(n) // (factorial (r) * factorial(n - r)) #double // to avoid decimal answers.
	return c

def factorial (x): #Factorial function.
	if x == 1: #Base case.
		return x 
	else:	   #Recursive case.
		return x * factorial(x - 1)

#When choosing 2 items from a set of 6 items there's a total of 15 possible combinations.
#Therefore the expected output for this program with the given values is 15.
print (combination(6,2))

#c = n!/(r!(n-r)!).
#c = combination.
#n = number of items in set.
#r = number of choosing items from the set.