def bank (x,y):
    x = float(x)
    y = int(y)
    for i in range (y):
        x += x * 0.1
    return x

money = float(input("Введите сумму: "))
year = int(input("Введите количество лет: "))

result = bank (money, year)
print (f"Ваша итоговая сумма через {year} лет = {result} руб.")
