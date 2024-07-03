#~ USAGE
# cd d:\python_developer
# .\pydev\Scripts\activate
# cd d:\python_developer\lesson_02
#~~~~~~~~~~~~~~~~~~~~~~~~
# python variables.py
#~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ сотрудник
name = 'Иван'  #~ строка
age = 45       #~ целое число
salary = 40.5  #~ число с плавающей точкой
has_children = True #~ логический тип

print('Сотрудник:')
print(f'  имя: {name}, строка: тип: {type(name)}')
print(f'  возраст: {age}, целое число: тип: {type(age)}')
print(f'  заработная плата: {salary}, число с плавающей точкой: тип: {type(salary)}')
print(f'  есть дети: {has_children}, логический тип: тип: {type(has_children)}')
