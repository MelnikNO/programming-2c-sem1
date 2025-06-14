# README.md

## Задание 1 
Тестирование должно учитывать развертывание и свертывание контекста: подготовка временных файлов перед тестами и их корректное удаление после завершения. Тестирование можно проводить или с помощью unittest или с помощью pytest. Использовать tempfile (или другую для unittest) или tmpdir  (для pytest) в тестах. 


Проверьте (как минимум):

Корректное считывание настроек из файла.
Обработку ошибки FileNotFoundError.
Обработку ошибки ValueError при некорректном JSON.
Для функции записи в файл проверьте:
Корректную запись строки в файл.
Создание файла, если он отсутствует.
Добавление строк в существующий файл.
Модульные тесты должны быть вынесены в отдельный файл (например, test_calculator_io.py).
Код должен быть оформлен в соответствии со стандартом PEP8.
Используйте комментарии и docstrings для описания функций.


**Комментарий к основной программе:** Программа вызвала достаточно сложностей и процесс разбора для понимания был очень долгим, что сложно описать его читабельным текстом. Главный момент, что программа предназначена для загрузки параметров из файла и ведения вычислений. Сначала программа загружает параметры из JSON-файла и обновляет глобальный словарь. Потом записывает результаты в файл.


**Комментарий к тестовой программе:** Pytest проверяет функциональность двух основных функций программы: загрузки параметров из JSON-файла и записи логов. Основная суть программы заключается в возможности настройки параметров через внешний файл и ведении истории операций.

**Результат программы:**

![code1](https://github.com/MelnikNO/programming-2/blob/main/Screen/LR7_1_test.png)

---

## Задание 2 
Используя параметризацию тестов с использованием библиотеки pytest, написать тесты функции two_sum, которую вы реализовали ранее. 

Требования

Покрытие тестами:

Тесты должны быть реализованы с использованием pytest.
Использовать параметризацию (@pytest.mark.parametrize) для проверки функции на разных входных данных.
Обеспечить покрытие тестами следующих случаев:
Базовый случай: массив из нескольких элементов, включая положительные и отрицательные числа.
Пограничные случаи:
Минимальный размер массива (len(nums) == 2).
Числа в массиве с минимальными и максимальными значениями в пределах [-10^9, 10^9].
Особые случаи:
Числа в массиве повторяются.
Все числа в массиве одинаковые.
Тесты должны проверять как входные данные, так и корректность индексов (порядок не важен).
Тестируемая функция:

Функция должна находиться в отдельном модуле (например, solution.py).
Тесты должны быть реализованы в отдельном файле (например, test_solution.py).


**Комментарий к основной программе:** Функция two_sum решает задачу поиска двух чисел в списке, сумма которых равна заданному значению.

**Комментарий к тестовой программе:** Pytest охватывает множество случаев использования функции из основной программы. Они позволяют убедиться в корректности работы функции в различных ситуациях. Важно также учитывать возможные значения элементов списка в пределах заданного диапазона. 

**Результат программы:**

![code1](https://github.com/MelnikNO/programming-2/blob/main/Screen/LR7_2_test.png)

---

## Задание 3 - Тестирование с помощью pytest
Автоматическая генерация входных данных с Hypothesis:

Использовать стратегию @given для генерации входных данных n в диапазоне 0 ≤ n ≤ 100.
Проверить, что функция корректно обрабатывает все допустимые входные значения.
Проверить свойства факториала:
(n + 1)! = (n + 1) × n!

Функция не возвращает отрицательных значений.
Обработка некорректных данных: функция должна выбрасывать исключение ValueError, если n не является натуральным числом (например, отрицательное число или дробь).

**Комментарий к тестовой программе:** Pytest проверяют функцию из основной программы, включая позитивные и негативные случаи. Hypothesis позволяет автоматически генерировать тестовые данные, что делает тесты более разнообразными и надежными. Основные сложности, которые могут возникнуть при тестировании функции factorial, связаны с обработкой некорректных типов данных и значений. 

**Результат программы:**

![code1](https://github.com/MelnikNO/programming-2/blob/main/Screen/LR7_3_test.png)

---

