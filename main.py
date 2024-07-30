def check_age(age: int):

    if age >= 18:# Введите условие для проверки возраста
        result = 'Доступ разрешён'
    else:
        result = 'Доступ запрещён'

    return result
#check_age(10)
#check_age(20)

def quadratic_equation(a, b, c):

    d = b ** 2 - 4 * a * c

    if d < 0:
        return 'корней нет'
    elif d == 0:
        x = -b / (2 * a)
        return x
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return x1, x2
# print(quadratic_equation(1, 8, 15))
# print(quadratic_equation(1, -13, 12))
# print(quadratic_equation(-4, 28, -49))
# print(quadratic_equation(1, 1, 1))

def check_email(email: str) -> bool:

    if ' ' in email:
        return False
    elif '@' and '.' in email:
        return True
    else:
        return False

# check_email('Helloworld@.ru') is True
# check_email('мояпочта@нетология.ру') is True
# check_email('python@email@net') is False
# check_email(' em@il.ru') is False