from sqlite import *


def calculate_calory(age, weight, height, sex):
    if sex == "Мужской":
        calory = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        calory = (10 * weight) + (6.25 * height) - (5 * age) - 161

    return calory


def set_key(key: str = None):

    def decorator(func):
         setattr(func, "key", key)

         return func

    return decorator
