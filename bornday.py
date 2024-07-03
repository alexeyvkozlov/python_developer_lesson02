#~ USAGE
# cd d:\python_developer
# .\pydev\Scripts\activate
# cd d:\python_developer\lesson_02
#~~~~~~~~~~~~~~~~~~~~~~~~
# python bornday.py
#~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ запрашиваем у пользователя год рождения А.С. Пушкина
user_input = input("Введите год рождения А.С. Пушкина: ")

#~ преобразуем введенный год в число для сравнения
try:
  user_year = int(user_input)
except ValueError:
  print("Неверный формат года")
  exit()

#~ год рождения А.С. Пушкина
correct_year = 1799
#~ день рождения А.С. Пушкина
correct_day = 6

#~ проверяем, был ли введен правильный год
if user_year != correct_year:
  print("Неверный год рождения")
else:
  #~ если год верен, запрашиваем день рождения
  user_birthday = input("Введите день рождения А.С. Пушкина: ")

  #~ проверяем, был ли введен правильный день рождения
  try:
    birthday_day = int(user_birthday)
    if birthday_day == correct_day:
      print("Верно")
    else:
      print("Неверный день рождения")
  except ValueError:
    print("Неверный формат дня рождения")