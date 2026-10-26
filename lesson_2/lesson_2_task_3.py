import math

def square(x):
    s = x * x
    if x % 1 != 0:
        s = math.ceil(s)
    s = int(s)
    print("Площадь квадрата:", s)

inp = float(input("Введите сторону квадрата: ")) 
square(inp)
