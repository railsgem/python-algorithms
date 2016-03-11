# A number is perfect if it is equal to the sum of its divisors, itself excluded. For instance, the divisors
# of 28 distinct from 28 are 1, 2, 4, 7 and 14, and 1 + 2 + 4 + 7 + 14 = 28, hence 28 is perfect.
# Write a program that outputs all 3-digit perfect numbers. There is actually a unique solution. The output of the program should be of the form:
# ... is a solution.
# Auth : Juno Chen

# define a range of numbers
min_number = 100
max_number = 999

def check_perfect_number(number):
	"""Print out the number if it is a perfect number.
	"""
	# find the number's divisors for 1 to number(not include number itself)
	divisors = []
	for divisor in range(1,int(number/2)+1):
		if number % divisor == 0:
			divisors.append(divisor)
	# if the sum of divisors equals to the number, the number is perfect.
	if sum(divisors) == number:
		#print(divisors)
		print('{} is a solution.'.format(number))

for number in range(min_number, max_number+1):
	check_perfect_number(number)