import numpy as np
import pandas as pd

# Đọc dữ liệu từ file input
data = np.loadtxt("input.txt") #Enter the input.txt file's path here

# In hệ phương trình dưới dạng ma trận
print("Phương trình dưới dạng ma trận:\n", data)

# Phép khử Gauss-Jordan
n = len(data)
for i in range(n):
    divisor = data[i][i]
    data[i] = data[i] / divisor
    
    # Trừ hàng i với các hàng khác để biến đổi các phần tử cột i về 0
    for j in range(n):
        if i != j:
            multiplier = data[j][i]
            data[j] = data[j] - multiplier * data[i]

# In ma trận đã được biến đổi
print("Biến đổi ma trận cuối cùng:\n", data)

# Kiểm tra xem có nghiệm hay không
has_solution = True
for i in range(n):
    if data[i][i] == 0:
        has_solution = False
        break
if not has_solution:
    print("Nghiệm của hệ phương trình: Vô nghiệm")
else:
    # In nghiệm
    solution = [data[i][-1] for i in range(n)]
    print("Nghiệm của hệ phương trình:\n", "X =", solution)
