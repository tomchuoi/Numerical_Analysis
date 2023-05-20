import numpy as np

n = int(input('Nhập số ẩn: '))

a = np.zeros((n, n+1))

print('Điền hệ số của hệ phương trình:')
for i in range(n):
    row = input().split()
    for j in range(n+1):
        a[i][j] = float(row[j])

print('\nPhương trình dưới dạng ma trận:')
print(a)

# Thuật khử Gauss
for i in range(n):
    # Đổi hàng nếu cột bằng 0
    if a[i][i] == 0:
        for j in range(i+1, n):
            if a[j][i] != 0:
                a[[i,j]] = a[[j,i]]
                break
        else:
            if a[i][n] != 0:
                print('Hệ phương trình vô nghiệm')
                exit()
            else:
                print('Hệ phương trình vô số nghiệm')
                exit()

    # Biến đổi phần tử về 1
    a[i] = a[i]/a[i][i]

    # Biến các phần tử khác về o
    for j in range(n):
        if i != j:
            a[j] = a[j] - a[j][i]*a[i]

    if i == 0:
        print('\nBiến đổi ma trận đầu tiên:')
        print(a)

    elif i == n-1:
        print('\nBiến đổi ma trận cuối cùng:')
        print(a)


x = a[:,n]



print('\nNghiệm là: ')
for i in range(n):
    print('X%d = %0.3f' % (i, x[i]), end='\t')
