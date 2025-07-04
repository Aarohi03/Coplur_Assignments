import numpy as np
#1)
arr = np.array([[6,-8,73,-110],[np.nan,-8,0,94],[np.nan,6,45,3]])
newarr = np.nan_to_num(arr,copy=True,nan=11)
print(newarr)
arr[[0,1,2],:]=arr[[1,2,0],:]
print(arr)
arr[:,[1,2,0]]=arr[:,[2,0,1]]
print(arr)

#2)
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr)
new=arr.transpose()
print(new)

#3)
arr = np.array([
    [1, 2, np.nan],
    [4, np.nan, 6],
    [7, 8, 9]])
mean = np.nanmean(arr, axis=0)
nan_idx = np.where(np.isnan(arr))
arr[nan_idx] = mean[nan_idx[1]]

print("Replaced NaNs with column means:")
print(arr)

#4)
arr = np.array([[1, -2, 3], [-4, 5, -6]])
arr[arr < 0] = 0
print(arr)

#5)
a1 = np.array([[1, 2, 3], [4, 5, 6]])
a2 = np.array([[7, 8, 9], [10, 11, 12]])
a3 = np.concatenate((a1, a2), axis=0)
print(a3)
flat = a3.flatten()
print(np.mean(flat))
print(np.median(flat))

#6)

# x+3y-2z=9
# -x+3y-z=-6
# 2x-5y+5z=17

A = np.array([
    [1, 3, -2],
    [-1, 3, -1],
    [2, -5, 5]
])
B = np.array([9, -6, 17])
res = np.linalg.solve(A,B)
print(res)
A_1=np.linalg.inv(A)
res = np.dot(A_1,B)
print(res)

#7)
import matplotlib.pyplot as plt

subjects = ['Maths', 'Physics', 'Chemistry', 'CS', 'English']
sem1_marks = [85, 78, 92, 88, 76]
sem2_marks = [80, 82, 89, 91, 74]
plt.plot(subjects, sem1_marks, label='Semester 1', linestyle='--', marker='o', color='blue')
plt.plot(subjects, sem2_marks, label='Semester 2', linestyle='-.', marker='s', color='green')
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Semester Marks Comparison Using Line Styles")
plt.grid(True)
plt.legend()
plt.show()