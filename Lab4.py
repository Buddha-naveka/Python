'''Написать программу, которая читая символы из файла, распознает, преобразует и выводит на экран объекты по определенному правилу.
 Объекты разделены пробелами. Распознавание и преобразование делать по возможности через регулярные выражения. 
 Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа.
'''
import re

text = '\d+\.\d+'
file = open('test.txt', 'r')
s =file.readline().split()
while s!=0:
    for i in range(len(s)):
        string = str(s[i])
        if re.findall(text, string):
            result = re.sub('\.', ',', string)
            print(result)
           
    s =file.readline().split()
