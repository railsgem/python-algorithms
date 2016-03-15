count_of_zero, count_of_2, count_of_5 = 0 ,0 ,0

for i in range(1, 1001):
	if i % 2 == 0:
		count_of_2 = count_of_2 + 1
	if i % 5 == 0:
		count_of_5 = count_of_5 + 1

#print("count_of_2 = ",count_of_2)
#print("count_of_5 = ",count_of_5)

if count_of_2 > count_of_5:
	count_of_zero = int(count_of_5 / 2)
else:
	count_of_zero = int(count_of_2 / 2)

#print("count_of_zero = ", count_of_zero)
print("There are {} trailing 0s in 1000!".format(count_of_zero))
