'''С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х 
равных по размерам подматриц, B,C,D,E заполняется случайным образом целыми 
числами в интервале [-10,10]. Для отладки использовать не случайное заполнение, а 
целенаправленное (ввод из файла и генератором). Вид матрицы А: 
В	Е
С	D
На основе матрицы А формируется матрица  F. По матрице F необходимо вывести не 
менее 3 разных графика. Программа должна использовать функции библиотек numpy  и 
matplotlib.

Формируется матрица F следующим образом: скопировать в нее А и если в С 
количество положительных элементов в четных столбцах больше, чем количество 
отрицательных  элементов в нечетных столбцах, то поменять местами В и С 
симметрично, иначе С и Е поменять местами несимметрично. При этом матрица А не 
меняется. После чего если определитель матрицы А больше суммы диагональных 
элементов матрицы F, то вычисляется выражение: A*AT – K * F^-1, иначе вычисляется 
выражение (A^-1 +G-F^-1)*K, где G-нижняя треугольная матрица, полученная из А. 
Выводятся по мере формирования А, F и все матричные операции последовательно.'''

import numpy as np
import matplotlib.pyplot as plt

#Заполнение матриц
N, K = int(input('Введите число N: ')), int(input('Введите число K: '))
perem = 0
perem2 = 0
while perem !=1:
    print('Заполненеи матрицы: \n1.Рандомно \n2.Из файла')
    output = int(input())
    if output == 1:
        A = np.random.randint(-10, 10, size=(N, N))
        print(f'Матрица А: \n{A}')
        perem = 1
    elif output ==2:
        file = open('test.txt', 'r')
        A = np.genfromtxt('test.txt', dtype = int, usecols = range(0, N), max_rows = N)
        file.close()
        print(f'Матрица А: \n{A}')
        perem = 1
    else:
        print('Такого варианта нет, попробуйте снова.')
perem =0
F = A.copy()

#Проверка областей и замена их
for i in range(N//2,N):
    for j in range(N//2):
            if j % 2 == 0 and F[i][j] > 0:
                perem +=1
            elif j % 2 == 1 and F[i][j]  < 0:
                 perem2 +=1
if perem > perem2:
    for i in range(N//2):
        for j in range(N//2):
            F[i][j], F[N -(i+1)][j] = F[N- (i+1)][j], F[i][j]
else:
    for j in range(N//2):
        for i in range(N//2,N):
            F[i][j], F[j][i] = F[j][i], F[i][j]


print(f'Матрица F: \n{F}')

# Математика
opr = round(np.linalg.det(A)) # Нахождение определителя
two_diag = np.fliplr(F) # Для нахождения суммы элементов побочной диагоняли
sum_diag = np.trace(F) + np.trace(two_diag) #сумма элементов диагоналей

if opr > sum_diag:
    AT = A.transpose() #Транспонирование 1.AAT = np.dot(A,AT) - перемножение 2.linalg.matrix_power() - возведенеи в степень
    Itog = np.dot(A,AT) - K * np.linalg.matrix_power(F,-1) #A*AT – K * F^-1
    print(f'Матрица Итоговая 1 вариант: \n{Itog}')
else:
    Itog = (np.linalg.matrix_power(A,-1) + np.tril(A) - np.linalg.matrix_power(F,-1)) * K #(A^-1 +G-F^-1)*K    np.tril(A)-получение нижней треугольной матрицы
    print(f'Матрица Итоговая 2 вариант: \n{Itog}')

plt.plot(F)
plt.show()

plt.matshow(F)
plt.show()

plt.scatter(F,F)
plt.show()



            