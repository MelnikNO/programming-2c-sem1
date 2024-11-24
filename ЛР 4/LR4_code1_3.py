"""Задание 3 комплект 1"""


def two_sum(lst, target):

    """Функция нахождения двух наименьших индексов элементов списка.
    Два цикла - два индекса, которые не повторяются.
    После нахождения суммы первая наименьшая пара возвращается кортежем.
    """

    res = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == target:
                res = [i, j]
                return res
    return res


def two_sum_hashed(lst, target):

    """Функция нахождения двух наименьших индексов элементов списка со сложностью О(n).
    Один цикл со встроенной функцией, которая позволяет перебрать элементы и их индексы.
    После нахождения суммы первая наименьшая пара возвращается кортежем.
    """

    res = {}
    mi = None

    for i, num in enumerate(lst):
        c = target - num
        if c in res:
            if mi is None or (res[c], i) < mi:
                mi = (res[c], i)

        res[num] = i

    return mi


def two_sum_hashed_all(lst, target):

    """Функция нахождения всех пар индексов, элементы которых дают сумму определенного числа из данных.
    Найденные пары добавляются в список, который сортируется по возрастанию и возвращается.
    """

    res = {}
    result = []

    for i, num in enumerate(lst):
        c = target - num
        if c in res:
            result.append((res[c], i))
        res[num] = i

    r = sorted(result)
    return r

def main():

    """Основная функция.
    Вводится список с определенными элементами, которые могут быть расположены в произвольном порядке.
    Вводится число из этого списка, по которому будет происходить поиск элементов.
    """

    number = input('Введите числа через пробел: ')
    lst = list(map(float, number.split()))
    target = float(input('Введите какое-нибудь число из этого интервала: '))
    print(two_sum_hashed_all(lst, target))

main()