# Проект FitLife - MVP версия 1.0
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
water_per_kg = 30
constant_ml = 1000

# Приветствие
print("Здравствуйте! Я - ваш помощник по контролю за здоровьем от FitLife.")
print("Прежде чем начнем, мне необходимо кое-что узнать от Вас:")

# 1. Знакомство
user_name = input("Как Вас зовут?")
user_age = int(input("Сколько Вам лет?"))
print()

# 2. Сбор данных
while True:
    user_weight = input("Какой у Вас вес? (в кг)")          # проверка на вес
    try:
        weight_float = float(user_weight)
        if 20 <= weight_float <= 250:
            print(f"Вес {weight_float} кг принят")
            break
        else:
            print("Ошибка: вес не должен быть меньше 20 и больше 250.")
    except ValueError:
        print("Ошибка: необходимо ввести число. Попробуйте еще раз!")
while True:
    user_height = input("Какой Ваш рост?(м)")                # проверка на рост
    try:
        height_float = float(user_height)
        if 1.4 <= height_float <= 2.5:
            print(f"Рост {height_float} м принят.")
            break
        else:
            print("Ошибка: рост должен быть от 1.4 до 2.5 метров.")
    except ValueError:
        print("Ошибка: необходимо ввести число. Попробуйте еще раз!")
print()

# 3. Логика расчетов
bmi = weight_float / (height_float ** 2)                        # расчёт ИМТ
bmi_round = round(bmi, 1)                                     # округление ИМТ
water_ml = weight_float * water_per_kg                      # норма воды мл
water_l = water_ml / constant_ml                            # литры
water_round = round(water_l, 1)  # округление воды

# 4. Вывод красивого результата
print(f"Отчет для пользователя:{user_name}, {user_age} г.")
print(f"Ваш индекс массы тела (ИМТ): {bmi_round}")
print(f"Рекомендуемая норма воды: {water_round} л в день")
print()
print("Расчет окончен,", "Будьте здоровы!", sep="\n")
