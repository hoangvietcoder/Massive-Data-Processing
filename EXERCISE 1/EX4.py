import numpy as np

# The multiplication of two given matrix's.
m1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = np.array([[1, 1], [1, 0], [0, 1]])
m_result = np.dot(m1, m2)
print("The multiplication of two given matrix's: \n", m_result)

# The outer product of two given vectors.
p_1 = [[1, 2], [3, 4]]
q_1 = [[1, 1], [0, 0]]
result = np.outer(p_1, q_1)
print("\nThe outer product of two given vectors: \n", result)

# The cross product of two given vectors
p_2 = p_1 = [[1, 2], [3, 4]]
q_2 = [[1, 0], [0, 1]]
result_1 = np.cross(p_2, q_2)
result_2 = np.cross(q_2, p_2)
print("\nThe cross product of two given vectors: \n", result_1, result_2)

# The determinant of a given square array.
matrix = np.array([[1, 0], [0, 1]])
result_3 = np.linalg.det(matrix)
print("\nThe determinant of a given square array:\n", result_3)

# The determinant of an array
a = np.array([[1, 2], [2, 1]])
result_4 = np.linalg.det(a)
print("\nThe determinant of an array:\n", result_4)

# The inner product of vectors for 1-D arrays (without complex conjugation) and in higher dimension
matrix_1 = np.array([1, 2, 3])
matrix_2 = np.array([4, 5, 6])
result_5 = np.inner(matrix_1, matrix_2)
print("\nThe inner product of vectors for 1-D arrays (without complex conjugation) and in higher dimension:\n",
      result_5)
