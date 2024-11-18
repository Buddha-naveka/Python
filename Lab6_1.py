'''Задание состоит из двух частей. 
1 часть – написать программу в соответствии со своим вариантом задания.
Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
 У няни 10 разных фруктов (ф1,…ф10). Сформировать (вывести) все возможные варианты меню полдника (1 фрукт) для ребенка на неделю.'''

import timeit
from itertools import permutations
fruits =['Яблоко', 'Груша', 'Мандарин', 'Апельсин', 'Банан', 'Манго', 'Маракуя', 'Авакадо', 'Дуриан', 'Драк.фрукт',]
spisok = []
perem = 0
while perem !=3:
    perem = int(input('Выберите: \n1.С помощью функций \n2.Алгоритмически \n3.Выйти \n'))
    if perem == 1:
        #print(len(list(permutations(d,7))))
        b =list(permutations(fruits,7))
        print(b)
        a =timeit.timeit('b', globals = globals(), number =1)
        print(f"Время: {a}")
    elif perem ==2:
        def fruit(fuits,spisok):
            h =[]
            for i in fruits:
                for o in fruits:
                    if o != i:
                        for p in fruits:
                            if p != i and p!=o:
                                for j in fruits:
                                    if j != i and j!=o and j!=p:
                                        for k in fruits:
                                            if k != i and k!=o and k!=p and k!=j:
                                                for l in fruits:
                                                    if l != i and l!=o and l!=p and l!=j and l!=k:
                                                        for m in fruits:
                                                            if m != i and m!=o and m!=p and m!=j and m!=k and m!=l:
                                                                spisok.append(i)
                                                                spisok.append(o)
                                                                spisok.append(p)
                                                                spisok.append(j)
                                                                spisok.append(k)
                                                                spisok.append(l)
                                                                spisok.append(m)
                                                                h.append(spisok)
                                                                spisok =[]
            return h
        print(fruit(fruits,spisok))
        n =timeit.timeit('fruit(fruits,spisok)', globals = globals(), number =1)
        print(f"Время: {n}")
    elif perem ==3:
        break
