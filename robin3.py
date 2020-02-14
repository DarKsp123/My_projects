#!/usr/bin/python3
print('Run', 'away!...')
                                    # Обработка ошибок с помощью оператора try
print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Обработка ошибок с помощью оператора try')
while True:                         # начало цикла
    reply = input('Enter text: ')   # Вввод данных пользователя
    if reply == 'stop': break       # Если ввести стоп, закрыть программу
    try:                            # Оператор обработки исключений
        num = int(reply)            # Проверка ввода пользователя на число
    except:                         # Вызов исключения для случаев если пользователь ввел не число
        print('Bad!' * 8)           # Печатаем то что в принте
    else:                           # А если число, то возводим его в квадрат
        print(num ** 2)
print('Bye')

                                        # Вложение кода на три уровня в глубину
print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t Вложение когда на три уровня в глубину')

while True:
    reply = input('Введите текст: ')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('Bad!' * 8)
    else:
        num = int(reply)
        if num <= 20:
            print('low')
        else:
            print(num ** 2)
print('Bye')
