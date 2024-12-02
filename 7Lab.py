import tkinter as tk
from tkinter.messagebox import showinfo
import timeit
from itertools import permutations


def click_button():

    shugar ={}

    def is_float(f):
        try:
            float(f)
            return True
        except ValueError:
            return False
    perem = 0
    fruits = []
    data_shugar = str(vvod1.get("1.0", "end"))
    probel_shugar = data_shugar.split()
    if len(probel_shugar) ==10:
        for i in range(len(probel_shugar)):
            f = probel_shugar[i]
            if is_float(f):
                f = float(f)
                shugar[i] = f
            else:
                perem = 1
                showinfo(title="Ошибка", message="Данные введены не корректно, запись должна содержать  ненцужных символов") 
    else:
        showinfo(title="Ошибка", message="Вы ввели не 10 чисел")
        perem =1
    print(shugar)
    if perem ==1:
        btn["state"] = ["active"]
        return


    data = str(vvod.get("1.0", "end"))
    probel = data.split()

    if len(probel) ==10:
        for i in range(len(probel)):
            f = probel[i]
            if f.isalpha() == False:
                btn["state"] = ["active"] 
                showinfo(title="Ошибка", message="Данные введены не корректно, запись должна содержать только буквы")          
                fruits = []
                break
            else:
                btn["state"] = ["disabled"]
                fruits.append(probel[i])
                if len(fruits) == 10:
                    window2 = tk.Tk()
                    window2.title('Ответ')
                    window2.geometry('500x450+650+200')
                    window2.configure(bg = '#4682B4')
                    t = tk.Text(window2)
                    t.place(x =60, y = 70, width= 400, height= 250)
                    scrollbar = tk.Scrollbar(window2,orient="vertical", command=t.yview)
                    scrollbar.place(x = 460, y = 70, height= 250)
                    #scrollbar.pack( side = 'right', fill='y' )

                    t["yscrollcommand"]=scrollbar.set
                    #-------------------------------------------------------------------------
                    min1, sum = 10000, 0
                    h, naim, spisok=[], [], []
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
                                                                        spisok.append(fruits[i]); sum += shugar[i] * 1 
                                                                        spisok.append(fruits[o]); sum += shugar[o] * 2
                                                                        spisok.append(fruits[p]); sum += shugar[p] * 3
                                                                        spisok.append(fruits[j]); sum += shugar[j] * 4
                                                                        spisok.append(fruits[k]); sum += shugar[k] * 5
                                                                        spisok.append(fruits[l]); sum += shugar[l] * 6
                                                                        spisok.append(fruits[m]); sum += shugar[m] * 7
                                                                        sum2 +=1
                                                                        if sum < min1:
                                                                            naim =[]
                                                                            naim=spisok
                                                                            min1 = sum
                                                                        h.append(spisok)
                                                                        spisok =[]

                    b =list(permutations(fruits,7))
                    a =timeit.timeit(lambda: list(permutations(fruits, 7)), globals = globals(), number =1)
                    tekst = f"Количиство комбинаций: {sum2} \nКомбинация с наименьшей сахарностью: {naim} \nЕё сахарность{sum} \nВремя: {a} \nНесколько вариантов комбинаций{b[:100]}"
                    #--------------------------------------------------------------------
                    
                    #t.insert("1.0", b[:100]) 
                    t.insert('end', tekst) 
                    window2.mainloop()
                    
    else:
            showinfo(title="Ошибка", message="Вы ввели не 10 фруктов")
    print(fruits)

window = tk.Tk()
window.title('7Lab')
window.geometry('600x550+650+200')
window.configure(bg = '#B0C4DE')
window.resizable(False,False)
text = tk.Label(text = 'Введите 10 фруктов: ',bg ='#5F9EA0', padx =10, pady =10, font=('Arial',14))
text1 = tk.Label(text = 'Введите сахорность фрутов(10 раз): ',bg ='#5F9EA0', padx =10, pady =10, font=('Arial',14))
vvod = tk.Text(font=('Arial',14),width= 40)
vvod1 = tk.Text(font=('Arial',14),width= 40)
btn = tk.Button(
    text = "Готово!",
    command = lambda: click_button()
)

text.pack(ipadx=30, ipady=10,padx= 30,pady= 30)
vvod.place(x = 80, y =130, height= 100)
btn.place(x = 265, y = 450, width = 80, height = 40)
text1.place(x = 120, y = 250)
vvod1.place(x = 80, y =320, height= 100)
window.mainloop()



