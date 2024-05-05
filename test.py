def string_to_int(s): # добавить обработку ValueError
    try:
        return int(s)
    except ValueError:
        return f'ошибка: нельзя преобразовать "{s}" в целое число'


def read_file(filename): # добавить обработку FileNotFoundError, IOError
    try:
        with open(filename, 'r', encoding = 'utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return f'ошибка: не удалось найти файл {filename}'
    except IOError:
        return f'ошибка ввода\вывода при работе с файлом {filename}'


def divide_numbers(a, b): # добавить обработку ZeroDivisionError, TypeError
    try:
        return a / b
    except ZeroDivisionError:
        return f'ошибка: нельзя делить на ноль'
    except TypeError:
        return f'ошибка: недопустимое значение параметра'


def access_list_element(lst, index): # добавить обработку IndexError, TypeError
    try:
        return lst[index]
    except IndexError:
        return f'ошибка: индекс {index} находится вне диапазона списка'
    except TypeError:
        return f'возможные ошибки: объект {lst} не итерируемый, либо индекс передан с ошибкой'



#проверка работы функции def string_to_int(s)
print(string_to_int("88 + 0"))
print(string_to_int(111.7))
print()


#проверка работы функции def read_file(filename)
print(read_file('test.txt'))
print(read_file('test1.txt'))
print()


#проверка работы функции def divide_numbers(a, b)
print(divide_numbers(1,'0'))
print(divide_numbers(1,0))
print(divide_numbers(1,555))
print()


#проверка работы функции def access_list_element(lst, index)
lst = ['sun', 3, 22]
print(access_list_element(lst, 6))

lst = 4444557889
print(access_list_element(lst, 6))
