import numpy as np

arr1=np.array([5,12,8,20,3,15])
mask= arr1>10
filtered=arr1[mask]
print(mask)
print(filtered)

