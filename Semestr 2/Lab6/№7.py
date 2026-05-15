import numpy as np

arr=np.array([1,2,3],dtype=np.int8)
print(arr.nbytes)

arr_float=arr.astype(np.float64)
print(arr_float.nbytes)