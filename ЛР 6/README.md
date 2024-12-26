# README.md

## Задание 1 - Анализ мест в коде с исключительными ситуациями

Можно вместо образца борда по ссылке в начале задания отлавливать исключения (errors) в функционале вашего калькулятора из предыдущих лабораторных работ, особенно в той, где надо было читать все необходимые и выраженния для вычислений из файла.

Исключительная ситуация может возникнуть на этапе работы с файлом (чтение, запись). Программа может не считать файл с настройками например, из-за ограниченного набора прав пользователя, запустившего данную программу или каких-либо настроек других ОС. Эти ситуации мы можем обработать с помощью блока (см. рабочий пример в стартовом борде):

```
try
    pass # какое-то выражение, возможно, поднимающее исключение  
except Exception:
   print('Исключение возникло') # обработка исключения 
else:
   # блок, выполняющийся, если исключения не было
finally:
   # блок, который выполняется в всегда независимо от того, было ли исключение или нет
```

**Комментарий к основной программе:** Программа вызвала достаточно сложностей и процесс разбора для понимания был очень долгим, что сложно описать его читабельным текстом. Главное надо было усвоить основную концепцию программы: Загрузка параметров (файл params.ini); запись результата в файл (newoutput.txt), если не получается, то создается резервный; основная программа вызывает функцию калькулятора и записывает результат с помощью вызванной функции:
```
write_log(number1, number2, action=operator, result=res, file=PARAMS['dest'])
        except Exception as e:
            print(f"Ошибка записи в лог: {e}")
            print(f"Не удалось записать в лог: {operator}: ({number1}, {number2}) = {res}")
            try:
                write_log(
                    f"Ошибка логирования: {e}",
                    action="error",
                    file='calc-history.log.txt'
                )
            except Exception as log_e:
                print(f"Критическая ошибка! Не удалось записать ошибку в {file}. Ошибка: {log_e}")
```
**Результат программы:**

![code1](https://github.com/MelnikNO/programming-2/blob/main/Screen/LR6_1.png)

**Комментарий к тестовой программе:** Тестовая программа проверяет успешность записи в файл, затем обрабатывает ошибки при попытке записи с недоступными правами и записи в файл с правами только для чтения
     ```
     os.chmod(file_name, 0o444)
     with pytest.raises(Exception) as e:
         write_log(1, 2, action="test", result=3, file=file_name)
     assert f'Ошибка записи в файл {file_name}. Записать не удалось.' in str(e.value)
     ```

**Результат программы:**

![code1](https://github.com/MelnikNO/programming-2/blob/main/Screen/LR6_1_test.png)

---

## Задание 2 - Модульное тестирование с unittest

Можно вместо образца борда по ссылке в начале задания покрыть тестами функционал вашего калькулятора из предыдущих лабораторных работ.

Шаблон для тестирования с помощью unittest может выглядеть так:

```
import unittest

class TestSomeFunc(unittest.TestCase): # создаем свой класс для тестов

     def firsttestcase(self): # внутри функции один или несколько тестовых
         self.assertEqual(2*2, 4) # случаев, которые проверяют какие-то 
         # близкие предположения
         

     # ...
     def secondtestcase(self): # вторая группа тестов
         pass


unittest.main(verbosity=1)     # запуск тестов
```

Пример тестирования двух функций convert_precision и two_sum, которую мы создавали ранее. Нюанс тестирования в repl.it и PyCharm. В repl.it  тесты запускаются вручную с помощью вкладки Shell (справа) (пример борда), в PyCharm требуется закомментировать запуск тестов с помощью: 

```
unittest.main(verbosity=1)
```


**Комментарий:**  Аналогично 1 заданию, сложности были. Сама программа содержит unittest для фйункции записи и вычислений. Тестовая функция для проверки записи файла:
     ```
     with self.assertRaises(Exception) as context:
         write_log(*args, action='*', file=log_file)
     self.assertIn("Ошибка записи в файл", str(context.exception))
     ```
После проверки вычисления, проверяется успешность записи в файл:
     ```
     try:
         write_log(1, 2, action="test", result=3, file=file_name)
         with open(file_name, "r") as f:
             content = f.read()
         self.assertIn("test: (1, 2) = 3", content)
     finally:
         if os.path.exists(file_name):
             os.remove(file_name)
     ```

**Результат программы:**

![code2](https://github.com/MelnikNO/programming-2/blob/main/Screen/LR6_2.png)

---

## Задание 3 - Тестирование с помощью pytest

Можно вместо образца борда по ссылке в начале задания покрыть тестами функционал вашего калькулятора из предыдущих лабораторных работ.

По аналогии с предыдущим пунктом 2.

Перепешите те же самые тесты с помощью фреймворка pytest. Сравните его использование с фреймворком unittest.

Разберите работу с ним с помощью слендующих внешних источников:

    https://pytest-docs-ru.readthedocs.io/ru/latest/usage.html
    https://tproger.ru/articles/testiruem-na-python-unittest-i-pytest-instrukcija-dlja-nachinajushhih
    https://proglib.io/p/python-testing
    https://habr.com/ru/articles/448782/
    https://replit.com/talk/learn/Python-unit-tests-with-PyTest/40976
    https://docs.replit.com/teams-edu/unit-testing

**Комментарий:** Аналогично 1 заданию, сложности были. Сама программа содержит pytest для фйункции записи и вычислений. Тестовая функция для проверки записи файла:
     ```
     args = [67, 90]
     log_file = '/newoutput2.txt'
     with pytest.raises(Exception) as context:
         write_log(*args, action='*', file=log_file)
     assert "Ошибка записи в файл" in str(context.value)
     ```
После проверки вычисления, проверяется успешность записи в файл:
     ```
     file_name = "test_log.txt"
     try:
         write_log(1, 2, action="test", result=3, file=file_name)
         with open(file_name, "r") as f:
             content = f.read()
         assert "test: (1, 2) = 3" in content
     finally:
         if os.path.exists(file_name):
             os.remove(file_name)
     ```

**Результат программы:**

![code3](https://github.com/MelnikNO/programming-2/blob/main/Screen/LR6_3.png)

---
