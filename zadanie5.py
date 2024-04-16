def are_columns_linearly_dependent(matrix):
    # Создаем матрицу, состоящую из столбцов исходной матрицы
    column_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    # Вычисляем определитель этой матрицы
    determinant = det(column_matrix)
    # Если определитель равен нулю, столбцы линейно зависимы
    if determinant == 0:
        return True
    else:
        return False

# Функция для вычисления определителя матрицы
def det(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        determinant = 0
        for j in range(n):
            submatrix = [row[:j] + row[j+1:] for row in matrix[1:]]
            determinant += (-1) ** j * matrix[0][j] * det(submatrix)
        return determinant

# Пример матрицы
mat = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 80]
]

# Проверяем, являются ли столбцы линейно зависимыми
result = are_columns_linearly_dependent(mat)

# Выводим результат
if result:
    print("Столбцы матрицы линейно зависимы.")
else:
    print("Столбцы матрицы линейно независимы.")
print("Исходная матрица:")
for row in mat:
    print(row)