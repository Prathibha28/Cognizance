import numpy as np
import pandas
dtype = [('ProductID',(np.str_,12)),('price',np.int32),('rating',np.float64)]
arr = pandas.read_csv('Dataset.csv').to_records(index=False)
structuredArr = np.array(arr,dtype=dtype)
print(structuredArr.dtype)
sort_Arr = np.sort(structuredArr,order='rating')
print(sort_Arr)
