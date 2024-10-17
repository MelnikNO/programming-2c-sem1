from LR2_code2 import calculate

def test_add():
  '''Проверяет функцию calculate() на сложения чисел через тестирование.'''
  assert calculate(1, 2, '+') == 3
  return 'test_add passed'


def test_sub():
  '''Проверяет функцию calculate() на вычитание чисел через тестирование.'''
  assert calculate(4, 65, '-') == -61
  return 'test_sub passed'


def test_mult():
  '''Проверяет функцию calculate() на умножение чисел через тестирование.'''
  assert calculate(5, 5, '*') == 25
  return 'test_mult passed'


def test_div():
  '''Проверяет функцию calculate() на деление чисел через тестирование.'''
  assert calculate(10, 2, '/') == 5
  return 'test_div passed'

if __name__ == "__main__":
  print(test_add())
  print(test_sub())
  print(test_mult())
  print(test_div())