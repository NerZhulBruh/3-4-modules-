import numpy as np

#Создать массив из 25 нулей
zeros = np.zeros(25)
zeros1 = [0] * 25
print(zeros)
print(zeros1)

#Создать массив из 10 единиц
ones = np.ones(10)
ones1 = [1]*10
print(ones)
print(ones1)

#Создать массив из 12 пятерок
fives = np.full(12, 5)
fives1 = [5 for i in range(10)]
print(fives)
print(fives1)


#Создать массив из целых чисел от 12 до 51
Z = np.arange(12, 52)
z1 = [i for i in range(12, 52)]
print(Z)
print(z1)

#Создать массив из целых четных чисел от 12 до 51
z_even = np.arange(12, 52, 2)
z_even1= [i for i in range(12,52) if i % 2 == 0]
print(z_even)
print(z_even1)

#Создать матрицу 3х3 с числами от 1 до 9
mat1 = np.arange(1, 10).reshape(3, 3)
mat2 = [[i for i in range(1, 4)], [i for i in range (4, 7)], [i for i in range(7, 10)]]
print(mat1)
print(mat2)

#Создать единичную матрицу 5х5
matr = np.eye(5, 5)
matr1 = [[1 for i in range(5)] for i in range(5)]
print(matr)
print(matr1)

#Матрица от 0.1 до 1 
m = np.arange(0.01, 1.01, 0.01).reshape(10, 10)
m1 = [[0.01 * j + 0.1 * i for j in range(1, 11)] for i in range(10)]
print(m)
print(m1)

#Матрица от1 до 26
M = np.arange(1, 26).reshape(5, 5)
M1 = [[j + 1 + i * 5 for j in range(5)] for i in range(5)]
print(M)
print(M1)

# Извлечь подматрицу из 9 задания
UndM = M[1:, 3:]
print(UndM)

#Извлечь число 15 из 9го задания
num15 = M[2, 4]
print(num15)
