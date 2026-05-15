import numpy as np
arr1 = np.array([10,20,30,40,50])
arr2 = np.array([[1,2,3],[4,5,6]])

print(arr1.ndim, arr1.shape, arr1.dtype,arr1.size)
print(arr2.ndim, arr2.shape, arr2.dtype,arr2.size)

print(arr1[0])
print(arr1[1:4])
print(arr2[0])
print(arr2[1:4])
