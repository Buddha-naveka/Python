import tkinter as tk
from tkinter.messagebox import showinfo
import timeit
from itertools import permutations


def click_button():
 
    fruits = []
    sugar = {0:9.9, 1:7.5, 2:2, 3:12, 4:13.7, 5:9.92, 6:13, 7:1, 8:5, 9:7}
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
                                                                        spisok.append(fruits[i]); sum += sugar[i] * 1 
                                                                        spisok.append(fruits[o]); sum += sugar[o] * 2
                                                                        spisok.append(fruits[p]); sum += sugar[p] * 3
                                                                        spisok.append(fruits[j]); sum += sugar[j] * 4
                                                                        spisok.append(fruits[k]); sum += sugar[k] * 5
                                                                        spisok.append(fruits[l]); sum += sugar[l] * 6
                                                                        spisok.append(fruits[m]); sum += sugar[m] * 7
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
vvod = tk.Text(font=('Arial',14),width= 40)
btn = tk.Button(
    text = "Готово!",
    command = lambda: click_button()
)

text.pack(ipadx=30, ipady=10,padx= 30,pady= 30)
vvod.place(x = 80, y =130, height= 100)
btn.place(x = 265, y = 450, width = 80, height = 40)
window.mainloop()



