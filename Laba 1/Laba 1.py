#Задание 1
name = str(input('Введите Имя:'))
def greet(name):
    print('привет', name)
greet(name)

#Задание 1(2)
number = int(input('Введите число: '))
def square(number):
    n = number**2
    print('Число в квадрате: ', n)
square(number)

#zadanie 1(3)
x = int(input('Первое число:'))
y = int(input('Второе число:'))

def max_of_two(x, y):
    if x > y:
        return print(x)
    elif x < y:
        return print(y)
    else:
        return print(x)
max_of_two(x, y)

#zadanie 2.1
name = str(input('Введите ваше имя: '))
age = int(input('Введите ваш возраст (Если не хотите указывать возраст, напишите 0): '))

def describe_person(name, age):
    if age == 0:
        return print('Вас зовут', name, 'вам', age+30)
    elif age > 0:
        return print('Вас зовут', name, 'вам', age)
    else:
        return print('Вы неправильно ввели свой возраст')

describe_person(name, age)