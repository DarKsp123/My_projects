# TODO Задча 1. Написать функци вычисляющую сумму всех чисел находящихся в строке.
def sum_numbers(text:str) -> int:
    total = 0
    for value in text.split():
        if value.isdigit():
            total += int(value)
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
def checkio(arry: list) -> int:
    result = 0
    if len(arry) > 0:
        for i in range(0, len(arry), 2):
            result += arry[i]
        return result * arry[-1]
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

