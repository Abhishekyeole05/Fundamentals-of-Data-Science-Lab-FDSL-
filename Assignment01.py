import numpy as np


array1 = np.array([1,2,3,4], dtype= np.int64)
print("1D Array")
print(array1)
print("\n")

array2 = np.array([[1,2,3,4],[1,2,3,4]],dtype =np.int64)
print("2D Array")
print(array2)
print("\n")


array3 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]],dtype=np.int64)
print("3D Array")
print(array3)
print("\n")

print(array1.data)
print(array2.data)
print(array3.shape)
print(array1.dtype)
print(array2.strides) 