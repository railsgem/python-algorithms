# Original List: [0, 3, 9, 4, 1, 9]
# i= 0
#     j= 1
#     j= 2
#     j= 3
#     j= 4
#     j= 5
#     ary[min],ary[i]: 0 0     ary[i],ary[min]: 0 0
#          [0, 3, 9, 4, 1, 9]
# i= 1
#     j= 2
#     j= 3
#     j= 4
#         ary[j] < ary[min]: 1 3
#         min:ary[ 4 ] =  1
#           [0, 3, 9, 4, 1, 9]
#           [0, 0, 0, 0, 1, 0]
#     j= 5
#     ary[min],ary[i]: 1 3     ary[i],ary[min]: 3 1
#          [0, 1, 9, 4, 3, 9]
# i= 2
#     j= 3
#         ary[j] < ary[min]: 4 9
#         min:ary[ 3 ] =  4
#           [0, 1, 9, 4, 3, 9]
#           [0, 0, 0, 1, 1, 0]
#     j= 4
#         ary[j] < ary[min]: 3 4
#         min:ary[ 4 ] =  3
#           [0, 1, 9, 4, 3, 9]
#           [0, 0, 0, 1, 1, 0]
#     j= 5
#     ary[min],ary[i]: 3 9     ary[i],ary[min]: 9 3
#          [0, 1, 3, 4, 9, 9]
# i= 3
#     j= 4
#     j= 5
#     ary[min],ary[i]: 4 4     ary[i],ary[min]: 4 4
#          [0, 1, 3, 4, 9, 9]
# i= 4
#     j= 5
#     ary[min],ary[i]: 9 9     ary[i],ary[min]: 9 9
#          [0, 1, 3, 4, 9, 9]
# i= 5
#     ary[min],ary[i]: 9 9     ary[i],ary[min]: 9 9
#          [0, 1, 3, 4, 9, 9]
         
def select_sort(ary):
    #position = [1]
    # print("position:", position)
    # position.extend([0] * 3)
    # print("position:", position)
    
    n = len(ary)
    print("Original List:", ary)
    position = []
    position.extend([0] * n)
    for i in range(0,n):
        print("i=", i)
        min = i
        for j in range(i+1,n):
            print("    j=",j)
            if ary[j] < ary[min]:
                print("        ary[j] < ary[min]:", ary[j], ary[min])
                min = j
                print("        min:ary[", min, "] = ", ary[min])
                position[min] = 1
                print("         ",ary)
                print("         ", position)
        print("    ary[min],ary[i]:",ary[min],ary[i],"    ary[i],ary[min]:",ary[i],ary[min])
        ary[min],ary[i] = ary[i],ary[min]
        print("        ",ary)
    return ary

L = [0, 3, 9, 4, 1, 9]
select_sort(L)
