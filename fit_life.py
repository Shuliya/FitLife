# Проект FitLife - MVP версия 1.0
WATER_PER_KG = 30
CONSTANT_ML = 1000

print("Здравствуйте! Я - ваш помощник по контролю за здоровьем от FitLife.")
print("Прежде чем начнем, мне необходимо кое-что узнать от Вас:")
user_name = input("Как Вас зовут?")

while True:
    user_age = input("Сколько Вам лет?")          # проверка на возраст
    try:
        user_age = int(user_age)
        if 0 < user_age < 100:
            print(f"Возраст {user_age} принят")
            break
        else:
            print("Ошибка: возраст должен быть больше 0 и меньше 100")
    except ValueError:
        print("Ошибка: необходимо ввести число. Попробуйте еще раз!")
print()

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
bmi = weight_float / (height_float ** 2)                        # расчёт ИМТ
bmi_round = round(bmi, 1)                                     # округление ИМТ
water_ml = weight_float * WATER_PER_KG                     # норма воды мл
water_l = water_ml / CONSTANT_ML                           # литры
water_round = round(water_l, 1)  # округление воды

print(f"Отчет для пользователя:{user_name}, {user_age} г.")
print(f"Ваш индекс массы тела (ИМТ):{bmi_round}")
print(f"Рекомендуемая норма воды:{water_round} л в день")
print()
print("Расчет окончен,", "Будьте здоровы!", sep="\n")
