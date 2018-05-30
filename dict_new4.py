# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
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
# ???
# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


for students in school:
  names = [name['first_name'] for name in students['students']]
  gend = {'девочки': 0, 'мальчики': 0}

  for name in names:
    if is_male[name]:
      gend['мальчики'] += 1
    else:
      gend['девочки'] += 1

  print('В классе {} {} девочки и {} мальчика'.format(students['class'], gend['девочки'], gend['мальчики']))
