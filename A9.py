import numpy as np

a=np.array([4,1,8,0,5])
b=np.array([[3,6,9,1,5],[2,0,1,6,3]])
aa=a.reshape(1,5)
print(aa)
r=np.concatenate((aa,b))
print("Joined Array....\n",r)

#2)
a= np.array([[1, 2, 3],[4, 5, 6]])
flat = a.flatten()
print("Original:\n", a)
print("Flattened:\n", flat)

#3)
a= np.array([[1, 2, 3],[4, 5, 6]])
r = a[::-1]
print("Reversed array...\n",r)

#4)
a=np.array([[1,2,3],[6,7,8],[4,6,0],[2,3,2]])
print(a)
print("Minimum : ",a.min(),"\nMaximum : ",a.max())

rows = len(a)
cols = len(a[0])
print("Rows:", rows)
print("Columns:", cols)

s = 0
for row in a:
    for x in row:
        s = s + x
print("Sum...\n",s)

print(a[0][0])
print(a[1][2])
print(a[3][1])

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Add...\n",a + b)
print("Substract...\n",a - b)
print("Multiply...\n",a * b)
print("Divide...\n",a / b)

