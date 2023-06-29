""""12.5(b)
Дан двумерный массив. Вывести на экран все элементы s-го столбца массива."""
import random

# import random
#
# lenX = int(input("enter your lenght X"))
# lenY = int(input("enter your lenght Y"))
#
# matrix = [[]] * lenX
#
# for index in range(lenX):
#     matrix[index] = [0] * lenY
#
# for index in range(lenX):
#     for index2 in range(lenY):
#         matrix[index][index2] = random.randint(10, 99)
#
# for index in range(lenX):
#     print(matrix[index])
#
# numberOfColumn = int(input())
#
# if numberOfColumn > lenY:
#     print("ERROR")
# else:
#     for index in range(lenX):
#         print(matrix[index][numberOfColumn - 1])


"""12.6(b)
Дан двумерный массив. Вывести на экран: все элементы m-й строки массива."""

# lenX = 3
# lenY = 4
#
# someMatrix = [[]] * lenX
#
# for index in range(lenX):
#     someMatrix[index] = [0]*lenY
#
# for index in range(lenX):
#     for index2 in range(lenY):
#         someMatrix[index][index2] = random.randint(1,9)
# for index in range(lenX):
#     print(someMatrix[index])
#
# someString = int(input("enter your number of the string"))
#
# if someString > lenX:
#     print("error")
# else:
#     print(someMatrix[someString-1])


""""12.16(a)Составить программу: расчета разности двух любых элементов двумерного массива"""

# import random
#
# lenX = 3
# lenY = 4
#
# someMatrix = [[]] * lenX
#
# for index in range(lenX):
#     someMatrix[index] = [0] * lenY
#
# for index in range(lenX):
#     for index2 in range(lenY):
#         someMatrix[index][index2] = random.randint(1,10)
#
# for index in range(lenX):
#     print(someMatrix[index])
# element = int(input("введите индекс в строке 1 числа\n"))
# element1 = int(input("введите индекс в столбике 1 числа x\n"))
# element2  = int(input("Эвведите индекс в строке 2 числа\n"))
# element3 = int(input("введите индекс в столбике 2 числа\n"))
#
# result = (someMatrix[element][element1]) -(someMatrix[element2][element3])
# print(f'Ваш ответ: {result}')


"""12.33(a)Дан двумерный массив. Вывести на экран:
все элементы пятого столбца массива, начиная с последнего элемента это-
го столбца;"""

# lenX = 4
# lenY = 5
#
# someMatrix = [[]] * lenX
#
# for index in range(lenX):
#     someMatrix[index] = [0] * lenY
#
# for index in range(lenX):
#     for index2 in range(lenY):
#         someMatrix[index][index2] = random.randint(10,99)
# for index in range(lenX):
#     print(someMatrix[index])
#
#
# column = 5
#
# for index in range(lenX):
#     print(someMatrix[index][column-1], end = " ")


"""12.62(a) Дан двумерный массив.
Найти: сумму элементов каждой строки;"""


# lenX = 3
# lenY = 4
#
# someMatrix = [[]] * lenX
#
# for index in range(lenX):
#     someMatrix[index] = [0] * lenY
#
# for index in range(lenX):
#     for index2 in range(lenY):
#         someMatrix[index][index2] = random.randint(1,99)
#
# for index in range(lenX):
#     print(someMatrix[index])
#
# result = someMatrix[0][0] + someMatrix[0][1] + someMatrix[0][2] + someMatrix[0][3]
# result1 = someMatrix[1][0] + someMatrix[1][1] + someMatrix[1][2] + someMatrix[1][3]
# result2 = someMatrix[2][0] + someMatrix[2][1] + someMatrix[2][2] + someMatrix[2][3]
#
# print(f'суммa элементов в каждой строке: {result}, {result1}, {result2}')


#12.90 """Дан двумерный массив. В каждой его строке найти:
#а) максимальный элемент;
#б) минимальный элемент;


# lenX =3
# lenY = 4
#
# someMatrix = [[]] * lenX
#
# for index in range(lenX):
#     someMatrix[index] = [0] * lenY
#
# for index in range(lenX):
#     for index2 in range(lenY):
#         someMatrix[index][index2]=random.randint(1,10)
#
# for index in range(lenX):
#     print(someMatrix[index])
#
# for index in range(lenX):
#     print(f'максимальные символы: {max(someMatrix[index])}')
# for index in range(lenX):
#     print(f'минимальные символы: {min(someMatrix[index])}')
