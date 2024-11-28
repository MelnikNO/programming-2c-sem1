import re # регулярные выражения, модуль для поиска, замены и обработки строк на основе заданных шаблонов
import time

from LR1_3_1 import calculate

class BatchCalculatorContextManager:

    """Менеджер контекста для обработки вычислений из файла."""

    def __init__(self, filename):

        """Инициализация менеджера контекста.
        Аргументы:
        filename: имя файла, из которого будут считываться выражения.
        """

        self.filename = filename
        self.file = None


    def __enter__(self):

        """Открывает файл для чтения и возвращает экземпляр менеджера контекста."""

        self.file = open(self.filename, 'r')
        self.start = time.perf_counter()
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):

        """Закрытие файла при выходе из контекста.
        Аргументы:
        exc_type: Тип исключения, если оно возникло.
        exc_val: Значение исключения, если оно возникло.
        exc_tb: Объект трассировки, если оно возникло.
        """

        if self.file:
            self.file.close()

        self.end = time.perf_counter()
        self.con = self.end - self.start
        print(f"Время выполнения: {self.con} секунд")


    def exp(self):

        """Генерирует выражения, считанные из файла."""

        for line in self.file:
            yield line.strip()


def main():
    filename = 'example.txt'
    with BatchCalculatorContextManager(filename) as manager:
        for example in manager.exp():
            mat = re.match(r'(\d+)([+\-*/])(\d+)', example) # проверяет, соответствует ли строка шаблону в начале строки
            if mat:
                a = float(mat.group(1))
                operator = mat.group(2)
                b = float(mat.group(3))
                res = calculate(a, b, operator)
                print(f"{example} = {res}")

            else:
                print(f"Что-то пошло не так {example}")


if __name__ == "__main__":
    main()