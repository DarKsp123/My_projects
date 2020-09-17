'''
import sys
print(sys.path)
x = 2
print(x ** 32)


D = {'a': 1, 'b': 2, 'c': 3}
for key in D:
    print(D[key])
'''

mass = [1, 2 ,3 ,4 ,5, 50, 60, 70, 90, 100, 60, 60]
a = 60
count = -1
for i in mass:
    count += 1
    if i == a:
        print(count, '-> ', mass[count])

if a in mass:
    print(mass.index(a))

print(mass.count(a))


import itertools as it

mass = [200000.59, 155000.00, 55600.00, 45400, 399.41]
a = 200400.00
for i in range(1, len(mass) + 1):
    comb = it.combinations(mass, 2) # it.permutations - учитывает и обратные перестановки.
    result = [i for i in comb if sum(i) == a]
    print(result)


def summs(answer, *dig):
    res = []
    for i in dig:
        for j in dig:
            if i + j == answer and (i, j) not in res and (j, i) not in res:
                res.append((i, j))
    return res


print(summs(13, *range(100)))


# TODO Полный алдгоритм оброботки всех возможных вариантов для суммы чисел
import itertools

def summs(answer, *dig):

    res = []
    for i in range(1, answer + 1):
        for j in itertools.combinations_with_replacement(list(dig), i):
            if sum(list(j)) == answer:
                res.append(j)
    return res


print(summs(5, *range(1, 3)))
