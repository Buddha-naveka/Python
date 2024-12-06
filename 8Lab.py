"""Объекты – прямоугольники
Функции: проверка пересечения
визуализация
раскраска
перемещение на плоскости
"""
d ={0:'red', 1:"blue", 2:'green', 3:'black', 4:'yellow'} # Цвета

import tkinter as tk
from tkinter.messagebox import showinfo

def click_button():
    data = str(t.get())
    probel = data.split()
    if len(probel) ==2:
        dx =int(probel[0])
        dy =int(probel[1])
        #canvas.delete(rect1)
        rect1.move(dx,dy)
        #rect1.visualize()
        if rect1.intersects(rect2):
            showinfo(title="Проверка", message="Фигуры пересекаются") 
    else:
        showinfo(title="Ошибка", message="Данные введены не корректно") 
          

def click_button1():
    data = str(t1.get())
    probel = data.split()
    if len(probel) ==2:
        dx =int(probel[0])
        dy =int(probel[1])
        #canvas.delete(rect1)
        rect2.move(dx,dy)
        #rect1.visualize()
        if rect1.intersects(rect2):
            showinfo(title="Проверка", message="Фигуры пересекаются") 
    else:
        showinfo(title="Ошибка", message="Данные введены не корректно") 

def recolr():
     rect1.recolor(d[0])
def recolb():
     rect1.recolor(d[1])
def recolr1():
     rect2.recolor(d[0])
def recolb1():
     rect2.recolor(d[1])
#----------------------------------------Class------------------------------------------------------
class Rectangle:
    def __init__(self, canvas, x, y, x1, y1, color="black"):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
        self.color = color
        self.id = canvas.create_rectangle(x, y, x1, y1, fill=color)
    
    def visualize(self):
        self.canvas.create_rectangle(self.x, self.y, self.x1, self.y1, fill=self.color)
        self.canvas.update() 

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.x1 += dx
        self.y1 += dy
        self.canvas.coords(self.id,self.x, self.y, self.x1, self.y1)
        self.canvas.update()

    def intersects(self, other):
        x_overlap = ((self.x < other.x1) and (self.x1 > other.x)) 
        y_overlap = ((self.y < other.y1) and (self.y1 > other.y)) 
        return x_overlap and y_overlap
    
    def recolor(self, new_color):
        self.color = new_color
        self.canvas.itemconfig(self.id, fill=self.color)
        self.canvas.update()
#------------------------------------------Ввод------------------------------------------------------------

perem = 0
with open('text', 'r') as file:
    data =file.readline().split()
if len(data) ==10:
    for i in range(len(data)):
        string = str(data[i])
        if string.isnumeric() == True:
            perem =1
        else: 
            showinfo(title="Ошибка", message="Это не числа")
            perem = 0
    if perem ==1:
        x,y,x1,y1,col,x_2,y_2,x1_2,y1_2,col1 = map(int, data)
        color = d[col]
        color1 = d[col1]
else: 
    showinfo(title="Ошибка", message="Чисел не 10")

window = tk.Tk()
window.title("9Lab")
window.geometry('750x650+650+200')
window.resizable(False,False)

btnr = tk.Radiobutton(text='Красный 1', value= 'Красный 1', command= lambda: recolr())
btnr.place(x = 640, y = 20)
btnb = tk.Radiobutton(text='Синий 1', value= 'Синий 1', command= lambda: recolb())
btnb.place(x = 640, y = 40)

btnr1 = tk.Radiobutton(text='Красный 2', value= 'Красный 2', command= lambda: recolr1())
btnr1.place(x = 640, y = 80)
btnb1 = tk.Radiobutton(text='Синий 2', value= 'Синий 2', command= lambda: recolb1())
btnb1.place(x = 640, y = 100)

#---------------------------------------Оформление низ----------------------------------------------
text = tk.Label(text = 'Введите смещение на x и y первой и/или второй фигуры : ',font=('Arial',14))
text.place(x =10, y = 560, height= 40)
t = tk.Entry()
t.place(x =40, y = 600, width= 100, height= 30)
btn = tk.Button(text = "Готово!",command = lambda: click_button())
btn.place(x = 170, y = 600, width = 80, height = 30)

t1 = tk.Entry()
t1.place(x =350, y = 600, width= 100, height= 30)
btn1 = tk.Button(text = "Готово!",command = lambda: click_button1())
btn1.place(x = 480, y = 600, width = 80, height = 30)
#---------------------------------------------------------------------------------------
canvas = tk.Canvas(window, width=600, height=550, bg="lightblue")
canvas.pack(anchor='nw')
rect1 = Rectangle(canvas, x, y, x1, y1, color)
#rect1.visualize()
rect2 = Rectangle(canvas, x_2, y_2, x1_2, y1_2, color1)
#rect2.visualize()
if rect1.intersects(rect2):
    showinfo(title="Проверка", message="Фигуры пересекаются") 
window.mainloop()
