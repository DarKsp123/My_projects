# TODO 1-ое дополнительное задание. Найти наибольшее и наименьшее значение в списке(в кортеже).
def max_value(elements) -> int:
    if len(elements) > 0:
        null_tuple = elements[0]
        for elem in elements:
            if elem > null_tuple:   # Для нахождения наименьшего значения нужно поменять знак с '>' на '<'
                null_tuple = elem
        return null_tuple
    else:
        return 0


if __name__ == '__main__':
    print('Example')
    print(max_value([1, 2, 3, 44, 56, 9, 10, 13, 23, 11, 38]))


assert max_value([1, 2, 3, 44, 56, 9, 10, 13, 23, 11, 38]) == 56
assert max_value((1, 2, 3, 44, 56, 9, 10, 13, 23, 11, 38)) == 56
assert max_value('') == 0
assert max_value(()) == 0
assert max_value([]) == 0


#-----------------------------------------------------------------------------------------------

# TODO Задча 1. Написать функци вычисляющую сумму всех чисел находящихся в строке.
def sum_numbers(text: str) -> int:
    total = 0
    for line in text.split():
        if line.isdigit():
            total += int(line)
    return total


if __name__ == '__main__':
    print('Example:')
    print(sum_numbers('This picture is an oil on canvas '
                   'painting by Danish artist Anna '
                   'Petersen between 1845 and 1910 year'))



# These "asserts" are used for self-checking and not for an auto-testing
assert sum_numbers('hi') == 0
assert sum_numbers('who is 1st here') == 0
assert sum_numbers('my numbers is 2') == 2
assert sum_numbers('This picture is an oil on canvas '
                   'painting by Danish artist Anna '
                   'Petersen between 1845 and 1910 year') == 3755
assert sum_numbers('5 plus 6 is') == 11
assert sum_numbers('') == 0
print("Coding complete? Click 'Check' to earn cool rewards!")
#-------------------------------------------------------------------------------------------------

# TODO Задача 2. Сложить только четные элементы последовательности и умножить их на поледний элемент последовательности.
def checkio(array: list) -> int:
    result = 0
    if len(array) > 0:
        for i in range(0, len(array), 2):
            result += array[i]
        return result * array[-1]
    else:
        return 0



# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio([0, 1, 2, 3, 4, 5]))

    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
#------------------------------------------------------------------------------------------------

# TODO Задача 3. Найти 3 подряд встречающихс слова в строке.
def checkio(words: str) -> bool:
    count = 0
    for word in words.split():
        if word.isalpha():
            count += 1
            if count == 3:
                return True
        else:
            count = 0
    return False

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))

    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
#------------------------------------------------------------------------------------------------------

#TODO Задча 4. Подсчитать кол-во цифр в числе.
def number_length(a: int) -> int:
    count = 0
    if a == 0:
        return 1
    while a > 0:
        count += 1
        a = a // 10
    return count

if __name__ == '__main__':
    print('Example')
    print(number_length(10))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert number_length(10) == 2
    assert number_length(0) == 1
    assert number_length(4) == 1
    assert number_length(44) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
#--------------------------------------------------------------------------------------------------------

#TODO Задача 5. Подсчитатиь количество последних нулей в числе.
def end_zeros(num: int) -> int:
    count = 0
    if num == 0:
        return 1
    while num % 10 == 0:
        num //= 10
        count += 1
    return count


if __name__ == '__main__':
    print("Example:")
    print(end_zeros(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")

#TODO Задача 6. Вернуть заданную строку в обратном порядке.
def backward_string(val: str) -> str:
    backward_val = val[::-1]
    return backward_val


if __name__ == '__main__':
    print("Example:")
    print(backward_string('val'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string('val') == 'lav'
    assert backward_string('') == ''
    assert backward_string('ohho') == 'ohho'
    assert backward_string('123456789') == '987654321'
    print("Coding complete? Click 'Check' to earn cool rewards!")

#TODO Задача 6.1. Вернуть заданную строку в обратном порядке.(Классический алгоритм)
def backward_string(val: str) -> str:
    backward_val = list(val)
    for i in range(len(val) // 2):
        tmp = backward_val[i]
        backward_val[i] = backward_val[len(val) - i - 1]
        backward_val[len(val) - i - 1] = tmp
    return ''.join(backward_val)


if __name__ == '__main__':
    print("Example:")
    print(backward_string('val'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string('val') == 'lav'
    assert backward_string('') == ''
    assert backward_string('ohho') == 'ohho'
    assert backward_string('123456789') == '987654321'
    print("Coding complete? Click 'Check' to earn cool rewards!")

#--------------------------------------------------------------------------------------------------------

#TODO Задача 7. Удалить из списка все элементы найденные до первого вхождения заданного числа(Используем условие проверки нахождения числа в списке).
from typing import Iterable


def remove_all_before(items: list, border: int) -> Iterable:
    if border in items:
        index = items.index(border)
        return items[index:]
    else:
        return items


if __name__ == '__main__':
    print("Example:")
    print(list(remove_all_before([1, 2, 3, 4, 5], 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
    assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
    assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
    assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    assert list(remove_all_before([], 0)) == []
    assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7, 7, 7, 7, 7, 7, 7, 7, 7]
    print("Coding complete? Click 'Check' to earn cool rewards!")


#TODO Задача 7.1. Удалить из списка все элементы найденные до первого вхождения заданного числа(Используем цикл for).
from typing import Iterable


def remove_all_before(items: list, border: int) -> Iterable:
    for elem in range(0, len(items)):
        if items[elem] == border:
            return items[elem:]
    return items

if __name__ == '__main__':
    print("Example:")
    print(list(remove_all_before([1, 2, 3, 4, 5], 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
    assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
    assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
    assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    assert list(remove_all_before([], 0)) == []
    assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7, 7, 7, 7, 7, 7, 7, 7, 7]
    print("Coding complete? Click 'Check' to earn cool rewards!")


#TODO Задача 7.2. Удалить из списка все элементы найденные до первого вхождения заданного числа(Используем блок вызова исключений try).
from typing import Iterable


def remove_all_before(items: list, border: int) -> Iterable:
    try:
        # search for the item
        index = items.index(border)
        print(f'the border is found at index {index}')
        return items[index:]
    except ValueError:
        print('border not present')
        return items


if __name__ == '__main__':
    print("Example:")
    print(list(remove_all_before([1, 2, 3, 4, 5], 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
    assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
    assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
    assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    assert list(remove_all_before([], 0)) == []
    assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7, 7, 7, 7, 7, 7, 7, 7, 7]
    print("Coding complete? Click 'Check' to earn cool rewards!")

#--------------------------------------------------------------------------------------------------------

#TODO Задача 8. Проверить все символы на вхождение в верхний регистр.
def is_all_upper(text: str) -> bool:
    if text.isupper() or text.strip() == '':
        return True
    elif text.isdigit():
        return True
    else:
        return False


if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == True
    assert is_all_upper('123') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")

#--------------------------------------------------------------------------------------------------------

#TODO Задача 9. Поменять местами первый и последний элемент списка
from typing import Iterable


def replace_first(items: list) -> Iterable:
    for elem in range(len(items) - 1):
        tmp = items[elem]
        items[elem] = items[elem + 1]
        items[elem + 1] = tmp
    return items


if __name__ == '__main__':
    print("Example:")
    print(list(replace_first([1, 2, 3, 4])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")

#--------------------------------------------------------------------------------------------------------

# TODO Задача 10. Найти наиболдьшую цифру в числе.
def max_digit(number: int) -> int:
    max_number = 0
    if number == 0:
        return 0
    while number > 0:
        if number % 10 > max_number:
            max_number = number % 10
        number //= 10
    return max_number


if __name__ == '__main__':
    print("Example:")
    print(max_digit(634))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")

#--------------------------------------------------------------------------------------------------------

