def fibonaccii(x):

    """Генератор, который создает числа Фибоначчи"""

    a, b = 0, 1
    for i in range(x):
        yield a
        a, b = b, a + b


def fib_plus(fib):

    """Генератор, который прибавляет 10 к каждому числу из ряду Фибоначчи"""

    for i in fib:
        yield i + 10

def main():
    cou = int(input('Введите количество чисел в ряду: '))

    f = fibonaccii(cou)
    fi = fib_plus(f)

    for n in fi:
        print(n, end=' ')

if __name__ == "__main__":
    main()