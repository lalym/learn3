# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
names={}
for student in students:
  if student['first_name'] in names:
    names[student['first_name']]+=1
  else:
    names[student['first_name']]=1

print('Самое частое имя среди учеников: '+ max(names, key=names.get))


# Пример вывода:
# Самое частое имя среди учеников: Маша