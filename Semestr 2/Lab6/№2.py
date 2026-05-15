import numpy as np

arr1=np.array([10,20,30,40,50])
arr2=np.array([1,2,3,4,5,6])

print("Сумма arr1:", np.sum(arr1))
print("Среднее arr1:", np.mean(arr1))
print("Мин arr1", np.min(arr1))
print('Макс arr1:', np.max(arr1))
print("Стд отклонение arr1:", np.std(arr1))

print('Сумма arr2',np.sum(arr2))
print('Среднее arr2',np.mean(arr2))
print('Мин arr2',np.min(arr2))
print('Макс arr2',np.max(arr2))
print('Стд отклонение arr2',np.std(arr2))

arr3=np.array([1,2,3,4,5,6])
arr4=np.array([1,2,3,4,5,6])
print(arr3+arr4)
print(arr3*4)