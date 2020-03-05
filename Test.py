# first programm
import sys

print(sys.platform)
print(2 ** 32)
x = 'Spam!'
print(x * 8)
#input('Press enter to exit: ')

# second step
a = [1, 1, 2, 3, 5, 8, 13, 21, 34,55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print([x for x in a if x in b]) # Находим пересичение в списках (но остануться дубли)

result = list(set(a) & set(b))  # Находит пересичение, но исключает дубли
print(result)

