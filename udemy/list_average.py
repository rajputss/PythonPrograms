def average(a):
	result = 0
	for x in a:
		result = result + x
	return result / len(a)

numbers = [1, 2, 3, 4, 5]

print average(numbers)