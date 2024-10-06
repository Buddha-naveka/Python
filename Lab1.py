"""С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N) заполняется случайным 
образом целыми числами в интервале [-10,10]. Для тестирования использовать не случайное 
заполнение, а целенаправленное, введенное из файла. Условно матрица имеет вид:
 2
1 3
 4
Формируется матрица F следующим образом: Скопировать в нее матрицу А и если 
нулевых элементов в нечетных столбцах в области 4 больше, чем количество 
отрицательных  элементов в четных строках в области 1, то поменять симметрично 
области 4 и 3 местами, иначе 1 и 2 поменять местами несимметрично. При этом матрица А 
не меняется. После чего вычисляется выражение: ((F+A)– (K * F) )*AT . Выводятся по мере 
формирования А, F и все матричные операции последовательно."""

import random

#//////////////НЕОБХОДИМЫЕ ФУНКЦИИ///////////////
def Print_matrix():
    print('\nВаша матрица А: \n')
    for i in range(Size_matrix):
        for j in range(Size_matrix):
           print(a[i][j], end =' ')           
        print("\n")  
     
    print('\nВаша матрица F: \n')
    for i in range(Size_matrix):
        for j in range(Size_matrix):
           print(f[i][j], end =' ')           
        print("\n") 
#//////////////////////////////////////////////

#Задаются начальные значения
a, f, result, copy = [], [], [], []
perem, perem2 = 0, 0
k = int(input('Введите число k: '))
while perem !=1:
    Size_matrix = int(input('Введите число строк и столбцов (число от 3 и до 100): '))
    if Size_matrix <3 or Size_matrix >99:
        print('Вы ввели некоректное число, попробуйте снова.')
    else:
        perem +=1
perem = 0

#Создание матрицы, заполненнst нулями
a=[[0] * Size_matrix for _ in range(Size_matrix)]

f=[[0] * Size_matrix for _ in range(Size_matrix)]
        
result=[[0] * Size_matrix for _ in range(Size_matrix)]

copy=[[0] * Size_matrix for _ in range(Size_matrix)]

#Вывод матриц
#Print_matrix()

#Заполнение матрицы А
print("Выберете как вы хотите заполнять матрицу: \n 1.Рандомно \n 2.Через Файл")
while perem !=1:
    output =int(input())
    if output == 1:
        for i in range(Size_matrix):
            for j in range(Size_matrix):
                a[i][j] = random.randint(-5,5)
        perem+=1
    elif output ==2:
        file = open("test.txt", "r") 
        for i in range(Size_matrix):
            stroka = file.readline().split()
            for j in range(Size_matrix):
                a[i][j] = int(stroka[j])
        file.close()
        perem +=1
    else:
        print('Некорректные данные.Попробуйте ввести число снова: ')
perem = 0

#Копирование матрицы А в F
for i in range(Size_matrix):
    for j in range(Size_matrix):
        f[i][j] = a[i][j]

#Вывод матриц
Print_matrix()

#Проверка 4 области
for i in range(Size_matrix//2, Size_matrix):
    for j in range(Size_matrix//2, i):
        if j % 2 != 0:
            if f[i][j] == 0:
                perem +=1
            else:
                continue
        else:
            continue

for i in range(Size_matrix-1, Size_matrix//2,-1):
    for j in range(Size_matrix-i, Size_matrix//2):
        if j % 2 != 0:
            if f[i][j] == 0:
                perem +=1
            else:
                continue
        else:
            continue


#Проверка 1 области
for i in range(Size_matrix//2):
    for j in range(i):
        if j % 2 ==0:
            if a[i][j] < 0:
                perem2 +=1
            else:
                continue
        else:
            continue

for i in range(Size_matrix//2, Size_matrix):
    for j in range(Size_matrix -(i+1)):
        if j % 2 ==0:
            if a[i][j] < 0:
                perem2 +=1
            else:
                continue
        else:
            continue


#Симметрия  и Несимметрия
if perem > perem2:
    for i in range(Size_matrix):
        for j in range(Size_matrix):
            if j> Size_matrix - ( i+1 ) and j> i:
                f[i][j], f[j][i] = f[j][i], f[i][j]
else :
    for i in range(Size_matrix):
        for j in range(i):
            if j< Size_matrix -(i + 1):
                f[i][j], f[j][Size_matrix- (i + 1)] = f[j][Size_matrix-(i + 1)], f[i][j]

print('\nВаша матрица F: \n')
for i in range(Size_matrix):
    for j in range(Size_matrix):
        print(f[i][j], end =' ')           
    print("\n") 


#Математические операции: 
#Сложение
for i in range(Size_matrix):
    for j in range(Size_matrix):
        result[i][j] = f[i][j] + a[i][j]

print('\nМатрица F + A: \n')
for i in range(Size_matrix):
    for j in range(Size_matrix):
        print(result[i][j], end =' ')           
    print("\n") 

#AT
for i in range(Size_matrix):
    for j in range(Size_matrix):
        copy[i][j] = a[i][j]

for i in range(Size_matrix):
    for j in range(Size_matrix):
        a[i][j] = copy[j][i]

print('\nAT: \n')
for i in range(Size_matrix):
    for j in range(Size_matrix):
        print(a[i][j], end =' ')           
    print("\n") 

#F*k
for i in range(Size_matrix):
    for j in range(Size_matrix):
        f[i][j] *=k

#(F+A) -F*k
for i in range(Size_matrix):
    for j in range(Size_matrix):
        result[i][j] -=f[i][j]

# ((F+A)– (K * F) )*AT
for i in range(Size_matrix):
    for j in range(Size_matrix):
        copy[i][j] = result[i][j]

result=[[0] * Size_matrix for _ in range(Size_matrix)]
for i in range(Size_matrix):
    for j in range(Size_matrix):
        for x in range(Size_matrix):
            result[i][j] += copy[i][x] * a[x][j]

print('\n((F+A)– (K * F) )*AT: \n')
for i in range(Size_matrix):
    for j in range(Size_matrix):
        print(result[i][j], end =' ')           
    print("\n") 