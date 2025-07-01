import numpy as np
#1)
a=np.array([2,8,6,3,5,9])
print("Ans 1 Array : \n",a)

a=np.empty((4,2))
print("Empty Array : \n",a)
a=np.full((4,2),'*')
print("Full Array : \n",a)

a=np.zeros((3,5))
print("Zeros Array : \n",a)
a=np.ones((4,3,2))
print("\n Ones Array : \n",a)

#2)
a=np.arange(2,11).reshape(3,3)
print("\n Ans 2 Array...\n",a)

#3)
v=np.zeros(10)
print(v)
v[5]=11
print("Updated : \n",v)

#4)
a=np.array([90,20,40,100,30])
print("Reverse....")
print(np.flip(a))

#5)
a= np.array([1, 2, 3, 4, 5])
fa= np.array(a, dtype=float)
print("Float Array... \n",fa)
