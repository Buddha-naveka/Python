import tkinter as tk
from tkinter.messagebox import showinfo
import timeit
from itertools import permutations


#fruits = []
def click_button():
 
    fruits = []
    sugar = {0:9.9, 1:7.5, 2:2, 3:12, 4:13.7, 5:9.92, 6:13, 7:1, 8:5, 9:7}
    #data = open('test.txt', 'r')
    data = str(vvod.get("1.0", "end"))
    #print(data)

    probel = data.split()
    if len(probel) ==10:
        for i in range(len(probel)):
            f = probel[i]
            if f.isalpha() == False:
                btn["state"] = ["active"]
                #print('no')  
                showinfo(title="Ошибка", message="Данные введены не корректно, запись должна содержать только буквы")          
                fruits = []
                break
            else:
                btn["state"] = ["disabled"]
                fruits.append(probel[i])
                if len(fruits) == 10:
                    b =list(permutations(fruits,3))
                    #print(b)
                    window2 = tk.Tk()
                    window2.title('Ответ')
                    window2.geometry('500x450+650+200')
                    window2.configure(bg = '#4682B4')
                    t = tk.Text(window2)
                    t.place(x =60, y = 70, width= 400, height= 250)
                    t.insert("1.0", b) 
                    scrollbar = tk.Scrollbar(window2,orient="vertical", command=t.yview)
                    scrollbar.place(x = 460, y = 70, height= 250)
                    #scrollbar.pack( side = 'right', fill='y' )
                    t["yscrollcommand"]=scrollbar.set
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
#text1 = tk.Label(text = 'Введите содержание сахара в фруктах: ',bg ='#5F9EA0', padx =10, pady =10, font=('Arial',14))
#vvod = tk.Entry(font=('Arial',14),width= 40)
vvod = tk.Text(font=('Arial',14),width= 40)
#vvod1 = tk.Entry(font=('Arial',14),width= 40)
'''t = tk.Text()
t.place(x = 80,y = 300)'''
btn = tk.Button(
    text = "Готово!",
    command = lambda: click_button()
)
#vvod = tk.Entry()
#data = str(vvod.get())
text.pack(ipadx=30, ipady=10,padx= 30,pady= 30)
vvod.place(x = 80, y =130, height= 100)
#text1.place(x = 110, y = 220)
#vvod1.place(x = 80, y =300, height= 70)
btn.place(x = 265, y = 450, width = 80, height = 40)
#btn.pack(anchor='s', ipadx=30, ipady=10, padx= 30,pady= 0)
window.mainloop()



