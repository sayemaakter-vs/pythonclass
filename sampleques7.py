import numpy as np

marks = np.array([72, 85, 49, 90, 67, 55, 38, 76, 81, 60, 45, 88])

print("Number of dimensions:", marks.ndim)
print("Shape:", marks.shape)
print("Data type:", marks.dtype)

print("Mean:", np.mean(marks))
print("Maximum:", np.max(marks))
print("Minimum:", np.min(marks))
print("Standard deviation:", np.std(marks))

passed_marks = marks[marks >= 60]
print("Marks greater than or equal to 60:", passed_marks)

below_50 = np.sum(marks < 50)
print("Number of marks below 50:", below_50)

matrix = marks.reshape(3, 4)
print("3 x 4 Matrix:")
print(matrix)

print("Sum of each row:", np.sum(matrix, axis=1))