from numpy import *

arr1 = random.randint(0,2,6)
print("First array:")
print(arr1)
arr2 = random.randint(0,2,6)
print("Second array:")
print(arr2)
array_equal = allclose(arr1, arr2)
print(array_equal)
