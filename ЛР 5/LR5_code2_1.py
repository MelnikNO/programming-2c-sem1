import time

class Timer:

    """Класс, который вычисляет время выполнения блока."""

    def __enter__(self):

        """Вычисляет время начало - запускает таймер."""

        self.start = time.perf_counter()

        return self


    def __exit__(self, exc_type, exc_val, exc_tb):

        """Останавливает таймер и выводит время выполнения.
        Аргументы:
        exc_type: Тип исключения, если оно произошло.
        exc_val: Значение исключения, если оно произошло.
        exc_tb: Трассировка стека, если произошло исключение.
        """

        self.end = time.perf_counter()
        self.con = self.end - self.start
        print(f"Время выполнения: {self.con} секунд")


def fibonacci(n):

    """Генератор чисел Фибоначчи, количество значений в ряду указывается пользователем."""

    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


def main():
    n = int(input('Введите большое число для ряда Фибоначчи: '))
    with Timer() as timer:
        fib_num = list(fibonacci(n))


if __name__ == "__main__":
    main()