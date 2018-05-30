# Задание 1
#Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
names={}
for student in students:
    if student['first_name'] in names:
      names[student['first_name']]+=1
    else:
      names[student['first_name']] = 1

for k,v in names.items():
    print("{}: {}".format(k, v))



