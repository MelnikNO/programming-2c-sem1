import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

def log_decorator(func):
    '''Декорирование функции и его переменных.
    В декорирующем замыкании происходит логирование до и после вызова функции.
    '''
    def log(oper1, oper2, operator):
        logger.debug(f'Введенные операнды и операция: {oper1}, {oper2}, {operator}')
        res = func(oper1, oper2, operator)
        logging.info(f'Результат: {res}')
        return res
    return log

@log_decorator
def calculate(a, b, operator):
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


def test_calc():
    '''Проводит тесты на определенных примерах'''
    assert calculate(1, 2, '+') == 3
    assert calculate(4, 65, '-') == -61
    assert calculate(5, 5, '*') == 25
    assert calculate(10, 2, '/') == 5
    print('Все тесты пройдены')


def main():
  '''Основная функция.
  Аргументы:
  number1 - первое числло.
  number2 - второе число.
  operator - оператор, который задается и используется для выполнения операции.
  '''
  number1 = float(input('Введите первое число: '))
  number2 = float(input('Введите второе число: '))
  operator = str(input('Введите оператор (+, -, *, /): '))

  print(calculate(number1, number2, operator))

main()
test_calc()