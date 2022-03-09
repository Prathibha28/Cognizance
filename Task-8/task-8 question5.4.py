from numpy import *
# 4.Array datatype conversion
arr = array([1.8, 2.2, 3.9,4.0])
print(f"Before changing type of arr {arr.dtype}")
array = arr.astype(int32)
print(f"After changing type of arr {array.dtype}")
