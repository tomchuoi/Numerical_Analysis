# Thuật toán Gauss-Jordan
# Nhập ma trận
def GetMatrix():
    n = int(input("Nhập số ẩn: "))
    a = []
    for i in range(n):
        row = []
        for j in range(n + 1):
            row.append(float(input("Nhập a[" + str(i) + "][" + str(j) + "]: ")))
        a.append(row)
    return a, n

# Hàm in ma trận
def PrintMatrix(a, n):
    for i in range(n):
        print(a[i])


# Hàm này khử ma trận
def PerformOperation(a, n):
	i = 0
	j = 0
	k = 0
	c = 0
	flag = 0

	# Biến đổi phần tử
	for i in range(n):
		if (a[i][i] == 0):

			c = 1
			while ((i + c) < n and a[i + c][i] == 0):
				c += 1
			if ((i + c) == n):

				flag = 1
				break

			j = i
			for k in range(1 + n):

				temp = a[j][k]
				a[j][k] = a[j+c][k]
				a[j+c][k] = temp

		for j in range(n):

			# Xét i khác j
			if (i != j):
				
				p = a[j][i] / a[i][i]

				k = 0
				for k in range(n + 1):
					a[j][k] = a[j][k] - (a[i][k]) * p

	return flag

# Hàm in kết quả
def PrintResult(a, n, flag):

	print("Nghiệm của hệ phương trình : ")

	if (flag == 2):
		print("Vô số nghiệm")
	elif (flag == 3):
		print("Vô nghiệm")
	# Printing the solution by dividing constants by
	# their respective diagonal elements
	else:		
		for i in range(n):
			print(a[i][n] / a[i][i], end=" ")

# To check whether infinite solutions
# exists or no solution exists
def CheckConsistency(a, n, flag):

	# flag == 2 for infinite solution
	# flag == 3 for No solution
	flag = 3
	for i in range(n):
		sum = 0
		for j in range(n):
			sum = sum + a[i][j]
		if (sum == a[i][j]):
			flag = 2

	return flag

# Nhập ma trận
a, n = GetMatrix()

flag = 0

# Biến đổi ma trận
flag = PerformOperation(a, n)

if (flag == 1):
	flag = CheckConsistency(a, n, flag)

# In ra ma trận cuối
print("Biến đổi ma trận cuối cùng : ")
PrintMatrix(a, n)
print()

# In nghiệm nếu có
PrintResult(a, n, flag)


