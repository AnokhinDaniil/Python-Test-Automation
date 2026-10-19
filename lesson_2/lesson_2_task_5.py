# Напишите функцию month_to_season(), которая принимает 1 аргумент — номер месяца — и возвращает название сезона, 
# к которому относится этот месяц.

def month_to_season(number):
    if number == 12 or number == 1 or number == 2:
        print("Зима")
    elif number == 3 or number == 4 or number == 5:
        print("Весна")
    elif number == 6 or number == 7 or number == 8:
        print("Лето")
    elif number == 9 or number == 10 or number == 11:
        print("Осень")
    else:
        print("Введено значение не из диапазона")

inp = int(input("Введите значение от 1 до 12: "))
month_to_season(inp)