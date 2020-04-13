testArr = [11, 22, 33, 22, 11]
result = testArr[0]
itog = []
#print(result)
for iter in testArr:
    if iter > result:
        result = iter
        itog.append(iter)
        print(result)
print(itog)

x = 'SPAM'
if 'rubbery' in 'shrubbery':
    print(x * 8)            # Выводит 8 раз SPAM
    x += 'NI'               # Добавляет к x NI = SPAM + NI
    if x.endswith('NI'):    # Если x заканчивается на NI то умножаем его на 2 и выводим = SPAMNISPAMNI
        x *= 2
        print(x)            # Выводит SPAMNISPAMNI

A = 't' if 'spam' else 'f' # Непустые строки означают истину
print(A)
A = 't' if '' else 'f' # Пустые ложь
print(A)


x = 'spam'
while x:
    print(x, end=" ")
    x = x[1:]
'''
while True:
    name = input('Enter name: ')
    if name == 'stop': break
    elif not name.isalpha():
        print('Введите буквы, а не числа')
        continue
    age = input('Enter age: ')
    try:
        age = int(age)
    except ValueError:
        print('Введите число')
        continue
    print('Hello', name, '=>', int(age) ** 2)
print('Bye')
'''


y = 11
x = y // 2
while x > 1:                                # Для значения y > 1
    if y % x == 0:                          # Остаток от деления
        print(y, 'has factor', x)           # Имеет сомножитель
        break                               # пропуск else
    x -= 1                                  # Повзволяет проверять значение уменьшая x на 1, находя таким образом сомножитель. Если не найден, то тогда число является простым
else:
    print(y, 'is prime')



L = ['asddasdsa', 'wqeqweqw', 'ewqeqweqeqweq', 'sdfgdfgdfgdf', 'dsgfdgdfgdfg']
c = []
b = 0
for i in L:
    c += i.title().split(',')
    b += 1
    #if i:
    #    c += i.title().split(',')
    #print(c)
#print('Bye')
print(c)



