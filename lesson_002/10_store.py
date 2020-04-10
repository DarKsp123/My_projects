#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

#----------------------------Столы-------------------------------#
table_code = goods['Стол']
table_item_0 = store[table_code][0]
table_item_1 = store[table_code][1]
table_quantity_0 = table_item_0['quantity']
table_quantity_1 = table_item_1['quantity']
table_price_0 = table_item_0['price']
table_price_1 = table_item_1['price']
table_quantity = table_quantity_0 + table_quantity_1
table_price = (table_quantity_0 * table_price_0) + (table_quantity_1 * table_price_1)
print('Стол -', table_quantity, 'шт, стоимость', table_price, 'руб')

#--------------------------Диваны-------------------------------#
couch_code = goods['Диван']
couch_item_0 = store[couch_code][0]
couch_item_1 = store[couch_code][1]
couch_quantity_0 = couch_item_0['quantity']
couch_quantity_1 = couch_item_1['quantity']
couch_quantity = couch_quantity_0 + couch_quantity_1
couch_price_0 = couch_item_0['price']
couch_price_1 = couch_item_1['price']
couch_price = (couch_quantity_0 * couch_price_0) + (couch_quantity_1 * couch_price_1)
print('Диваны -', couch_quantity, 'шт, стоимость', couch_price, 'руб')

#--------------------------Стулья-------------------------------#
chair_code = goods['Стул']
chair_item_0 = store[chair_code][0]
chair_item_1 = store[chair_code][1]
chair_item_2 = store[chair_code][2]
chair_quantity_0 = chair_item_0['quantity']
chair_quantity_1 = chair_item_1['quantity']
chair_quantity_2 = chair_item_2['quantity']
chair_quantity = chair_quantity_0 + chair_quantity_1 + chair_quantity_2
chair_price_0 = chair_item_0['price']
chair_price_1 = chair_item_1['price']
chair_price_2 = chair_item_2['price']
chair_price = (chair_price_0 * chair_quantity_0) + (chair_price_1 * chair_quantity_1) + (chair_price_2 * chair_quantity_2)
print('Стулья -', chair_quantity, 'шт, стоимость', chair_price, 'руб')

print('\n\t\t\t\t\t\t\t\t\t\t\t Теперь с помощью цикла')
#-------------------------------------- Решение с помощью циклов--------------------#
for key, value in goods.items():
    quantity = 0
    price = 0
    for store_item in store[value]:
        quantity += store_item['quantity']
        price += store_item['price'] * store_item['quantity']
    print(key, '-', quantity, 'шт, стоимость', price, 'руб')



##########################################################################################
# ВНИМАНИЕ! После того как __ВСЯ__ домашняя работа сделана и запушена на сервер,         #
# нужно зайти в ЛМС (LMS - Learning Management System ) по адресу http://go.skillbox.ru  #
# и оформить попытку сдачи ДЗ! Без этого ДЗ не будет проверяться!                        #
# Как оформить попытку сдачи смотрите видео - https://youtu.be/qVpN0L-C3LU               #
##########################################################################################






