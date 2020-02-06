# Работа со строками
from math import trunc

line = 'aaa,bbb,ccc,dd'
print(line.split(','))
S = 'spam'
print(S.upper())
print(S.isalpha())
print(S.isdigit())
line = 'aaa,bbb,ccc,dd\n'
print(line)
print(line.rstrip())  # Удаление пробелов в конце строки
print(line.rstrip().split(','))  # Удаление пробелов в конце строки + Разбиение разделителем
print('%s, eggs, and %s' % ('spam', 'SPAM!'))  # Метод форматирования
print('{0}, eggs, and {1}'.format('spam', 'SPAM!'))  # Метод форматирования
print('{}, eggs, and {}'.format('spam', 'SPAM!'))  # Метод форматирования
print('{:,.2f}'.format(296999.2567))  # Разделитель, десятичные цифры
print('%.2f | %+05d' % (3.14159, -42))  # Цифры, дополнение, знаки
# print(dir(line)) # Выводит все методы и функции для line
print(S.__add__('NI!\n\t\t\t\t\tДальше идет работа со списками'))  # Метод конкатенации(Сложения = S + 'NI!')
# print(help(str)) # Выводит подсказку по методам и функциям того или иного ТИПА данных)

# Работа со списками

L = [123, 'spam', 1.23]  # Список из трех элементов разного типа
print(len(L))  # Кол-во элементов в списке
print(L)
L.append('NI')  # Добавление объекта в конец списка
print(L)
L.pop(2)  # Удаление элемента из середины
print(L)
L.insert(0, 'SPAM!')  # Вставляет элемент в произвольную позицию по индексу
print(L)
L.remove('spam')  # Удаляем элемент из списка по его названию
print(L)
S = ['Hellow', 'World!', 'Python']
L.extend(S)  # Вставляем один список в конец другова
print(L)
M = ['bb', 'aa', 'cc']
print(M)
M.sort()  # Упорядочивание списка по возрастанию
print(M)
M.reverse()  # Обращается список по убыванию
print(M)
print(L)
L[3] = 'Goodbye'
print(L)
M = [[1, 2, 3],  # Матрица в виде вложенных списков
     [4, 5, 6],
     [7, 8, 9]]
print(M)
print(M[1])  # Получаем вторую строку матрицы
print(M[1][2])  # Получение строку 2 и затем элемент 3 внутри этой строки
# Работа с выражениями спискового включения(list comprehension) - столбцами матрицы'
print('\n\t\t\t\t\t\tРабота с выражениями спискового включения(list comprehension) - столбцами матрицы')

col2 = [row[1] for row in M]  # Выводим второй стобец матрицы
print(col2)
col2 = [row[1] + 1 for row in M]  # Добавляем 1 к каждому элементу второго стобца матрицы
print(col2)
col2 = [row[1] for row in M if row[1] % 2 == 0]  # Отфильтровать нечетные элементы
print(col2)

diag = [M[i][i] for i in [0, 1, 2]]  # Собрать диагональ из матрцы
print(diag)

doubles = [c * 2 for c in 'spam']  # Повторить символы в строке
print(doubles)

print(list(range(4)))  # От 0..3
print(list(range(-6, 7, 2)))  # от -6 до +6 с шагом 2

math = [[x ** 2, x ** 3] for x in range(4)]  # множество значений, фильтры if
print(math)

math = [[x, x / 2, x * 2] for x in range(-6, 7, 2) if
        x > 0]  # множество значений, фильтры if(задаем матрицу по формуле)
print(math)

G = (sum(row) for row in M)
print(next(G))

print(list(map(sum, M)))  # Отоброзить sum на элементы в М

# Создание множеств и словарей
print('\n\t\t\t\t\t\t\t\t\t\t\t\t\tСоздание множеств и словарей')

print({sum(row) for row in M})  # Создать множество сумм элементов в строках
print({i: sum(M[i]) for i in range(3)})  # Создать таблицу ключей / значений сумм элементов в строках
print([ord(x) for x in 'spaam'])  # Выводим порядковый номер(десятичный) символа, согласно ASCII
print({ord(x) for x in
       'spaam'})  # множество с удаленными дубликатами значений порядкового номера символов в таблице ASCII
print({x: ord(x) for x in 'spaam'})  # Словарь с уникальными ключами
G = (ord(x) for x in 'spaam')  # Генератор значений
print(next(G))  # Выводим значения генертора, без функ-ции next(движение по циклу) не работает

# Словари
print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tСловари')

D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
print(D['food'])  # Извлечь значение, связанное с ключом 'food'
D['quantity'] += 1  # Добавить 1 к значению, связанному с ключом 'quantity'
print(D)

D = {}
D['name'] = 'Bob'
D['job'] = 'dev'  # Присвоение приводит к созданию ключей
D['age'] = 40
print(D)
print(D['name'])

bob1 = dict(name='Bob', job='dev', age=40)  # Создаем ключевые слова(словарь)
print(bob1)

bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40]))  # Связывание вместе(создается словарь)
print(bob2)

rec = {'name': {'first': 'Bob', 'last': 'Smith'},  # Вложенные списки(сложноструктурированные)
       'jobs': ['dev', 'mgr'],
       'age': 40.5}
print(rec['jobs'][0])
rec['jobs'].append('janitor')  # Добавляем значение в атрибут словаря jobs
print(rec)

rec = 0  # Очищение области памяти занимаемая объектом(в нашем случае rec)
print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t Недостоющие ключи: проверка if')
# Недостающие ключи: проверки if

D = {'a': 1, 'b': 2, 'c': 3}
print(D)
D['e'] = 99  # Присвоение новому ключу - увеличивает словарь
print(D)

# if not 'f' in D:                                #Проверка атрибута f в словаре D(так как не выдает ошибку)
#    print('missing')


value = D.get('x', 0)  # Избегаем обращения к несуществующим ключам с помощью метода get
print(value)
value = D[
    'x'] if 'x' in D else 0  # Избегаем обращения к несуществующим ключам с помощью проверки значения через if/else
print(value)

# Цикл for

print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t Цикл for')

Ks = list(D.keys())  # Неупорядоченный список ключей
print(Ks)
Ks.sort()  # Сортировка ключей

for key in Ks:
    print(key, '=>', D[key])  # Цикл for проход по отсартированным ключам

D = {'a': 1, 'c': 3, 'b': 2}
print(D)
for key in sorted(D):
    print(key, '=>', D[key])

for c in 'spam':
    print(c.upper())  # Проходит по символам в строке и выводит символы в верхнем регистре

x = 4
while x > 0:
    print('spam!' * x)
    x -= 1
    # Итерация и оптимизация
print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t Итерация и оптимизация')

squares = [x ** 2 for x in [1, 2, 3, 4, 5]]  # Списковое включение вычисляющее квадраты для списка чисел
print(squares)
squares = []
for x in [1, 2, 3, 4, 5]:  # Тоже самое только через отдельный цикл for
    squares.append(x ** 2)
print(squares)

# Кортежи(Не изменяемы списки). Хорош использовать, если вы хотите написать программу
# без каких либо изменений в нее
print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Кортежи')

T = (1, 2, 3, 4)  # Кортеж из 4 элементов
print(T)
print(len(T))  # Вывести длину кортежа
T = T + (5, 6)  # Конкатенация
print(T)
print(T[5])  # Индексация, нарезание и т.д.
print(T.index(4))  # Методы(вызываемые методы в данном случае index) кортежей. 4 обнаруживается по смещению 3
print(T.count(4))  # Еще один вызываемы метод кортежей(count). 4 обнаруживается один раз

T = (2,) + T[
           1:]  # Создаем новый кортеж для нового значения. Значение вставляется так, что отбрасываются начальные символы(T[1:]
print(T)
T = 'spam', 3.0, [11, 22, 33]
print(T[2][2])

# Файлы
print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Файлы')

f = open('data.txt', 'w')  # Создать новый файл в режиме записи
f.write('Hellow\n')  # Записать в него строки символов
f.write('world\n')
f.close()  # Закрыть файл для сбрасывания буферов вывода на диск
f = open('data.txt')  # 'r' (чтение) - стандартный режим обработки
text = f.read()  # Прочитать все содержимое файла в строку
print(text)
print(text.split())  # Содержимое файла всегда строка
# print(dir(f)) Показывает все методы
# print(help(f.seek)) Описание методов по средстав help
for line in open('data.txt'):  # Вывод данных в файле строка за строкой
    print(line)

    # Двоичные файлы(удобны для обработки медиаданных, доступа к данным)
print('\n\t\t\t\t\t\t\t\t\t\t\t\t Двоичные файлы(удобны для обработки медиаданных, доступа к данным)')

import struct

packed = struct.pack('>i4sh', 7, b'spam', 8)  # создать упакованные двоичные данные
print(packed)  # 10 байтов, не объекты и не текст

file = open('data.bin', 'wb')  # Открыть двоичный файл для записи
file.write(packed)  # Записатьупакованные двоичные данные
file.close()
print(file)
data = open('data.bin', 'rb').read()  # Открыть/прочитать двоичный файл данных
print(data)
print(data[4:8])  # Нарезать байты в середине
print(list(data))  # Последовательность 8 битных данных
print(struct.unpack('>i4sh', data))  # Снова распаковать в объекты

# Файлы с текстом Unicode стр 156-158(Важная тема для кодировки/декодировки)
print('\n\t\t\t\t\t\t\t\t\t\t\t\t Файлы с текстом Unicode')

S = 'sp\xc4m'  # Текст Unicode, отличающийся от ASCII
print(S)
print(S[2])  # Последовательность символов
file = open('unidata.txt', 'w', encoding='utf-8')  # Записать/закодировать текст UTF-8
print(file.write(S))  # Записано 4 символа
file.close()
text = open('unidata.txt', encoding='utf-8').read()  # Прочитать/декодировать текст UTF-8
print(text)
print(len(text))

raw = open('unidata.txt', 'rb').read()  # Читать закодированные байты
print(raw)
print(len(raw))  # 5 байтов в кодировке UTF-8
# При получение закодированного сообщения в электронной почте или через
# сетевое подключение можно кодировать/декодировать в ручную
print(text.encode('utf-8'))  # В ручную кодировать в байты
print(raw.decode('utf-8'))  # В ручную декодировать в строку
# Кодирование в другие кодировки
print(text.encode('latin-1'))  # Байты отличаются от других
print(text.encode('utf-16'))  # Байты отличаются от других
print(len(text.encode('latin-1')), len(text.encode('utf-16')))
print(b'\xff\xfes\x00p\x00\xc4\x00m\x00'.decode('utf-16'))  # Декодируются в ту же самую строку
# Чтение декодирование в Python 2.X
import codecs

print(codecs.open('unidata.txt', encoding='utf-8').read())  # Python 2.X читать/декодировать текст
print(open('unidata.txt', 'rb').read())  # Читать низкоуровневые байты
print(open('unidata.txt').read())  # Так же низкоуровневые/декодирование

# Прочие основные типы стр.158
print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Прочие основные типы')
# Множества вызываются с помощью встроенной функции set
X = set('spam')  # Создать множество из последовательности
Y = {'h', 'a', 'm'}  # Создать мнодество с помощью литералов множеств
print(X, Y)  # Кортеж из двух множеств без круглых скобок
print(X & Y)  # Пересечение
print(X | Y)  # Объединение
print(X - Y)  # Разность
print(X > Y)  # Надмножество
print({n ** 2 for n in [1, 2, 3, 4]})  # Включение множеств
print(list(set([1, 2, 1, 3, 1])))  # Фильтрация дубликатов(возмрожно неупорядоченных)
print(set('spam') - set('ham'))  # Нахождение разностей в коллекциях
print(set('spam') == set('asmp'))  # Нейтральная к порядку проврка(Равенство 'spam' == 'asmp' дает False)
print('p' in set('spam'), 'p' in 'spam', 'ham' in ['eggs', 'spam', 'ham'])  # Проверка челенства в in
print(1 / 3)  # Математика с плавающей точкой
print((2 / 3) + (1 / 2))
import decimal  # Десятичные числа: фиксированная точность

d = decimal.Decimal('3.141')
print(d + 1)
decimal.getcontext().prec = 2
print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))
from fractions import Fraction  # Дроби: числитель + знаменатель

f = Fraction(2, 3)
print(f + 1)
print(f + Fraction(1, 2))
# Булевские значения
print(1 > 2, 1 < 2)  # Булевские значения
print(bool('spam'))  # Булевское значение объекта
X = None  # Заполнитель None
print(X)
L = [None] * 100  # Инициализировать список сотней объектов None
print(L)
# Как нарушить гибкость кода(Объект типа type)
print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Как нарушить гибкость кода(Объект типа type)')
print(type(L))  # Типом L является list
print(type(type(L)))  # Даже типы явлюятся объектами
if type(L) == type([]):  # Проверка типа при необходимости
    print('yes')
if type(L) == list:  # Использование имени типа
    print('yes')
if isinstance(L, list):  # Объектно-ориентированная проверка
    print('yes')

    # Классы, определяемы пользователем. стр. 161
print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Классы, определяемые пользователем стр. 161')


class Worker:
    def __init__(self, name, pay):  # инициализировать при создание
        self.Name = name  # self - новый объект
        self.pay = pay

    def lastName(self):
        return self.Name.split()[-1]  # Разбить строку по пробелам

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)  # Обновить pay на месте


bob = Worker('Bob Smith', 50000)  # Создать два экземпляра
sue = Worker('Sue Jones', 60000)  # Каждый имеет атрибут name и pay
print(bob.lastName())
print(sue.lastName())
sue.giveRaise(.11)
print(sue.pay)
# Заканчивается введине, начинаем погружение :D
# Числовые типы
print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t Закончили введение, начали погружение :D'
      '\n\t\t\t\t\t\t\t\t\t\t\t\t\t Числовые типы')
# Оснвы числовых типов стр 165
print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Основы числовых типов стр. 165')

print(int(3.1415))
print(float(3))

a = 3  # Имя создается: не объявляется за ранее
b = 4
print(a + 1, a - 1)  # Сложение (3 + 1)б вычитание (3 - 1)
print(b * 3, b / 2)  # Умножение (4 * 3)б деление (4 / 2)
print(a % 2, b ** 2)  # Деление по модулю (нахождение остатка), воведение в степень (4 ** 2)
print(2 + 4.0, 2.0 ** b)  # преобразование разнородных типов
print(b / 2 + a)  # группировка и преобразование
print(b / (2 + a))  # меняем приоритет вычисления
num = 1 / 3.0
print(num)  # Явный вывод
print('%e' % num)  # Выражение форматирования строк
print('%4.2f' % num)  # Альтернативный формат с плавающей точкой
print('{0:4.2f}'.format(num))  # метод форматирования строк
print(1 < 2)  # Меньше
print(2.0 >= 1)  # Больше или равно: число разнородного типа 1 преобразуется в 1.0
print(2.0 == 2.0)  # Равенство значений
print(2.0 != 2.0)  # Неравенство значений
X = 2
Y = 4
Z = 6
print(X < Y < Z)  # Сцепленные сравнения: проверки вхождения в диапазон
print(X < Y and Y < Z)  # Тоже самое. Первый вариант оптимизирован
print(1.1 + 2.2 == 3.3)
print(1.1 + 2.2)
print(int(1.1 + 2.2) == int(3.3))
# Деление: классическое, с округлением в меньшую сторону и настоящее
print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Деление: классическое, с округлением в меньшую сторону и настоящее')
print(10 / 4)  # Сохраняет остаток
print(10 / 4.0)  # сохраняет остаток
print(10 // 4)  # усекает остаток
print(10 // 4.0)  # округляет в меньшую сторону
print('X = ', Y // Z) # Всегда усекает, всегда возвращает целочисленный результат для целых
print('X = ', Y / float(Z)) # Гарантирует деление с плавающей точкой с остатком
                                    # Округление в меньшую сторону или усечение
print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Округление в меньшую сторону или усечение')

import math
print(math.floor(2.5)) # Ближайшее меньшее значение
print(math.floor(-2.5)) # Ближайшее меньшее значение
print(math.trunc(2.5)) # Усечение дробной части (в сторону нуля)
print(math.trunc(-2.5)) # Усечение дробной части (в сторону нуля)
print(5 / 2, 5 / -2)
print(5 // 2, 5 // -2) # Усекает в меньшую сторону: округляет до первого меньшего целого. (2.5 становиться 2, -2.5 становиться -3)
print(5 // 2.0, 5 // -2.0) # Повторяется для чисел с плавающей точкой, хотя результат имеет тот же тип
print(round(5 // 2)) # Тоже округление, только без импортирования модуля math
                                    # Шестнадцатеричная, восьмеричная и двоичная формы записи:литералы и преобразования
print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t Шестнадцатеричная, восьмеричная и двоичная формы записи:литералы и преобразования')

print(0o1, 0o20, 0o377) # Восьмеричные литералы: основание 8, цифры 0-7
print(0x01, 0x10, 0xFF) # Шестнадцатеричные литералы: основание 16, цифры 0-9/A-F
print(0b1, 0b10000, 0b11111111) # Двоичные литералы: основание 2, цифры 0-1
print(0xFF, (15 * (16 ** 1)) + (15 * (16 ** 0))) # Как шестнадцатеричное/двоичное число отображается на десятичное
print(0x2F, (2 *(16 ** 1)) + (15 * (16 ** 0)))  # Как шестнадцатеричное/двоичное число отображается на десятичное
print(0xF, 0b1111, (1 * (2 ** 3) + 1 * (2 ** 2) + 1 * (2 ** 1) + 1 * (2 ** 0))) # Как шестнадцатеричное/двоичное число отображается на десятичное
print(oct(64)) # Преобразование десятичного числа в восьмеричное
print(hex(64)) # Преобразование десятичного числа в шестнадцатеричное
print(bin(64)) # Преобразование десятичного числа в двоичное
print(int('64'), int('100', 8), int('40', 16), int('1000000', 2)) # int - преобразует строку цифр в число, и принимает второй не обязательный аргумент, указывающий основание системы счисления
print(int('0x40', 16), int('0b1000000', 2)) # литеральная форма
print('{0:o}, {1:x}. {2:b}'.format(64, 64, 64))
X = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFF # 16 ричная система счисления
print(X)
print(oct(X)) # Переводим в восьмиричную
print(bin(X)) # Переводим в двоичную
                                            # Побитовые операции
print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Побитовые операции')
x = 1 # Десятичное значение 1 в битах выглядит как 0001
print(x << 2) # Сдвиг влево на 2 бита: 0100
print(x | 2) # Побитовое ИЛИ(один из битов = 1): 0011 (Объединение битов 0001 | 0010 = 0011)
print(x & 1) # Побитовое И (оба бита = 1): 0001 (Выбор общих битов 0001 & 0001 = 0001)
                                            # Основы множеств
print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Основы множеств')
print({1, 2, 3, 4}) # Литералы множеств
S = {'s', 'p', 'a', 'm'}
print(S)
S.add('alot') # добавление элемента в литерал множества
print(S)
S1 = {1, 2, 3, 4}
print(S1 & {1, 3}) # Пересичение
print({1, 5, 3, 6} | S1) # Объединение
print(S1 - {1, 3, 4}) # Разность
print(S1 > {1, 3}) # Надмножество
S = set() # Инициализация пустого множества
S.add(1.23)
print(S)
S.add((1, 2, 3)) # Списки(list) и словари(dict) не допускаются, но кортежи разрешены
print(S)
S = S | {(4, 5, 6), (1, 2, 3)} # Объединение, тоже что и S.union()
print(S)
                                            # Включение мноеств в Python
print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t Включение множеств в Python')
print({x ** 2 for x in [1, 2, 3, 4]}) # Включение множества в Python
print({x for x in 'spam'}) # то же, что и set('spam')
print({c * 4 for c in 'spam'}) # Множество накопленных результатов выражения
print({c * 4 for c in 'spamham'})
S = {c * 4 for c in 'spam'}
S = S | {'mmmm', 'xxxx'}
print(S)
S = S & {'mmmm', 'xxxx'}
print(S)
L = [1, 2, 1, 3, 2, 4, 5]
print(set(L)) # Удаление дубликатов
L = list(set(L)) # Удаление дубликатов
print(L)
print(list(set(['yy', 'cc', 'aa', 'xx', 'dd', 'aa'])))
K = set([1, 3, 5, 7]) - set([1, 2, 4, 5, 6]) # Найти различия в списках
print(K)
K = set('abcdefg') - set('abdghij') # Найти различия в строках
print(K)
K = set('spam') - set(['h', 'a', 'm']) # найти различия, разнородные типы
print(K)
K = set(dir(bytes)) - set(dir(bytearray)) # В bytes, но не в bytearray
print(K)
K = set(dir(bytearray)) - set(dir(bytes))
print(K)
L1, L2 = [1, 3, 5, 2 ,4], [2, 5, 3, 4, 1]
print(L1 == L2) # В последовательностях порядок имеет значение
print(set(L1) == set(L2))
print(sorted(L1) == sorted(L2))
print(L1, L2)
engineers = {'bob', 'sue', 'ann', 'vic'}
managers = {'tom', 'sue'}
print('bob' in engineers) # Являеется ли сотрудник bob инженером?
print(engineers & managers) # Кто одновременно инженер и менеджер?
print(engineers | managers) # Все сотрудники в обеих катогориях
print(engineers - managers) # Инженеры не являющиеся менеджерами
print(managers - engineers) # Менеджеры, не являющиеся инженерами
print(engineers > managers) # Все ли менеджеры - инженеры? (Надмножества)
print({'bob', 'sue'} < engineers) # Оба ли сотрудника инженеры? (Подмножества)
print((managers | engineers) > managers) # Все сотрудники - надмножество менеджеров?
print(managers ^ engineers) # Кто находится в одной категории, но не в обеих?
print((managers | engineers) - (managers ^ engineers)) # Пересичение!

                                            # Булевские значения
print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Булевские значения')
print(type(True))
print(isinstance(True, int))
print(True == 1) # То же самое значение
print(True is 1) # Но другой объект: см. следующую главу
print(True or False) # То же что и 1 or 0
print(True + 4) # М-да

                                                # Динамическая типизация
print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t Динамическая типизация'
      '\n\t\t\t\t\t\t\t\t\t\t\t\t Разделяемы ссылки и изменения на месте')

L1 = [2, 3, 4] # Изменяемый объект
L2 = L1 # Создает ссылку на тот же самый объект
L1[0] = 24 # Изменение на месте
print(L1, L2) # L1 и L2 отличаются от первоначального значения
L1 = [2, 3, 4]
L2 = L1[:] # Соззать копию L1 (или list(L1), copy.copy(L1) и т.д.)
L1[0] = 24
print(L1, L2)
                                                # Фундаментальные основы строк
print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t Фундаментальные основы строк'
      '\n\t\t\t\t\t\t\t\t\t\t\t ')

myjob = 'hacker'
for c in myjob: # проходит по элементам с выводом каждого
    print(c, end = ' ') # end = говорит о разделителе между символами вывода

print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t Расширенное нарезание: третий предел и объекты срезов')
S = 'abcdefghijklmnop'
print(S[1:10:2]) # пропуск элементов
print(S[::2])
S = 'hello'
print(S[::-1]) # Смена порядка следования элементов на противоположный
S = 'abcedfg'
print(S[5:1:-1]) # Смысл границ изменяется
print('spam'[1:3]) # Синтаксис нарезания
print('spam'[slice(1, 3)]) # Индексация посредством объектов срезов
print('spam'[::-1])
print('spam'[slice(None, None, -1)])
import sys
print(sys.argv)
                                            # Изменение строк, часть 1
print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t Изменения строк, часть 1')
S = 'spam'
S = S + 'SPAM!' # Чтобы изменить строку, нужно создать новую
print(S)
S = S[:4] + 'Burger' + S[-1]
print(S)
S = 'splot'
S = S.replace('pl', 'pamal')
print(S)
                                            # Строковые методы
                                     # Синтаксис - объект.метод(аргументы)

print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t Строковые методы')
S = 'spam'
result = S.find('pa') # Вызов метода find для поиска 'pa' в строке S
print(result)
S = 'spammy'
S = S[:3] + 'xx' + S[5:] # Нарезать сегменты из S
print(S)
print('aa$bb$cc$dd'.replace('$', 'SPAM'))
S = 'xxxxSPAMxxxxSPAMxxxx'
where = S.find('SPAM') # Поиск позиции
print(where) # Нашлась по смещению 4
S = S[:where] + 'EGGS' + S[(where + 4):]
print(S)
S = 'xxxxSPAMxxxxSPAMxxxx'
print(S.replace('SPAM', 'EGGS'))
print(S.replace('SPAM', 'EGGS', 1))
S = 'spammy'
L = list(S) # Приобразуем строку в объект
print(L)
L[3] = 'x' # Работает для списков, но не для строк
L[4] = 'x' # Работает для списков, но не для строк
print(L)
S = ''.join(L) # Преобразуем обратно в строку
print(S)
print(', '.join(['eggs', 'sausage', 'ham', 'toast'])) # Объект есть разделитель, в данном случае 'SPAM'
line = 'aaa bbb ccc'
col1 = line[0:3] # методики нарезания
col3 = line[8:] # методики нарезания
print(col1, col3)
line = 'aaa bbb ccc'
cols = line.split() # Разбиение строк по методу разделителя( в данном случае пусто, по умолчанию пробел)
print(cols)
line = 'bob, hacker, 40'
print(line.split(',')) # В данном примере разделить ',', применяется для анализа данных БД
line = "i'mSPAMaSPAMlumberjack"
print(line.split('SPAM')) # Разделитель может быть длиннее одного символа
                                # Синтаксис - x.метод(аргумент)
S = 'a+b+c'
x = S.replace('+', 'spam')
print(x)
                                # Основы выражений форматирования
print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Основы выражений форматирования')

print('That is %d %s bird!' % (1, 'dead')) # Выражение формата
exclamantion = 'Ni'
print('The knights who say %s!' % exclamantion) # Подстановка строки
print('%d %s %g you' % (1, 'spam', 4.0)) # Подстановки, специфичные для типов
print('%s -- %s -- %s' % (42, 3.14159, [1, 2, 3])) # Все типы соответствующие цели %s
x = 1234
res = 'integers: ...%d...%-6d...%06d' % (x, x, x)
print(res)
x = 1.23456789
print('%e | %f | %g' % (x, x, x))
print('%-6.2f | %05.2f | %+06.1f' % (x, x, x))
print('%s' % x, str(x))
print('%f, %.2f, %.*f' % (1/3.0, 1/3.0, 4, 1/3.0)) # Указатель '*' - когда размеры не известны, можно применять вычисляемые гирину и точность.
                                                   # 4 - дает точность
                                        # Выражения форматирования, основанные на словаре
print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t Выражения форматирования, основанные на словаре')
print('%(qty)d more %(food)s' % {'qty': 1, 'food': 'spam'})
replay = '''
Greetings...
Hello %(name)s!
Your age is %(age)s'''   # Шаблон с целями подстановки
values = {'name': 'Bob', 'age': 40} # Создание значений для подстановки
print(replay % values) # Выполнение подстановки
food = 'spam'
qty = 10
print('%(qty)d more %(food)s' % vars())
                                        # Оснсовы методов форматирования
print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t Основы методов форматирования')
template = '{0}, {1} and {2}' # По позициям
print(template.format('spam', 'ham', 'eggs'))
template = '{motto}, {pork} and {food}' # По ключевым словам
print(template.format(motto = 'spam', pork = 'ham', food = 'eggs'))
template = '{motto}, {0} and {food}' # По позициям и ключевым словам
print(template.format('ham', motto = 'spam', food = 'eggs'))
template = '{}, {} and {}' # По относительным позициям
print(template.format('spam', 'ham', 'eggs'))
                            # Тоже самое чт ои примеры выше, только по средствам выражения
template = '%s, %s and %s'
print(template % ('spam', 'ham', 'eggs'))
template = '%(motto)s, %(pork)s and %(food)s'
print(template % dict(motto = 'spam', pork = 'ham', food = 'eggs'))
print('{motto}, {0} and {food}'.format(42, motto = 3.14, food = [1, 2, 3]))
X = '{motto}, {0} and {food}'.format(42, motto = 3.14, food = [1, 2])
print(X)
print(X.split(' and '))
Y = X.replace('and', 'but under no circumstances')
print(Y)
                        # Добавление ключей, атрибутов и смещений
print('\n\t\t\t\t\t\t\t\t\t Добавление ключей, атрибутов и смещений')
import sys
print('My {1[kind]} runs {0.platform}'.format(sys, {'kind': 'laptop'})) # Словарь индексируется по ключу kind и затем извлекается атрибут platform из объекта импортированного модуля sys
print('My {map[kind]} runs {sys.platform}'.format(sys = sys, map = {'kind': 'laptop'})) # Делается тоже самое, но вместо позиций применяются ключевые слова
somelist = list('SPAM')
print(somelist)
print('first = {0[0]}, third = {0[2]}'.format(somelist))
print('first = {0}, last = {1}'.format(somelist[0], somelist[-1]))
parts = somelist[0], somelist[-1], somelist[1:3]
print('first = {0}, last = {1}, middle = {2}'.format(*parts))
print('{0:10} = {1:10}'.format('spam', 123.4567))
print('{0:>10} = {1:<10}'.format('spam', 123.4567))
print('{0.platform:>10} = {1[kind]:<10}'.format(sys, dict(kind='laptop')))
print('{0:e}, {1:.3e}, {2:g}'.format(3.14159, 3.14159, 3.14159))
print('{0:f}, {1:.2f}, {2:06.2f}'.format(3.14159, 3.14159, 3.14159))
print('{0:x}, {1:o}, {2:b}'.format(255, 255, 255)) # Шестнадцатиричный, восьмеричный, двоичный
print(bin(255), int('11111111', 2), 0b11111111) # Другие преобразования из/в двоичную
print(hex(255), int('FF', 16), 0xFF) # Другие преобразования в/из шестнадцатиричного
print(oct(255), int('377', 8), 0o377) # Другие рпеобразования в/из восьмеричного
print('{0:.2f}'.format(1 / 3.0)) # Жестко закодированные параметры
print('%.2f' % (1 / 3.0)) # то же самое для выражения
print('{0:.{1}f}'.format(1 / 3.0, 4)) # Получение значений из аргумента
print('%.*f' % (4, 1 / 3.0)) # Тоже самое для выражения
print('{0:.2f}'.format(1.2345)) # Строковый метод
print(format(1.2345, '.2f')) # Встроенная функция format
print('%.2f' % 1.2345) # Выражение

print('%s, %s and %s' % (3.14, 42, [1, 2])) # произвольные типы
print('My %(kind)s runs %(platform)s' % {'kind': 'laptop', 'platform': sys.platform})
print('My %(kind)s rund %(platform)s' % dict(kind = 'laptop', platform = sys.platform))
somelist = list('SPAM')
parts = somelist[0], somelist[-1], somelist[1:3]
print('first = %s, last = %s, middle = %s' % parts)
                                    # Жестко закодированные сылки в обоих случаях
import sys
print('My {1[kind]:<8} runs {0.platform:>8}'.format(sys, {'kind': 'laptop'}))
print('My %(kind)-8s runs %(plat)8s' % dict(kind = 'laptop', plat = sys.platform))
                                    # Заблаговременное создание данных двумя способами
data = dict(platform = sys.platform, kind = 'laptop')
print('My {kind:<8} runs {platform:>8}'.format(**data))
print('My %(kind)-8s runs %(platform)8s' % data)
                                    # Дополнительные возможности
print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t Дополнительные возможности')
print('{0:b}'.format((2 ** 16) - 1)) # код двоичного формата в методе(только)
print(bin((2 ** 16) - 1)) # Другие более универсальные варианты
print('%s' % bin((2 ** 16) -1)) # Подходит для метода и выражения
print('{}'.format(bin((2 ** 16) - 1))) # С относительной нумерацией
print('%s' % bin((2 ** 16) - 1)[2:]) # Вырезание 0b для получения точного эквивалента
print('{:,d}'.format(999999999999)) # Новая возможность метода str.format
                                    # Гибкий синтаксис ссылок
D = dict(name = 'Bob', job = 'dev')
print('{0[name]} {0[job]} {0[name]}'.format(D)) # Метод, ссылки на ключи
print('{name} {job} {name}'.format(**D)) # Метод, аргументы из словаря
print('%(name)s %(job)s %(name)s' % D) # Выражения, ссылки на ключи
print('The {0} side {1} {2}'.format('bright', 'of', 'life'))
print('The {} side {} {}'.format('bright', 'of', 'life'))
print('The %s side %s %s' % ('bright', 'of', 'life'))
print('{0:f}, {1:.2f}, {2:05.2f}'.format(3.14159, 3.14159, 3.14159))
print('{:f}, {:.2f}, {:06.2f}'.format(3.14159, 3.14159, 3.14159))
print('%f, %.2f, %06.2f' % (3.14159, 3.14159, 3.14159))
                                    # Эстетика или практичность
print('%.2f' % 1.2345) # Одиночное значение
print('%.2f %s' % (1.2345, 99)) # Кортеж с множеством значений
print('%s' % 1.23) # Одиночное значение само по себе
print('%s' % (1.23,)) # Одиночное значение в кортеже
print('%s' % ((1.23,),)) # Одиночное значение, являющееся кортежем
                                # метод форматирования
print('{0:.2f}'.format(1.2345)) # Одиночное значение
print('{0:.2f} {1}'.format(1.2345, 99)) # Мноество значений
print('{0}'.format(1.23)) # Одиночное значение, само по себе
print('{0}'.format((1.23,))) # Одиночное значение, являющееся кортежем

def myformat(fmt, args): return fmt % args
print(myformat('%s %s', (88, 89))) # Вызов вашего объекта функции
print(str.format('{} {}', 88, 89)) # Или вызов встроенной функции
          #otherfunction(myformat) # Ваша функция - тоже объект

                                # Списки и словари
print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Списки и словари')

print(len([1, 2, 3])) # Длина
print([1, 2, 3] + [4, 5 ,6]) # Конкатенация
print(['Ni!'] * 4) # Повторение
print(str([1, 2]) + "34") # Преобразование списка в строку, чтобы сработала конкатенация
print([1, 2] + list("34")) # Преобразование строки в список, чтобы сработала конкатенация
print(3 in [1, 2, 3]) # Членство

for x in [1, 2, 3]:             # Итерация
    print(x, end = ' ')

res = [c * 4 for c in 'SPAM'] # Саписковые включения
print(res)

res = []
for c in 'SPAM':                # Эквивалент спискового включения
    res.append(c * 4)
print(res)

print(list(map(abs, [-2, -1, 0, 1, 2]))) # Отображение функции по всей последовательности
L = ['spam', 'Spam', 'SPAM!']
print(L[2]) # Смещения начинаются с нуля
print(L[-2]) # Отрицательные смещения отсчитываются справа
print(L[1:]) # Нарезание извлекает сегменты

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1]) # Достает вложенный подсписок
print(matrix[1][1]) # Достает элемент внутри строки подсписка
print(matrix[2][0])
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(matrix[1][1])
L = ['spam', 'Spam', 'SPAM!']
L[1] = 'eggs' # Присваивание по индексу
print(L)
L[0:2] = ['eat', 'more'] # Присваивание по срезу: удаление + вставка
print(L)

L = [1, 2, 3]
L[1:2] = [4, 5] # Замена/вставка
print(L)
L[1:1] = [6, 7] # Вставка (ничего не заменяет)
print(L)
L[1:2] = [] # Удаление (ничего не вставляет)
print(L)
L= [1]
L[:0] = [2, 3, 4] # Вставить все на место :0, пустой срез в начале
print(L)
L[len(L):] = [5, 6, 7] # Вставить все на место len(L):, пустой срез в конце
print(L)
L.extend([8, 9, 10]) # Вставить все в конец, именованный метод
print(L)
                                                # Вызов списковых методов
print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Вызов списковых методов и сведения о сортировке списков')

L = ['eat', 'more', 'SPAM!']
L.append('please') # Вызов метода дополнения: добавляет элемент в конец
print(L)
L.sort()        # Сортировка элементов списка ('S' < 'e')
print(L)
L = ['abc', 'ABD', 'aBe']
L.sort() # Сортировка со смешанным регистром символов
print(L)
L = ['abc', 'ABD', 'aBe']
L.sort(key=str.lower) # Приведение к нижнему регистру
print(L)
L = ['abc', 'ABD', 'aBe']
L.sort(key=str.lower, reverse=True) # Изменение порядка сортировки
print(L)
L = ['abc', 'ABD', 'aBe']
print(sorted(L, key=str.lower, reverse=True)) # Встроенная функция сортировки
L = ['abc', 'ABD', 'aBe']
print(sorted([x.lower() for x in L], reverse=True)) # Предворительно трансформирует элементы: отличается!
L = [1, 2]
L.extend([3, 4, 5]) # Добавление множества элементов в конец (подобно + на месте)
print(L)
L.pop() # Удаление и возврат последнего элемента (по умолчанию: -1)
print(L)
L.reverse() # Метод обращения списка на месте
print(L)
print(list(reversed(L))) # Встроенная функция обращения списка с результатом (итератор)
L = []
L.append(1)         # Затолкнуть в стек
L.append(2)
print(L)
L.pop()             # Вытолкнуть из стека
print(L)

L = ['spam', 'eggs', 'ham']
print(L.index('eggs'))              # Индекс объекта поиск
L.insert(1, 'toast') # Вставка в позицию
print(L)
L.remove('eggs') # Удаление по значению
print(L)
L.pop(1)    # Удаление по позиции
print(L)
print(L.count('spam')) # Количество вхождений
L = ['spam', 'eggs', 'ham', 'toast']
del L[0] # Удаление одного элемента
print(L)
del L[1:] # Удаление целой секции (То же, что и L[1:] = L[]
print(L)
L = ['Already', 'got', 'one']
L[1:] = []
print(L)
L[0] = []
print(L)







