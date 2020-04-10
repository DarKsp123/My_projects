'''
while True:     # Начало цикла
    reply = input('Enter text: ')   # Ввод текста с клавиатуры
    if reply == 'stop':     # Если введем stop, то цикл закончится и програма выйдет
        break
    elif not reply.isdigit():   # проверка на ошибки ввода текста
        print('Bad' * 8)
    else:                       # Если мы прошли проверку ввода то программа будет выводить число возведенное в степень
        print(int(reply) ** 2)
print('Bye')

while True:
        reply = input('Enter text: ')
        if reply == 'stop': break
        try:
            num = int(reply)
        except:
            print('Bad' * 8)
        else:
            print(num ** 2)
print('Bye')

while True:
    reply = input('Enter text: ')
    if reply == 'stop':
        break
    try:
        num = int(reply)
    except:
        print('Bad' * 8)
    else:
        if num < 20:
            print('Low')
        else:
            print(num ** 2)
print('Bye')
'''

from tkinter import *

def clicked():                                  # Функция вывода
    res = txt.get()
    res = int(res)
    result = str(res ** 2)
    lbl.configure(text='Возведение числа в степень 2: {}'.format(result))

window = Tk()   # Объявляем окно программы
window.title("Добро пожаловать в приложение PythonRU")      # Название кона программы
window.geometry('400x250')     # Объявляем размеры окна программы
lbl = Label(window, text='Привет', font=('Arial Bold', 14))     # Виджет label - Создание текста в окне нашей программы
lbl.grid(column=0, row=0)   # Место расположение текста лейбла (столбец, строка)
txt = Entry(window, width=10) #, state='disabled')   # Создание текстового поля, дял ввода пользователя (Размер поля(символов), включение/отключение пользовательского ввода)
txt.grid(column=1, row=0)   # расположение текстового поля
txt.focus()
btn = Button(window, text='Клик!', bg='Black', fg='red', command=clicked)    # Создание кнопки (Название кнопки, цвет кнопки, цвет надписи на кнопке, функция нажатия)
                                                                                # ВАЖНО!!! - Создать функцию нажатия для выполнения той или иной операции
btn.grid(column=2, row=0)   # Расположение кнопки(столбец, строка)
window.mainloop()   # Функция mainloop - Запускает цикл окна программы, без него пользователь ничего не увидит

