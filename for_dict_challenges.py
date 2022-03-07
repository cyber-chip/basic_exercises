# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

from itertools import count

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
count = {}
for student in students:
    for name in student.values():
    # print(name)
        if name in count:
            count[name] += 1
        else:
            count[name] = 1  

for n in count:
    print(n, count[n])            


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

def list(students):
    counts = {}
    for student in students:
      for name in student.values():
        if name in counts:
          counts[name] += 1
        else:
          counts[name] = 1    

    result=sorted(counts.items(), key = lambda item : item[1])
    answer=(result.pop())
    return(answer[0])
print(f'Самое частое имя среди учеников: {list(students)}')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
i=1
for st in school_students:
    counts = {}    
    for student in st:
      for name in student.values():
        if name in counts:
          counts[name] += 1
        else:
          counts[name] = 1    

    result=sorted(counts.items(), key = lambda item : item[1])
    answer=(result.pop())
    print(f'самое встречающееся имя в классе {i} {answer[0]}')
    i+=1


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
males = 0
females = 0

for clas in school:
    number_of_clas = clas['class']
    for students in clas['students']:
        # print(students)
        for f_cl in students.values():
            # print(f_cl)       
            if is_male[f_cl]:
                males += 1
            else:
                females += 1           
    print(f'в классе {number_of_clas} {females} девочки и {males} мальчика')
    males,females = (0,0)


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
males = 0
females = 0

for clas in school:
    number_of_clas = clas['class']
    for students in clas['students']:
        # print(students)
        for f_cl in students.values():
            # print(f_cl)       
            if is_male[f_cl]:
                males += 1
            else:
                females += 1        
    if males > females:
        print(f'Больше всего мальчиков в классе {number_of_clas}')
    else:
        print(f'Больше всего девочек в классе {number_of_clas}')
    males,females = (0,0)

