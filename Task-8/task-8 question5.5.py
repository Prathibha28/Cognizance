from numpy import *
# 5.Array re-dimensioning
arr_1d = array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(f"array of 1d dimension {arr_1d.ndim}")
print(f"array of 1d {arr_1d}")
arr_2d = resize(arr_1d, (3, 4))
print(f"array of 2d \n {arr_2d}")
print(f"array of 2d dimension {arr_2d.ndim}")
arr_3d = resize(arr_1d, (2, 3, 2))
print(f"array of 3d \n {arr_3d}")
print(f"array of 3d dimension {arr_3d.ndim}")
