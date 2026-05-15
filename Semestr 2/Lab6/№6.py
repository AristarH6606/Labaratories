import numpy as np

arr=np.array([40,10,30,20])

sorted_arr=np.sort(arr)
idx_max=np.argmax(arr)
print(idx_max)
print(arr[idx_max])