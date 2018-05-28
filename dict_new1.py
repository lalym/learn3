# Задание 1
#Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
rv=str(len([x for x in students if x['first_name'] == 'Вася']))
rp=str(len([x for x in students if x['first_name'] == 'Петя']))
rm=str(len([x for x in students if x['first_name'] == 'Маша']))
print("Вася: "+rv)
print("Петя: "+rp)
print("Маша: "+rm)
