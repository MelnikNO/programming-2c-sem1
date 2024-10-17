def calculate(a: float, b: float, operator: str):
  ''' Выполняет определенную арифметическую операцию над двумя числами.
  Если заданный операнд равен предложенным, то выполняется соответствующая операция и возвращается результат вычисления.
  Аргументы:
  a - первое числло.
  b - второе число.
  operator - оператор, который задается и используется для выполнения операции.
  return - возвращает результат выполнения арифметической операции.
  '''
  if operator == '+':
    return a + b
  elif operator == '-':
    return a - b
  elif operator == '*':
    return a * b
  elif operator == '/':
    if b == 0:
      return 'На ноль делить нельзя!'
    return a / b
  else:
    return 'Недопустимый оператор'


def test_add():
  '''Проверяет функцию calculate() на сложения чисел через тестирование.'''
  assert calculate(1, 2, '+') == 3
  return 'test passed'


def test_sub():
  '''Проверяет функцию calculate() на вычитание чисел через тестирование.'''
  assert calculate(4, 65, '-') == -61
  return 'test passed'


def test_mult():
  '''Проверяет функцию calculate() на умножение чисел через тестирование.'''
  assert calculate(5, 5, '*') == 25
  return 'test passed'


def test_div():
  '''Проверяет функцию calculate() на деление чисел через тестирование.'''
  assert calculate(10, 2, '/') == 5
  return 'test passed'


def main():
  '''Основная функция.
  Аргументы:
  number1 - первое числло.
  number2 - второе число.
  operator - оператор, который задается и используется для выполнения операции.
  '''
  # number1 = float(input('Введите первое число: '))
  # number2 = float(input('Введите второе число: '))
  # operator = str(input('Введите оператор: '))

  # print(calculate(number1, number2, operator))
  print(test_add())
  print(test_sub())
  print(test_div())
  print(test_mult())

main()