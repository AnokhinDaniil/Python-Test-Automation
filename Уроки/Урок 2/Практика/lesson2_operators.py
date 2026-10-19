user_login = "adam"
user_pass = "qwerty123456"

login = input("login: ")
password = input("password: ")

if (login == user_login) and (password == user_pass):
    print("secret is open")
else:
    print("locked")