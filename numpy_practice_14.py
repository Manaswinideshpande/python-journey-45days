# numpy practice file 
import numpy as np

list_1 = [1,2,3,45,6,78,3,4]
arr1 = np.array(list_1)
print(arr1)
print(type(arr1))
print(arr1.shape)
print(arr1.ndim)


print(arr1.dtype)
print(np.arange(1,50))


b = np.arange(1,50,2)
print(b)
print(np.eye(9,dtype = int))

c = np.zeros((9,3),dtype ='int')
print(c)

d = np.ones((5,3),dtype ='int')
print(d)

print(np.diag(list_1 ))



n = arr1.reshape((4,2))
n2 = arr1.reshape((2,4))
n3 = arr1.reshape((1,8))
print(n,n2,n3)