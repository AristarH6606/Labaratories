import numpy as np

arr1=np.array([[1,2,3],
              [4,5,6]])
row_sums=np.sum(arr1, axis=1)
col_sums=np.sum(arr1, axis=0)
print(row_sums)
print(col_sums)