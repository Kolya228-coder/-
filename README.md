n = int(input())  # Считываем размерность матрицы
matrix = []

# Считываем саму матрицу
for k in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

numbers = [i for i in range(1, n ** 2 + 1)]  # Список чисел от 1 до n^2
matrix_numbers = []
for t in range(n):
    for g in range(n):
        matrix_numbers.append(matrix[t][g])

# Проверка, чтобы все числа от 1 до n^2 присутствовали в матрице
if sorted(matrix_numbers) != numbers:
    print("NO")
    exit()

# Эталонная сумма (сумма чисел в первой строке)
proverka = sum(matrix[0])

# Проверка суммы всех строк
for a in range(1, n):
    if sum(matrix[a]) != proverka:
        print("NO")
        exit()

# Проверка суммы всех столбцов
for b in range(n):
    col_sum = sum(matrix[a][b] for a in range(n))
    if col_sum != proverka:
        print("NO")
        exit()

# Проверка суммы главной диагонали
count = 0
for m in range(n):
    count += matrix[m][m]

# Проверка суммы побочной диагонали
count_2 = 0
for h in range(n):
    count_2 += matrix[h][n - 1 - h]

# Проверка диагоналей
if proverka == count and proverka == count_2:
    flag = True
else:
    flag = False

# Если все проверки пройдены
if flag:
    print('YES')
else:
    print('NO')
