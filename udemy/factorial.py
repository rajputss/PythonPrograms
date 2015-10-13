def factorial(number):
	result = 1
	#while number > 0:
	for x in range(1, number + 1):
		#result = result * number
		result = result * x
		#number = number - 1
	return result
	
in_variable = input("Enter a number to calculate the factorial of: ")
print factorial(in_variable)	
