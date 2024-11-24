"""Задание 4 комплект 1"""

from functools import cache


def fibonachchi(n, flst = [0, 1]):

    """Функция вычисления чисел Фибоначчи через рекурсивный способ."""

    if n == 0:
        return []
    if n == 1:
        return flst[0]
    if n == 2:
        return flst
    else:
        last = flst[-2] + flst[-1]
        return sorted(fibonachchi(n - 1, flst + [last]))


@cache
def fib(n: int):

    """Функция вычисления чисел Фибоначчи с помощью декоратора из стандартного модуля."""

    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

fib_lst = [fib(i) for i in range(10)]
print(f"Через декоратор: {fib_lst}")
print(f"Через ручной счет: {fibonachchi(10)}")