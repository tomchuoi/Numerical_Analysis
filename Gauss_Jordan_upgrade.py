import numpy as np
import pandas as pd

# Read data from file
data = np.loadtxt("input.txt") #Enter the input.txt file's path here

# Print the system of linear equations
print("Phương trình dưới dạng ma trận:\n", data)

# Gauss-Jordan elimination
n = len(data)
for i in range(n):
    # Divide the ith row by the diagonal element
    divisor = data[i][i]
    data[i] = data[i] / divisor
    
    # Subtract the ith row from all other rows to make the other elements in the ith column equal to zero
    for j in range(n):
        if i != j:
            multiplier = data[j][i]
            data[j] = data[j] - multiplier * data[i]

# Print the transformed matrix
print("Biến đổi ma trận cuối cùng:\n", data)

# Check if the system has a solution or not
has_solution = True
for i in range(n):
    if data[i][i] == 0:
        has_solution = False
        break
if not has_solution:
    print("Nghiệm của hệ phương trình: Vô nghiệm")
else:
    # Print the solution
    solution = [data[i][-1] for i in range(n)]
    print("Nghiệm của hệ phương trình:\n", "X =", solution)
