import array
from datetime import datetime

# Функция для определения дня недели по заданной дате
def get_weekday(day, month, year):
    date = datetime(year, month, day)
    return date.strftime("%A")  # Возвращает день недели

# Функция для проверки, является ли год високосным
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Функция для вычисления возраста
def calculate_age(day, month, year):
    today = datetime.now()
    birth_date = datetime(year, month, day)
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age


# Функция для вывода даты  в виде звёздочек
def print_date_with_stars(day, month, year):
    str_of_star = ["", "", "", "", ""]
    date_str = f"{day:02} {month:02} {year}"
    for char in date_str:
        match char:
            case '0':
                str_of_star[0] += '***   '
                str_of_star[1] += '* *   '
                str_of_star[2] += '* *   '
                str_of_star[3] += '* *   '
                str_of_star[4] += '***   '
            case '1':
                str_of_star[0] += '  *   '
                str_of_star[1] += '  *   '
                str_of_star[2] += '  *   '
                str_of_star[3] += '  *   '
                str_of_star[4] += '  *   '
            case '2':
                str_of_star[0] += '***   '
                str_of_star[1] += '  *   '
                str_of_star[2] += '***   '
                str_of_star[3] += '*     '
                str_of_star[4] += '***   '
            case '3':
                str_of_star[0] += '***   '
                str_of_star[1] += '  *   '
                str_of_star[2] += '***   '
                str_of_star[3] += '  *   '
                str_of_star[4] += '***   '
            case '4':
                str_of_star[0] += '* *   '
                str_of_star[1] += '* *   '
                str_of_star[2] += '***   '
                str_of_star[3] += '  *   '
                str_of_star[4] += '  *   '
            case '5':
                str_of_star[0] += '***   '
                str_of_star[1] += '*     '
                str_of_star[2] += '***   '
                str_of_star[3] += '  *   '
                str_of_star[4] += '***   '
            case '6':
                str_of_star[0] += '***   '
                str_of_star[1] += '*     '
                str_of_star[2] += '***   '
                str_of_star[3] += '* *   '
                str_of_star[4] += '***   '
            case '7':
                str_of_star[0] += '***   '
                str_of_star[1] += '* *   '
                str_of_star[2] += '* *   '
                str_of_star[3] += '  *   '
                str_of_star[4] += '  *   '
            case '8':
                str_of_star[0] += '***   '
                str_of_star[1] += '* *   '
                str_of_star[2] += '***   '
                str_of_star[3] += '* *   '
                str_of_star[4] += '***   '
            case '9':
                str_of_star[0] += '***   '
                str_of_star[1] += '* *   '
                str_of_star[2] += '***   '
                str_of_star[3] += '  *   '
                str_of_star[4] += '***   '
    j = 0
    while j < 5:
        print(str_of_star[j])
        j += 1


# Запрос данных у пользователя
day = int(input("Введите день вашего рождения (1-31): "))
month = int(input("Введите месяц вашего рождения (1-12): "))
year = int(input("Введите год вашего рождения (например, 1990): "))

# Получение информации
weekday = get_weekday(day, month, year)
leap_year = is_leap_year(year)
age = calculate_age(day, month, year)
#коррекция окончания
correct_year = 'лет'
if age != 11 and age % 10 == 1: correct_year = 'год'
elif 2 <= age <= 4 or (age > 20 and 2 <= age % 10 <=4):
    correct_year = 'года'

# Вывод 
print(f"Дата вашего рождения: \n")
print_date_with_stars(day, month, year)
print(f"День недели: {weekday}")
print(f"Год {year} {'високосный' if leap_year else 'не високосный'}")
print(f"Вам сейчас {age} {correct_year}.")
print(4 % 10)
