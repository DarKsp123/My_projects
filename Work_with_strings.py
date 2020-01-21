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


