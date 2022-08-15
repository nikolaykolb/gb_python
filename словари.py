dict_for_example = {'Three': 3, 'Five hundred and eleven': 511, 'fifty-four': 54}
print(dict_for_example)
# словари в Python - встроенный и изменяемый класс
# Основное применение словаря - это хранение значения с некоторым ключом и возможностью извлечения значения из словаря,заданного ключом
# Обращаться к ключам и значениям можно с помощью методов
# dict.keys() и dict.values()

# Проверка наличия значения в словаре с помощью ключа
'Five hundred and eleven' in dict_for_example
print(True or False)

# обновление ключа
# обновление ключа не влият на порядок
dict_for_example['Three'] = 43
print(dict_for_example)

# Удаление ключа из словаря с помощью функции del
del(dict_for_example['fifty-four'])
print(dict_for_example)
# Если после удаления ключа, мы хотим обновить ключ, то он добавится в конец словаря вместе со значением
dict_for_example['fifty-four'] = None
print(dict_for_example)

# Также мы можем записывать ключи и значения словаря в списки, используя функцию list()
# К примеру:
d = list(dict_for_example.values())
print(d)  # в списке d будут значения ключей словаря dict_for_example

s = list(dict_for_example.keys())
print(s)  # в списке s будут ключи словаря dict_for_example

d = {'coding': 'good', 'thinking': 'better'}
print(d.get('coding'))
# 'good' returned

d = {1: '001', 2: '010', 3: '011'}
print(d.get(4, "Not found"))
# since 4 is not in keys, it'll print "Not found"

dict_2 = {0: 'name', 1: 'surname', 2: 'address'}
print(dict_2.setdefault(3, 'gender'))
print(dict_2)
# setdefault works like append() method in lists and add key with value to our dictionary

first_dict = {0: ' Dmitriy', 1: 'Parshutkin', 2: 'Nikolaevich'}
second_dict = {3: 'Ekaterina', 4: 'Molodkovets', 5: 'Stanislavovna'}
first_dict.update(second_dict)
print(first_dict)
# update method works like 'extend()' method in list data type


data_base = {'nickname': 'Nikolas2000', 'age': '17', 'location': 'Earth'}
for key, value in data_base.items():
    print(f'{key}={value}')
# метод items испульзуем для итерации пар(ключ+ значение) в словаре


for item in data_base.items():
    print(item, end=' -> ')
    key, value = item
    print(f'{key} = {value}')
# метод items() возвращает данные в кортеже вида : (<key>, <value>)


