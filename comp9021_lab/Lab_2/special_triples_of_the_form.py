# Write a program that finds all triples of consecutive positive three-digit integers each of which is
# the sum of two squares, that is, all triples of the form (n, n + 1, n + 2) such that:
# • n, n + 1 and n + 2 are integers at least equal to 100 and at most equal to 999;
# • each of n, n + 1 and n + 2 is of the form a2 + b2.
# Hint: As we are not constrained by memory space for this problem, we might use a list that stores
# an integer for all indexes n in [100, 999], equal to 1 in case n is the sum of two squares, and to 0
# otherwise. Then it is just a matter of finding three consecutive 1’s in the list. This idea can be
# refined (by not storing 1s, but suitable nonzero values) to not only know that some number is of
# the form a2 + b2, but also know such a pair (a, b). . .
# The output of the program could be:
# (144, 145, 146) (equal to (0^2+12^2, 8^2+9^2, 5^2+11^2)) is a solution.
# (232, 233, 234) (equal to (6^2+14^2, 8^2+13^2, 3^2+15^2)) is a solution.
# (288, 289, 290) (equal to (12^2+12^2, 8^2+15^2, 11^2+13^2)) is a solution.
# (360, 361, 362) (equal to (6^2+18^2, 0^2+19^2, 1^2+19^2)) is a solution.
# (520, 521, 522) (equal to (14^2+18^2, 11^2+20^2, 9^2+21^2)) is a solution.
# (576, 577, 578) (equal to (0^2+24^2, 1^2+24^2, 17^2+17^2)) is a solution.
# (584, 585, 586) (equal to (10^2+22^2, 12^2+21^2, 15^2+19^2)) is a solution.
# (800, 801, 802) (equal to (20^2+20^2, 15^2+24^2, 19^2+21^2)) is a solution.
# (808, 809, 810) (equal to (18^2+22^2, 5^2+28^2, 9^2+27^2)) is a solution.
# 
# 
# 

sum_of_two_squares = [None] * 1000
# a^2 + b^2 = c^2; 
# a, b < c
# 
max = 31

for i in range(max + 1):
	for j in range(max + 1):
		n = i * i + j * j
		if n < 1000:
			sum_of_two_squares[n] = i,j

#print(sum_of_two_squares)

for n in range(100,1000):
	if sum_of_two_squares[n] != None and sum_of_two_squares[n+1] != None and sum_of_two_squares[n+2] != None:
		print("({}, {}, {}) (equal to ({}^2+{}^2, {}^2+{}^2, {}^2+{}^2)) is a solution.".format(n, n+1, n+2,sum_of_two_squares[n][0],sum_of_two_squares[n][1],sum_of_two_squares[n+1][0],sum_of_two_squares[n+1][1],sum_of_two_squares[n+2][0],sum_of_two_squares[n+2][1]))
		