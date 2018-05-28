is_male = {
  'Оля': False,  # если True, то пол мужской
  'Петя': True,
  'Вася': True,
  'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in names:
    if is_male.values() == False:
        print(name + " мужчина")
    else:
        print(name + " женщина")