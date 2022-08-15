# СТРОКИ.
# 1) строки неизменяемы.

# 2) метод 'str' может преобразовывать числа(int,float) в строки, к примеру:
random_str = str(5)
print(random_str)
    # или
random_str_1 = str([4, 5, 9])
print(random_str_1)

# БАЗОВЫЕ ОПЕРАЦИИ СО СТРОКАМИ В PYTHON:

#1) Конкатенация(сложение):
name = 'Nikolay '
surname = 'Kolb '
lastName = 'Andreevich '
FIO = surname + name + lastName
print(FIO)

#2) Дублирование строки:
double_str = ('kolb' * 2)
print(double_str)
#3) узнать длину строки(количество символов,считая с 0):
print(len('kolb'))

#4) доступ по индексу и срез:
# можно разделить строку побуквенно и перейти к конкретному символу строки,указав его номер в квадратных скобках (начало отсчета с 0)



