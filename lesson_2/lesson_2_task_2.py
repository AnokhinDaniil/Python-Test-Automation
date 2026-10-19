def is_year_leap(year):
    if year % 4 == 0:
        return True
    else: 
        return False
    

inp = int(input("Введите год: "))
result = is_year_leap(inp)

print("год", inp, ":", result)