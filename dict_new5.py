# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
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

for students in school:
  names = [name['first_name'] for name in students['students']]
  gend = {'девочки': 0, 'мальчики': 0}

  for name in names:
    if is_male[name]:
      gend['мальчики'] += 1
    else:
      gend['девочки'] += 1

  #print(gend)
  for c in students['class']:
    if gend['мальчики'] > gend['девочки']:
      print("Больше всего мальчиков в классе {}".format(students['class']))
      break
    else:
      print("Больше всего девочек в классе {}".format(students['class']))
      break



# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a