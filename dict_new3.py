# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
# ???
for class_n, class_st in enumerate(school_students, 1):
  names = [name['first_name'] for name in class_st]
  count_name = {name: names.count(name) for name in names}
  values = list(count_name.values())



  for key, value in count_name.items():
    if value == max(values):
      print("Самое частое имя в классе {}: {}".format(class_n, key))


# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша