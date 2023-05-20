import numpy as np

#Enter the input.txt file's path here
with open('input.txt', 'r') as f: 
    input_data = f.read()

# Splitting input data by blank lines to get separate systems of equations
systems = input_data.split('\n\n')

for i, system in enumerate(systems):
    print(f'System {i+1}:')
    # Splitting each system by newlines to get individual equations
    equations = system.strip().split('\n')
    n = len(equations)
    
    # Creating a numpy array of size n x (n+1) to store augmented matrix
    a = np.zeros((n, n+1))

    for j in range(n):
        row = equations[j].split()
        for k in range(n+1):
            a[j][k] = float(row[k])

    print('\nPhương trình dưới dạng ma trận:')
    print(a)

    # Thuật khử Gauss
    for j in range(n):
        # Đổi hàng nếu cột bằng 0
        if a[j][j] == 0:
            for k in range(j+1, n):
                if a[k][j] != 0:
                    a[[j,k]] = a[[k,j]]
                    break
            else:
                if a[j][n] != 0:
                    print('Hệ phương trình vô nghiệm')
                    exit()
                else:
                    print('Hệ phương trình vô số nghiệm')
                    exit()

        # Biến đổi phần tử về 1
        a[j] = a[j]/a[j][j]

        # Biến các phần tử khác về o
        for k in range(n):
            if j != k:
                a[k] = a[k] - a[k][j]*a[j]

        if j == 0:
            print('\nBiến đổi ma trận đầu tiên:')
            print(a)

        elif j == n-1:
            print('\nBiến đổi ma trận cuối cùng:')
            print(a)



    x = a[:,n]


    print('\nNghiệm là: ')
    for j in range(n):
        print('X%d = %0.3f' % (j, x[j]), end='\t')
