#Задание 1.1
import math

try:
    numb=int(input('Введите число:'))
    res=math.sqrt(numb)
    print(f'Квадратный корень из {numb} = {res}')
except ValueError as e:
    print(f'Ошибка: {e}')
#Задание 1.2
from datetime import date, datetime

clock= datetime.now()
today=date.today()

print(f'время:{clock.time()}, дата: {today}')