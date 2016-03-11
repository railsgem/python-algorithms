
# [0, 3, 9, 4, 1, 9]
# Begin:
# i= 0
# 	j= 1
# 		array[j-1] - array[j]: [ 0  -  3 ]
# 			 [0, 3, 9, 4, 1, 9]
# 	j= 2
# 		array[j-1] - array[j]: [ 3  -  9 ]
# 			 [0, 3, 9, 4, 1, 9]
# 	j= 3
# 		array[j-1] - array[j]: [ 9  -  4 ]
# 		**swap!
# 			 [0, 3, 4, 9, 1, 9]
# 	j= 4
# 		array[j-1] - array[j]: [ 9  -  1 ]
# 		**swap!
# 			 [0, 3, 4, 1, 9, 9]
# 	j= 5
# 		array[j-1] - array[j]: [ 9  -  9 ]
# 			 [0, 3, 4, 1, 9, 9]
# i= 1
# 	j= 1
# 		array[j-1] - array[j]: [ 0  -  3 ]
# 			 [0, 3, 4, 1, 9, 9]
# 	j= 2
# 		array[j-1] - array[j]: [ 3  -  4 ]
# 			 [0, 3, 4, 1, 9, 9]
# 	j= 3
# 		array[j-1] - array[j]: [ 4  -  1 ]
# 		**swap!
# 			 [0, 3, 1, 4, 9, 9]
# 	j= 4
# 		array[j-1] - array[j]: [ 4  -  9 ]
# 			 [0, 3, 1, 4, 9, 9]
# i= 2
# 	j= 1
# 		array[j-1] - array[j]: [ 0  -  3 ]
# 			 [0, 3, 1, 4, 9, 9]
# 	j= 2
# 		array[j-1] - array[j]: [ 3  -  1 ]
# 		**swap!
# 			 [0, 1, 3, 4, 9, 9]
# 	j= 3
# 		array[j-1] - array[j]: [ 3  -  4 ]
# 			 [0, 1, 3, 4, 9, 9]
# i= 3
# 	j= 1
# 		array[j-1] - array[j]: [ 0  -  1 ]
# 			 [0, 1, 3, 4, 9, 9]
# 	j= 2
# 		array[j-1] - array[j]: [ 1  -  3 ]
# 			 [0, 1, 3, 4, 9, 9]
# i= 4
# 	j= 1
# 		array[j-1] - array[j]: [ 0  -  1 ]
# 			 [0, 1, 3, 4, 9, 9]
# i= 5
# Sorted:	 [0, 1, 3, 4, 9, 9]

def bubble_sort(array):
	n = len(array)	#get array length

	print("Begin:")
	for i in range(n):
		print("i=",i)
		for j in range(1,n-i):
			print("	j=",j)
			print("		array[j-1] - array[j]:","[",array[j-1]," - ",array[j],"]")
			if array[j-1] > array[j]:
				array[j-1],array[j] = array[j],array[j-1]
				print("		**swap!")
			print("			",array)
	return array


L = [0, 3, 9, 4, 1, 9]
print(L)

sort_L = bubble_sort(L)
print("Sorted:	",sort_L)

