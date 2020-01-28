# Работа со строками

line = 'aaa,bbb,ccc,dd'
print(line.split(','))
S = 'spam'
print(S.upper())
print(S.isalpha())
print(S.isdigit())
line = 'aaa,bbb,ccc,dd\n'
print(line)
print(line.rstrip())  # Удаление пробелов в конце строки
print(line.rstrip().split(',')) # Удаление пробелов в конце строки + Разбиение разделителем
print('%s, eggs, and %s' % ('spam', 'SPAM!')) # Метод форматирования
print('{0}, eggs, and {1}'.format('spam', 'SPAM!')) # Метод форматирования
print('{}, eggs, and {}'.format('spam', 'SPAM!')) # Метод форматирования
print('{:,.2f}'.format(296999.2567)) # Разделитель, десятичные цифры
print('%.2f | %+05d' % (3.14159, -42)) # Цифры, дополнение, знаки
# print(dir(line)) # Выводит все методы и функции для line
print(S.__add__('NI!\n\t\t\t\t\tДальше идет работа со списками')) # Метод конкатенации(Сложения = S + 'NI!')
# print(help(str)) # Выводит подсказку по методам и функциям того или иного ТИПА данных)

                                        # Работа со списками

L = [123, 'spam', 1.23] # Список из трех элементов разного типа
print(len(L)) # Кол-во элементов в списке
print(L)
L.append('NI') # Добавление объекта в конец списка
print(L)
L.pop(2) # Удаление элемента из середины
print(L)
L.insert(0,'SPAM!') # Вставляет элемент в произвольную позицию по индексу
print(L)
L.remove('spam') # Удаляем элемент из списка по его названию
print(L)
S = ['Hellow', 'World!', 'Python']
L.extend(S) # Вставляем один список в конец другова
print(L)
M = ['bb', 'aa', 'cc']
print(M)
M.sort() # Упорядочивание списка по возрастанию
print(M)
M.reverse() # Обращается список по убыванию
print(M)
print(L)
L[3] = 'Goodbye'
print(L)
M = [[1, 2, 3],   # Матрица в виде вложенных списков
     [4, 5, 6],
     [7, 8, 9]]
print(M)
print(M[1]) # Получаем вторую строку матрицы
print(M[1][2]) # Получение строку 2 и затем элемент 3 внутри этой строки
                         # Работа с выражениями спискового включения(list comprehension) - столбцами матрицы'
print('\n\t\t\t\t\t\tРабота с выражениями спискового включения(list comprehension) - столбцами матрицы')

col2 = [row[1] for row in M] # Выводим второй стобец матрицы
print(col2)
col2 = [row[1] + 1 for row in M] # Добавляем 1 к каждому элементу второго стобца матрицы
print(col2)
col2 = [row[1] for row in M if row[1] % 2 == 0] # Отфильтровать нечетные элементы
print(col2)

diag = [M[i][i] for i in [0, 1, 2]] # Собрать диагональ из матрцы
print(diag)

doubles = [c * 2 for c in 'spam'] # Повторить символы в строке
print(doubles)

print(list(range(4))) # От 0..3
print(list(range(-6, 7, 2))) # от -6 до +6 с шагом 2

math = [[x ** 2, x ** 3] for x in range(4)] # множество значений, фильтры if
print(math)

math = [[x, x / 2, x * 2] for x in range(-6, 7, 2) if x > 0] # множество значений, фильтры if(задаем матрицу по формуле)
print(math)

G = (sum(row) for row in M)
print(next(G))

print(list(map(sum, M))) # Отоброзить sum на элементы в М

                              # Создание множеств и словарей
print('\n\t\t\t\t\t\t\t\t\t\t\t\t\tСоздание множеств и словарей')

print({sum(row) for row in M}) # Создать множество сумм элементов в строках
print({i : sum(M[i]) for i in range(3)}) # Создать таблицу ключей / значений сумм элементов в строках
print([ord(x) for x in 'spaam']) # Выводим порядковый номер(десятичный) символа, согласно ASCII
print({ord(x) for x in 'spaam'}) # множество с удаленными дубликатами значений порядкового номера символов в таблице ASCII
print({x : ord(x) for x in 'spaam'}) # Словарь с уникальными ключами
G = (ord(x) for x in 'spaam') # Генератор значений
print(next(G))                # Выводим значения генертора, без функ-ции next(движение по циклу) не работает

                                        # Словари
print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tСловари')

D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
print(D['food']) # Извлечь значение, связанное с ключом 'food'
D['quantity'] += 1 # Добавить 1 к значению, связанному с ключом 'quantity'
print(D)

D = {}
D['name'] = 'Bob'
D['job'] = 'dev'                  # Присвоение приводит к созданию ключей
D['age'] = 40
print(D)
print(D['name'])

bob1 = dict(name = 'Bob', job = 'dev', age = 40) # Создаем ключевые слова(словарь)
print(bob1)

bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40])) # Связывание вместе(создается словарь)
print(bob2)

rec = {'name': {'first': 'Bob', 'last': 'Smith'},   # Вложенные списки(сложноструктурированные)
       'jobs': ['dev', 'mgr'],
       'age': 40.5}
print(rec['jobs'][0])
rec['jobs'].append('janitor') # Добавляем значение в атрибут словаря jobs
print(rec)

rec = 0 # Очищение области памяти занимаемая объектом(в нашем случае rec)
print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t Недостоющие ключи: проверка if')
                                    # Недостающие ключи: проверки if

D = {'a': 1, 'b': 2, 'c': 3}
print(D)
D['e'] = 99 # Присвоение новому ключу - увеличивает словарь
print(D)

# if not 'f' in D:                                #Проверка атрибута f в словаре D(так как не выдает ошибку)
#    print('missing')


value = D.get('x', 0)                     # Избегаем обращения к несуществующим ключам с помощью метода get
print(value)
value = D['x'] if 'x' in D else 0         # Избегаем обращения к несуществующим ключам с помощью проверки значения через if/else
print(value)

                                            # Цикл for

print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t Цикл for')

Ks = list(D.keys()) # Неупорядоченный список ключей
print(Ks)
Ks.sort() # Сортировка ключей

for key in Ks:
    print(key, '=>', D[key])    # Цикл for проход по отсартированным ключам


D = {'a': 1, 'c': 3, 'b': 2}
print(D)
for key in sorted(D):
    print(key, '=>', D[key])

for c in 'spam':
    print(c.upper()) # Проходит по символам в строке и выводит символы в верхнем регистре

x = 4
while x > 0:
    print('spam!' * x)
    x -= 1
                            # Итерация и оптимизация
print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t Итерация и оптимизация')

squares = [x ** 2 for x in [1, 2, 3, 4, 5]] # Списковое включение вычисляющее квадраты для списка чисел
print(squares)
squares = []
for x in [1, 2, 3, 4, 5]:    # Тоже самое только через отдельный цикл for
    squares.append(x ** 2)
print(squares)

                            # Кортежи(Не изменяемы списки). Хорош использовать, если вы хотите написать программу
                            # без каких либо изменений в нее
print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Кортежи')

T = (1, 2, 3, 4) # Кортеж из 4 элементов
print(T)
print(len(T)) # Вывести длину кортежа
T = T + (5, 6) # Конкатенация
print(T)
print(T[5]) # Индексация, нарезание и т.д.
print(T.index(4)) # Методы(вызываемые методы в данном случае index) кортежей. 4 обнаруживается по смещению 3
print(T.count(4)) # Еще один вызываемы метод кортежей(count). 4 обнаруживается один раз

T = (2,) + T[1:] # Создаем новый кортеж для нового значения. Значение вставляется так, что отбрасываются начальные символы(T[1:]
print(T)
T = 'spam', 3.0, [11, 22, 33]
print(T[2][2])

                                        # Файлы
print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Файлы')

f = open('data.txt', 'w') # Создать новый файл в режиме записи
f.write('Hellow\n') # Записать в него строки символов
f.write('world\n')
f.close() # Закрыть файл для сбрасывания буферов вывода на диск
f = open('data.txt') # 'r' (чтение) - стандартный режим обработки
text = f.read() # Прочитать все содержимое файла в строку
print(text)
print(text.split()) # Содержимое файла всегда строка
# print(dir(f)) Показывает все методы
# print(help(f.seek)) Описание методов по средстав help
for line in open('data.txt'): # Вывод данных в файле строка за строкой
    print(line)

                                    # Двоичные файлы(удобны для обработки медиаданных, доступа к данным)
print('\n\t\t\t\t\t\t\t\t\t\t\t\t Двоичные файлы(удобны для обработки медиаданных, доступа к данным)')

import struct
packed = struct.pack('>i4sh', 7, b'spam', 8) # создать упакованные двоичные данные
print(packed) # 10 байтов, не объекты и не текст

file = open('data.bin', 'wb') # Открыть двоичный файл для записи
file.write(packed) # Записатьупакованные двоичные данные
file.close()
print(file)
data = open('data.bin', 'rb').read() # Открыть/прочитать двоичный файл данных
print(data)
print(data[4:8]) # Нарезать байты в середине
print(list(data)) # Последовательность 8 битных данных
print(struct.unpack('>i4sh', data)) # Снова распаковать в объекты

                                    # Файлы с текстом Unicode стр 156-158(Важная тема для кодировки/декодировки)
print('\n\t\t\t\t\t\t\t\t\t\t\t\t Файлы с текстом Unicode')

S = 'sp\xc4m' # Текст Unicode, отличающийся от ASCII
print(S)
print(S[2]) # Последовательность символов
file = open('unidata.txt', 'w', encoding='utf-8') # Записать/закодировать текст UTF-8
print(file.write(S)) # Записано 4 символа
file.close()
text = open('unidata.txt', encoding='utf-8').read() # Прочитать/декодировать текст UTF-8
print(text)
print(len(text))

raw = open('unidata.txt', 'rb').read() # Читать закодированные байты
print(raw)
print(len(raw)) # 5 байтов в кодировке UTF-8
                    # При получение закодированного сообщения в электронной почте или через
                    # сетевое подключение можно кодировать/декодировать в ручную
print(text.encode('utf-8')) # В ручную кодировать в байты
print(raw.decode('utf-8')) # В ручную декодировать в строку
                        # Кодирование в другие кодировки
print(text.encode('latin-1')) # Байты отличаются от других
print(text.encode('utf-16')) # Байты отличаются от других
print(len(text.encode('latin-1')), len(text.encode('utf-16')))
print(b'\xff\xfes\x00p\x00\xc4\x00m\x00'.decode('utf-16')) # Декодируются в ту же самую строку
                                        # Чтение декодирование в Python 2.X
import codecs
print(codecs.open('unidata.txt', encoding='utf-8').read()) # Python 2.X читать/декодировать текст
print(open('unidata.txt', 'rb').read()) # Читать низкоуровневые байты
print(open('unidata.txt').read()) # Так же низкоуровневые/декодирование

                                # Прочие основные типы стр.158
print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Прочие основные типы')
# Множества вызываются с помощью встроенной функции set
X = set('spam') # Создать множество из последовательности
Y = {'h', 'a', 'm'} # Создать мнодество с помощью литералов множеств
print(X, Y) # Кортеж из двух множеств без круглых скобок
print(X & Y) # Пересечение
print(X | Y) # Объединение
print(X - Y) # Разность
print(X > Y) # Надмножество
print({n ** 2 for n in [1, 2, 3, 4]}) # Включение множеств
print(list(set([1, 2, 1, 3, 1]))) # Фильтрация дубликатов(возмрожно неупорядоченных)
print(set('spam') - set('ham')) # Нахождение разностей в коллекциях
print(set('spam') == set('asmp')) # Нейтральная к порядку проврка(Равенство 'spam' == 'asmp' дает False)
print('p' in set('spam'), 'p' in 'spam', 'ham' in ['eggs', 'spam', 'ham']) # Проверка челенства в in
print(1 / 3) # Математика с плавающей точкой
print((2 / 3) + (1 / 2))
import decimal # Десятичные числа: фиксированная точность
d = decimal.Decimal('3.141')
print(d + 1)
decimal.getcontext().prec = 2
print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))
from fractions import Fraction # Дроби: числитель + знаменатель
f = Fraction(2, 3)
print(f + 1)
print(f + Fraction(1, 2))
                                # Булевские значения
print(1 > 2, 1 < 2) # Булевские значения
print(bool('spam')) # Булевское значение объекта
X = None # Заполнитель None
print(X)
L = [None] * 100 # Инициализировать список сотней объектов None
print(L)
                                        # Как нарушить гибкость кода(Объект типа type)
print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Как нарушить гибкость кода(Объект типа type)')
print(type(L)) # Типом L является list
print(type(type(L))) # Даже типы явлюятся объектами
if type(L) == type([]): # Проверка типа при необходимости
    print('yes')
if type(L) == list: # Использование имени типа
    print('yes')
if isinstance(L, list): # Объектно-ориентированная проверка
    print('yes')

                                        # Классы, определяемы пользователем. стр. 161
print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Классы, определяемые пользователем стр. 161')

class Worker:
    def __init__(self, name, pay): # инициализировать при создание
        self.Name = name # self - новый объект
        self.pay = pay
    def lastName(self):
        return self.Name.split() [-1] # Разбить строку по пробелам
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent) # Обновить pay на месте
bob = Worker('Bob Smith', 50000) # Создать два экземпляра
sue = Worker('Sue Jones', 60000) # Каждый имеет атрибут name и pay
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

a = 3       # Имя создается: не объявляется за ранее
b = 4
print(a + 1, a - 1)


















