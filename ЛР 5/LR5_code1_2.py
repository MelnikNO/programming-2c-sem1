import random

def RandomNumberIterator(x, start, end):

    """Функция-генератор случайных чисел, где используется ключевое слово"""

    for i in range(x):
        yield random.randint(start, end)


def main():
    cou = int(input('Введите количество случайных чисел: '))
    s = int(input('Введите начало диапозона: '))
    e = int(input('Введите конец диапозона: '))

    rand = RandomNumberIterator(cou, s, e)

    for n in rand:
        print(n)


if __name__ == "__main__":
    main()