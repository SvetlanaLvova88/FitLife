# Проект FitLife - MVP версия 1.0


# 1. Знакомство
# TODO: Спроси у пользователя имя и сохрани в переменную user_name
# TODO: Спроси возраст и сохрани
user_name = str(input('Здравствуйте! Введите Ваше имя: '))
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

# Подсчет воды: вес * 30 мл
# TODO: Рассчитай water_needed
water_needed = user_weight * 30
water_needed_ml = water_needed * 1000  # Перевод в миллилитры
water_needed = round(water_needed_ml, 1)  # круг

# 4. Вывод красивого результата
# TODO: Используй f-строку, чтобы вывести приветствие,
print(f"Привет, {user_name}!")
print(f"Ваш возраст: {user_age}")
print(f"Ваш ИМТ: {bmi:.1f}")
print(f"Ваша норма воды: {water_needed} мл")
print("Расчет окончен. Будьте здоровы!")
