from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 15", "+79001234567"),
    Smartphone("Samsung", "Galaxy S24", "+79119876543"),
    Smartphone("Xiaomi", "Redmi Note 13", "+79251112233"),
    Smartphone("Huawei", "P60 Pro", "+79034445566"),
    Smartphone("Google", "Pixel 8", "+79167778899")
]
x = 0
for i in catalog:
    print(f"{catalog[x].mobile_mark} - {catalog[x].mobile_model}. {catalog[x].mobile_number}")
    x += 1
