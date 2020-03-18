# Задача № 1
# Выведите все элементы, которые меньше 5
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
result = [c for c in a if c < 5]
print(result)

# Задача № 2
#Даны списки:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
result = []
for elem in a:
    if elem in b:
        result.append(elem)
print(result)
result = [elem for elem in a if elem in b]
print(result)

result = list(set(a) & set(b))
print(result)

# Задача № 3
# Отсортируйте словарь по значению в порядке возрастания и убывания.
# В порядке возрастания
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
my_dict = list(d.items())
print(my_dict)
my_dict.sort(key= lambda key: key[1])
print(my_dict)
for key in my_dict:
    print(key[0], '=>', key[1])

# В порядке убывания
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
my_dict = list(d.items())
print(my_dict)
my_dict.sort(key = lambda keys: keys[1])
print(my_dict)
for keys in my_dict[::-1]:
    print(keys[0], '=>', keys[1])
# Задача № 4
#Напишите программу для слияния нескольких словарей в один.
