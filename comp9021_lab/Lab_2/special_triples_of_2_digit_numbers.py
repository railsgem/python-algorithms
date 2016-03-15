# Write a program that finds all triples of positive integers (i, j, k) such that i, j and k are two digit
# numbers, i < j < k, every digit occurs at most once in i, j and k, and the product of i, j and k
# is a 6-digit number consisting precisely of the digits that occur in i, j and k. For instance, since
# 20 × 79 × 81 = 127980, (20, 79, 81) is a solution. The output of the program should consist of lines
# of the form:
# .. x .. x .. = ...... is a solution.
# 
# Writen by Ying Chen
#
i = []
j = []
k = []

def int_to_list(number):
	number_str = str(number)
	number_list = []
	for i in range(0,len(str(number)) ):
		number_list.append(int(number_str[i]))
	return number_list

def check_solution(first_digits,second_digits):
	i , j, k,six_digits_numbers = 0, 0, 0, 0 
	six_digits = []
	i = first_digits[0] * 10 + second_digits[0]
	j = first_digits[1] * 10 + second_digits[1]
	k = first_digits[2] * 10 + second_digits[2]
	six_digits_numbers = i * j * k
	six_digits = int_to_list(six_digits_numbers)
	#print("i , j, k",i,j,k)
	#print("six_digits",six_digits)
	count = 0
	for first_digit in first_digits:
		if first_digit in six_digits:
			count = count + 1
	for second_digit in second_digits:
		if second_digit in six_digits:
			count = count + 1
	if count == 6:
		print("{} x {} x {} = {} is a solution ".format(i,j,k,i*j*k),six_digits)

def find_second_digits(first_digits):
	digits = first_digits[:]
	for second_digit_of_i in range(0,10):
		if second_digit_of_i not in first_digits:
			#print("second_digit_of_i =",second_digit_of_i)
			for second_digit_of_j in range(0,10):
				if second_digit_of_j not in first_digits and second_digit_of_j != second_digit_of_i:
			#		print("	second_digit_of_j =",second_digit_of_j)
					for second_digit_of_k in range(0,10):
						if second_digit_of_k not in first_digits and second_digit_of_k != second_digit_of_i and second_digit_of_k != second_digit_of_j:
			#				print("		second_digit_of_k = ", second_digit_of_k)
							second_digits = []
							second_digits.append(second_digit_of_i)
							second_digits.append(second_digit_of_j)
							second_digits.append(second_digit_of_k)
							#print("first_digits = ",first_digits)
							#print("	second_digits = ",second_digits)
							# if 20 × 79 × 81 = 127980, (20, 79, 81) is a solution
							check_solution(first_digits,second_digits)
				#print("	")



# Hence i < j < k, and every digit occurs at most once in i, j ,k
# so, first_digit_of_i < first_digit_of_j < first_digit_of_k
# for example: i = 20 , j = 79, k = 81
# 	first_digit_of_i = 2 , first_digit_of_j = 7, first_digit_of_k = 8
# 	then, the second digit of i,j,k should not equal to 
# 			first_digit_of_i,first_digit_of_j,first_digit_of_k.
# 			
for first_digit_of_i in range(1,10):
	#print("first_digit_of_i = ", first_digit_of_i)
	for first_digit_of_j in range(first_digit_of_i + 1, 10):
		#print("	first_digit_of_j = ", first_digit_of_j)
		for first_digit_of_k in range(first_digit_of_j + 1, 10):
			#print("		first_digit_of_k = ", first_digit_of_k)
			# put first digits of i, j, k into first digits list
			first_digits = []
			first_digits.append(first_digit_of_i)
			first_digits.append(first_digit_of_j)
			first_digits.append(first_digit_of_k)
			#print("first_digits = ", first_digits)
			# find second digits
			find_second_digits(first_digits)
	





