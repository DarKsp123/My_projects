import os

directory_1 = os.listdir(r'C:\Сверка\2.4 БГУ для МБУ')
directory_2 = os.listdir(r'C:\Сверка\МИНТРУД')

result = list(set(directory_1) - set(directory_2))
print('C:\Сверка\\2.4 БГУ для МБУ\n' + '\n'.join(result))


