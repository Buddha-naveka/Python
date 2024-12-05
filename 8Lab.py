"""Объекты – прямоугольники
Функции: проверка пересечения
визуализация
раскраска
перемещение на плоскости
"""
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
#------------------------------------------------------------------------------------------------------
perem = 0
while perem !=1:
    print("Введите x,y,x1,y1 для 1 фигуры:")
    i = [int(a) for a in input().split()]
    if len(i) ==4:
        x,y,x1,y1 = i[0],i[1],i[2],i[3]
        perem =1
    else:
        print('Вы ввели некоректные данные, попробуйте ещё раз')
perem = 0
while perem !=1:
    print("Введите x,y,x1,y1 для 2 фигуры:")
    i = [int(a) for a in input().split()]
    if len(i) ==4:
        x_2,y_2,x1_2,y1_2 = i[0],i[1],i[2],i[3]
        perem =1
    else:
        print('Вы ввели некоректные данные, попробуйте ещё раз')

window = tk.Tk()
window.title("9Lab")
window.geometry('600x650+650+200')
window.resizable(False,False)
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
canvas.pack()
rect1 = Rectangle(canvas, x, y, x1, y1, "red")
#rect1.visualize()
rect2 = Rectangle(canvas, x_2, y_2, x1_2, y1_2, "blue")
#rect2.visualize()
if rect1.intersects(rect2):
    showinfo(title="Проверка", message="Фигуры пересекаются") 
window.mainloop()

