import math

def arithmetic(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
    else:
        return "Unknown operation"

def is_year_leap(year):
    if year % 4 == 0:
        return "Високосный"
    else:
        return "Невисокосный"

def square(a):
    result = (a ** 2, a * 4, a * math.sqrt(2))
    return result

def season(num):
    num = int(num)
    if num in range(1, 3) or num == 12:
        return "Зима"
    elif num in range(3, 6):
        return "Весна"
    elif num in range(6, 9):
        return "Лето"
    elif num in range(9, 12):
        return "Осень"
    else:
        return "Нет такого месяца, как и времени года"


def deposit(sum, years):
    percent = 0.1
    for i in range(0, years):
        sum += sum * percent
    return sum

def is_prime(num):
    if num < 2:
        return "Сложное"
    elif num == 2:
        return "Простое"
    else:
        for i in range(2, num):
            if num % i == 1:
                return "Простое число"
            else:
                return "Сложное число"

def XOR_cipher(phrase, key):
    return phrase ^ key

print(XOR_cipher('hooi', 'pizda'))
