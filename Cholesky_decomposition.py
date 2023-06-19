import numpy as np

def cholesky_decomposition(matrix):
    n = len(matrix)
    L = np.zeros((n, n))

    for i in range(n):
        for j in range(i+1):
            if i == j:
                L[i][j] = np.sqrt(matrix[i][i] - np.sum(L[i][:j]**2))
            else:
                L[i][j] = (matrix[i][j] - np.dot(L[i][:j], L[j][:j])) / L[j][j]

    return L

# Read matrix from input file
with open("input.txt", "r") as file:
    lines = file.readlines()

matrix = []
for line in lines:
    row = [float(x) for x in line.strip().split()]
    matrix.append(row)

# Convert matrix to NumPy array
A = np.array(matrix)

# Perform Cholesky decomposition
L = cholesky_decomposition(A)


print("Lower Triangular Matrix (L):")
print(L)

print("\nTranspose of Lower Triangular Matrix (L^T):")
print(L.T)
