'''2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов)
и целевую функцию для нахождения оптимального  решения.
У няни 10 разных фруктов (ф1,…ф10). Сформировать (вывести) все возможные варианты меню полдника (1 фрукт) для ребенка на неделю.'''
import timeit
from itertools import permutations
g = -1
fruits =['Яблоко', 'Груша', 'Мандарин', 'Апельсин', 'Банан', 'Манго', 'Маракуя', 'Авакадо', 'Слива', 'Драк.фрукт',]

the_vowel = ['у','е','а','о','я','и','ю']
print(fruits)
for i in fruits:
    g +=1
    if i[0].lower() in the_vowel:
        fruits.pop(g)
print(fruits)
sugar = {0:9.9, 1:7.5, 2:2, 3:12, 4:13.7, 5:9.92, 6:13}
spisok = []
perem= 0
while perem !=3:
    perem = int(input('Выберите: \n1.Вывести все варианты \n2.Целевая функция \n3.Выйти \n'))
    if perem == 1:
        sum1 = (len(list(permutations(fruits,7))))
        b =list(permutations(fruits,7))
        print(b)
        a =timeit.timeit('b', globals = globals(), number =1)
        print(f"Время: {a}")
        print(f'Количеесвто вариантов: {sum1}')
    elif perem ==2:
        def fruit(fuits,spisok):
            min1, sum = 10000, 0
            h,  naim=[], []
            sum2  = 0
            for i in range(len(fruits)):
                for o in range(len(fruits)):
                    if o != i:
                        for p in range(len(fruits)):
                            if p != i and p!=o:
                                for j in range(len(fruits)):
                                    if j != i and j!=o and j!=p:
                                        for k in range(len(fruits)):
                                            if k != i and k!=o and k!=p and k!=j:
                                                for l in range(len(fruits)):
                                                    if l != i and l!=o and l!=p and l!=j and l!=k:
                                                        for m in range(len(fruits)):
                                                            if m != i and m!=o and m!=p and m!=j and m!=k and m!=l:
                                                                sum = 0
                                                                spisok.append(fruits[i]); sum += sugar[i] * 1 
                                                                spisok.append(fruits[o]); sum += sugar[o] * 2
                                                                spisok.append(fruits[p]); sum += sugar[p] * 3
                                                                spisok.append(fruits[j]); sum += sugar[j] * 4
                                                                spisok.append(fruits[k]); sum += sugar[k] * 5
                                                                spisok.append(fruits[l]); sum += sugar[l] * 6
                                                                spisok.append(fruits[m]); sum += sugar[m] * 7
                                                                #sum2 +=1
                                                                if sum < min1:
                                                                    naim =[]
                                                                    naim=spisok
                                                                    min1 = sum
                                                                #h.append(spisok)
                                                                spisok =[]
            #print(f'Количество вариантов: {sum2}')
            #print(f'Наименьшая комбинация: {naim}')
            print(f'Количество сахара: {sum}')
            return naim
        print(f'Комбинация с наименьшим количеством сахара{fruit(fruits,spisok)}')
    elif perem ==3:
        break

