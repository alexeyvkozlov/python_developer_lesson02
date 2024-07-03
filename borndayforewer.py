#~ USAGE
# cd d:\python_developer
# .\pydev\Scripts\activate
# cd d:\python_developer\lesson_02
#~~~~~~~~~~~~~~~~~~~~~~~~
# python borndayforewer.py
#~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ функция для бесконечного цикла while
def ask_user():
  #~ год рождения А.С. Пушкина
  correct_year = 1799
  #~ день рождения А.С. Пушкина
  correct_day = 6
  #~~~~~~~~~~~~~~~~~~~~~~~~
  is_year = True
  is_day = False
  #~~~~~~~~~~~~~~~~~~~~~~~~
  while True:
    #~~~~~~~~~~~~~~~~~~~~~~~~
    if is_year:
      #~ запрашиваем у пользователя год рождения А.С. Пушкина
      user_input = input("Введите год рождения А.С. Пушкина: ")
      #~ преобразуем введенный год в число для сравнения
      try:
        user_year = int(user_input)
      except ValueError:
        print("Неверный формат года")
        continue
      #~ проверяем, был ли введен правильный год
      if user_year == correct_year:
        is_year = False
        is_day = True
      else:
        print("Неверный год рождения")
      #~~~~~~~~~~~~~~~~~~~~~~~~
      if is_day:
        #~ запрашиваем у пользователя день рождения
        user_birthday = input("Введите день рождения А.С. Пушкина: ")
        #~ преобразуем введенный день в число для сравнения
        try:
          birthday_day = int(user_birthday)
        except ValueError:
          print("Неверный формат дня рождения")
          continue
        #~ проверяем, был ли введен правильный день
        if birthday_day == correct_day:
          print("Верно")
          return
        else:
          print("Неверный день рождения")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ запускаем функцию ask_user
ask_user()