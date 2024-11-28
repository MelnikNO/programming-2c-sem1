import random


class RandomNumberIterator():

    """Класс-итератор для генерации случайных чисел в заданном диапозоне."""

    def __init__(self, count, start, end):

        """Метод инициализации, который принимает такие аргументы.
        count = количество чисел в диапозоне
        start = начало диапазона
        end = конец диапазона
        """

        self.count = count
        self.start = start
        self.end = end
        self.c = 0


    def __iter__(self):

        """Метод, который возвращает объект итератора."""

        return self


    def __next__(self):

        """Метод для получения следующего числа."""

        if self.c < self.count:
            num = random.randint(self.start, self.end)
            self.c += 1
            return num
        else:
            raise StopIteration

def main():
    cou = int(input('Введите количество случайных чисел: '))
    s = int(input('Введите начало диапозона: '))
    e = int(input('Введите конец диапозона: '))

    rand = RandomNumberIterator(cou, s, e)

    for n in rand:
        print(n)


if __name__ == "__main__":
    main()