'''Написать программу, которая читая символы из бесконечной последовательности (эмулируется 
конечным файлом), распознает, преобразует и выводит на экран объекты по определенному правилу. 
Объекты разделены пробелами. Преобразование делать по возможности через словарь. Для 
упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр 
числа. Регулярные выражения использовать нельзя.
Вещественные числа. В них менять точку на запятую.'''
def is_float(s):
    try:
        float(s[i])
        return True
    except ValueError:
        return False
with open('test.txt', 'r') as file:
    while True:
        s =file.readline().split()
        for i in range(len(s)):
            string = str(s[i])
            if is_float(s) and string.isnumeric() == False:
                result = string.replace('.', ',', 1)
                print(result)
        if not s:
            break
           
    
