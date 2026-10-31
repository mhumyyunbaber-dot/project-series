import numpy as np

a=[1,2,3,4,5,5.6]
arr=np.array(a)

print("List",a)
print("array",arr)

l1=[1,2,3]
l2=[4,5,6]
l3=[7,8,9]

arr=np.array([l1,l2,l3])
print("array",arr)
print(arr.ndim)
print(arr.shape)
print(arr.dtype)

text="Humayun Babar"

arr=np.fromiter(text,dtype="U2")

print(arr)

arr=np.arange(1,20,2,dtype=np.float32)
print(arr)

arr=np.linspace(3.5,20,4,dtype=np.int32)
arr=np.empty((5,6),dtype=np.int64)
arr=np.ones((3,3),dtype=np.int64)

a0=np.ones((3,2),dtype=np.int64)
a1=np.zeros((3,3),dtype=np.int32)
a2=np.linspace(1,15,9,dtype=np.int32)
a3=np.arange(1,20,2,dtype=np.float32)
print("ones",a0)
print("zeros",a1)
print("linespace",a2)
print("arange",a3)

arr=np.random.rand(2,3)
arr=np.random.randint(1,10,(3,3))
arr=np.eye(3,3)
arr1=np.diag([1,2,3])
arr2=np.ones_like(arr1)
arr3=np.zeros_like(arr1)
print(arr)
print(arr1)
print(arr2)
print(arr3)