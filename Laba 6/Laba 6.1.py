class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def strong_password(self, password):
        if len(password) < 8:
            raise ValueError("Пароль должен состоять минимум из 8 символов")
        return password

    def set_pasword(self, new_password):
        self.__password = new_password

    def check_password(self, replay_password):
        return self.__password == replay_password

    def get_password_mask(self):
        return "*" * len(self.__password)


username = input('Введите ник: ')
email = input('Введите почту: ')

while True:
    password = input('Введите пароль : ')
    if len(password) >= 8:
        break
    else:
        print('Неправильно! (Пароль должен состоять минимум из 8 символов!)')

user = UserAccount(username, email, password)

while True:
    password_to_check = input('Введите старый пароль ещё раз: ')
    if user.check_password(password_to_check):
        print('Пароль верный')
        break
    else:
        print("Пароль неверный")

new_password = input("Введите новый пароль: ")
user.set_pasword(new_password)

while True:
    newpassword_to_check = input('Введите пароль ещё раз: ')
    if len(newpassword_to_check) >= 8:
        break
    else:
        print('Пароль должен быть больше 8 символов')

if user.check_password(newpassword_to_check):
    print('Пароль верный')
else:
    print('Пароль неверный')

print(f'Ник: {user.username}')
print(f'Почта: {user.email}')
print(f'Скрытый Пароль: {user.get_password_mask()}')