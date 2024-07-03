#~ USAGE
# cd d:\python_developer
# .\pydev\Scripts\activate
# cd d:\python_developer\lesson_02
#~~~~~~~~~~~~~~~~~~~~~~~~
# python victory.py
#~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ список знаменитостей и их годов рождения
famous_people = [
  ("Александр Сергеевич Пушкин", 1799),
  ("Альберт Эйнштейн", 1879),
  ("Махатма Ганди", 1869),
  ("Мартин Лютер Кинг", 1929),
  ("Стив Джобс", 1955)
]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ функция для отображения результатов игры
def show_results(correct_answers, incorrect_answers):
  total_answers = correct_answers + incorrect_answers
  if total_answers > 0:
    percentage_correct = correct_answers  *  100 / total_answers
    percentage_incorrect = incorrect_answers  *  100 / total_answers
    print(f"Количество правильных ответов: {correct_answers}")
    print(f"Количество ошибок: {incorrect_answers}")
    print(f"Процент правильных ответов: {percentage_correct:.2f}%")
    print(f"Процент неправильных ответов: {percentage_incorrect:.2f}%")
  else:
    print("Ответы не были даны.")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ основная функция викторины
def play_quiz():
  correct_answers = 0
  incorrect_answers = 0
  for famous_person, birth_year in famous_people:
    answer = int(input(f"Введите год рождения {famous_person}: "))
    if answer == birth_year:
      correct_answers += 1
    else:
      incorrect_answers += 1
  show_results(correct_answers, incorrect_answers)

  restart = input("Хотите начать заново? (да/нет): ")
  if restart.lower() == "да":
    play_quiz()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ запуск викторины
play_quiz()
