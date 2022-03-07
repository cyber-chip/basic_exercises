# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

from unicodedata import name

names = ['Оля', 'Петя', 'Вася', 'Маша']
print("Задание 1")
print('\n'.join(names))



# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём
# Пример вывода:
# Оля: 3
# Петя: 4
print("Задание 2")
names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in names:
	print(name, len(name))

# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

is_male = {
    'Оля': False,  # если False, то пол женский
    'Петя': True,  # если True, то пол мужской
    'Вася': True,
    'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']
print("Задание 3")
for name in names:
    if name not in is_male:
         print(f'{name} is not in the dictionary')
    elif is_male[name]:
        print(f'{name} male')
    else:
        print(f'{name} female')


    
# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# Группа 1: 2 ученика.
# Группа 2: 4 ученика.

groups = [
    ['Вася', 'Маша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
    ['Оля', 'Петя', 'Гриша'],
]
user_groups = len(groups)
groups_count = len(groups)
members_groups_count = [len(inner_group) for inner_group in groups]

print("Задание 4")
print(f'Всего {len(groups)} группы')
i = 0
while i < len(groups):
	print(f'В группе {len(groups[i])} ученика')
	i += 1



# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят
# Пример вывода:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]
print("Задание 5")
for i, inner_group in enumerate(groups):
    names = ', '.join(inner_group)
    print(f'Группа {i+1} : {names}')