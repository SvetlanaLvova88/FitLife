import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
# Проект FitLife - MVP версия 1.0

K_WATER = 30
K_ML = 1000
# 1. Знакомство
# TODO: Спроси у пользователя имя и сохрани в переменную user_name
# TODO: Спроси возраст и сохрани
user_name = input('Здравствуйте! Введите Ваше имя: ')
while not user_name:
    print('Вы не ввели имя')
    user_name = input('Введите имя еще раз: ')

user_age = int(input('Введите Ваш возраст: '))
while user_age < 0:
    print('Вы ввели отрицательное значение')
    user_age = int(input('Введите возраст еще раз: '))


# 2. Сбор данных
# TODO: Запроси вес (в кг) и сохрани в user_weight (тип float)
# TODO: Запроси рост (тип float)
user_weight = float(input('Введите Ваш вес (кг): '))
while user_weight < 0:
    print('Вы ввели отрицательное значение')
    user_weight = float(input('Введите Ваш вес (кг) еще раз: '))
while user_weight > 636:
    print('У Джона Брауэра Миннока был вес меньше')
    user_weight = float(input('Введите Ваш вес (кг) еще раз: '))

user_height = float(input('Введите Ваш рост (м): '))
while user_height < 0:
    print('Вы ввели отрицательное значение')
    user_height = float(input('Введите Ваш рост (м) еще раз: '))
while user_height > 2.72:
    print('Ого, Вы выше самого Роберта Уoдлоу')
    user_height = float(input('Введите Ваш рост (м) еще раз: '))


# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
# TODO: Рассчитай bmi (Индекс массы тела)
bmi = user_weight / (user_height ** 2)
bmi = round(bmi, 1)  # округление
if bmi < 18.5:
    print('Недостаточная масса тела')
elif bmi <= 24.9:
    print('Нормальная масса тела')
elif bmi <= 29.9:
    print('Избыточная масса тела')
elif bmi <= 34.9:
    print('Ожирение I степени')
elif bmi <= 39.9:
    print('Ожирение II степени')
else:
    print('Ожирение III степени')


# Подсчет воды: вес * 30 мл
# TODO: Рассчитай water_needed
water_needed = round(user_weight * K_WATER / K_ML, 3)

# 4. Вывод красивого результата
# TODO: Используй f-строку, чтобы вывести приветствие,
print(f"Отчет для {user_name}!")
print(f"Ваш возраст: {user_age}.")
print(f"Ваш индекс массы тела: {bmi:.1f}.")
print(f"Рекомендуемая норма воды в сутки: {water_needed} л.")
print("Расчет окончен! Будьте здоровы!")
