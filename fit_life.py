import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
# Проект FitLife - MVP версия 1.0


# 1. Знакомство
# TODO: Спроси у пользователя имя и сохрани в переменную user_name
# TODO: Спроси возраст и сохрани
user_name = input('Здравствуйте! Введите Ваше имя: ')
user_age = int(input('Введите Ваш возраст: '))


# 2. Сбор данных
# TODO: Запроси вес (в кг) и сохрани в user_weight (тип float)
# TODO: Запроси рост (тип float)
user_weight = float(input('Введите Ваш вес (кг): '))
user_height = float(input('Введите Ваш рост (м): '))

# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
# TODO: Рассчитай bmi (Индекс массы тела)
bmi = user_weight / (user_height ** 2)
bmi = round(bmi, 1)  # округление

# Подсчет воды: вес * 30 мл
# TODO: Рассчитай water_needed
water_needed = round(user_weight * 30 / 1000, 3)

# 4. Вывод красивого результата
# TODO: Используй f-строку, чтобы вывести приветствие,
print(f"Hi, {user_name}!")
print(f"Your age: {user_age}")
print(f"Your BMI: {bmi:.1f}")
print(f"Your water intake: {water_needed} l")
print("Calculation complete. Stay healthy!")
