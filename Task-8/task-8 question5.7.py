from numpy import *
# 7.Getting the positions (indexes) where elements of 2 numpy arrays match
arr_1 = array([1,2,3])
arr_2 = array([5,6,3])
for i in range(0,len(arr_1)):
    if arr_1[i] == arr_2[i]:
        print(f"The position or index where elements of numpy arrays match is {i}")
