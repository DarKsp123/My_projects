# TODO 1-ое дополнительное задание. Найти наибольшее и наименьшее значение в списке(в кортеже).

#--------------------------------------------------------------------------------------------------

# TODO Задча 1. Написать функци вычисляющую сумму всех чисел находящихся в строке.



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


# -------------------------------------------------------------------------------------------------

# TODO Задача 2. Сложить только четные элементы последовательности и умножить их на поледний элемент последовательности.


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio([0, 1, 2, 3, 4, 5]))

    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")


# ------------------------------------------------------------------------------------------------

# TODO Задача 3. Найти 3 подряд встречающихс слова в строке.



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


# ------------------------------------------------------------------------------------------------------

# TODO Задча 4. Подсчитать кол-во цифр в числе.



if __name__ == '__main__':
    print('Example')
    print(number_length(10))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert number_length(10) == 2
    assert number_length(0) == 1
    assert number_length(4) == 1
    assert number_length(44) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")


# --------------------------------------------------------------------------------------------------------

# TODO Задача 5. Подсчитатиь количество последних нулей в числе.



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

# --------------------------------------------------------------------------------------------------------

#TODO Задача 6. Вернуть заданную строку в обратном порядке.


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

if __name__ == '__main__':
    #print("Example:")
    print(backward_string('123456789'))

    # These "asserts" are used for self-checking and not for an auto-testing
    #assert backward_string('val') == 'lav'
    #assert backward_string('') == ''
    #assert backward_string('ohho') == 'ohho'
    #assert backward_string('123456789') == '987654321'
    #print("Coding complete? Click 'Check' to earn cool rewards!")

# --------------------------------------------------------------------------------------------------------

#TODO Задача 7. Удалить из списка все элементы найденные до первого вхождения заданного числа(Используем условие проверки нахождения числа в списке).
from typing import Iterable




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





if __name__ == '__main__':
    print("Example:")
    print(list(replace_first([1, 2, 3, 4])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")

#--------------------------------------------------------------------------------------------------------

