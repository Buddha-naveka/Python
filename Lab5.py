'''Задана рекуррентная функция. Область определения функции – натуральные числа. Написать программу сравнительного вычисления данной функции рекурсивно и итерационно. 
Определить границы применимости рекурсивного и итерационного подхода. Результаты сравнительного исследования времени вычисления представить в табличной форме. 
Обязательное требование – минимизация времени выполнения и объема памяти.
3.	F(0) = 1; F(1) = 2; F(n) = (-1)^n*(F(n-1)/n! - 2F(n-2) /(2n)!)'''

import math
import timeit
perem, fact1, fact2 = 1 ,2, 2
while perem ==1:
    n = int(input('Введите n: '))
    choice = int(input('1.Рекурсивно \n2.Итерационно \n'))
    
    if choice ==1: 
        def factre(n): #Функция для вычисления факториала вместо неё используется функция библиотееки math
            if n == 1 or n == 0:
                factr = 1
            else:
                factr = n * factre(n-1)
            return factr   
        def Fr(n):
            if n == 0:
                return 1
            elif n == 1:
                return 2
            else:
                return (-1)**n * ((Fr(n-1)/math.factorial(n)) - 2*(Fr(n-2)) /math.factorial(2*n))
                #return (-1)**n * (Fr(n-1)/factre(n) - 2*Fr(n-2) /factre(2*n))

        a =timeit.timeit('Fr(n)', globals = globals(), number =1)
        print(f'Рекурсивно.Функция: {Fr(n)} \nВремя: {a}')
        
    elif choice ==2:
        def Fi(n, fact1,fact2):
            for i in range(0,n+1):
                if i == 0:
                    answer = 1
                    two = answer
                elif i == 1:
                    answer = 2
                    one = answer
                else:
                    fact2 = fact2 * (i*2) * ((i*2)-1)
                    answer = (-1)**i * (one/fact1 - 2*two /fact2)
                    two, one = one, answer
                    fact1 *=(i+1)            
            return answer

        a =timeit.timeit('Fi(n, fact1, fact2)', globals = globals(), number =1)
        print(f'Функция: {Fi(n, fact1,fact2)} \nВремя: {a}')
    perem = int(input('1.Продолжить \n2.Остановить \n'))




