# question-1
import numpy as np

vector = np.array([10, 11, 12, 13, 14])
no_consecutive_zeros = 5
new_vector = np.zeros(len(vector) + (len(vector)-1) * no_consecutive_zeros)
new_vector[0:len(new_vector): no_consecutive_zeros+1] = vector
print(new_vector)
