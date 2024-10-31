import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


def convert_precision(tolerance):
    '''Функция, аргументом которой является заданная точность в виде нотации (1е-6 например) или в виде числа 0,1 и 0,001.
    Далее число преобразуется в строковый вид и в зависимости от ее вида считается значение точности.
    '''

    h = str(tolerance)

    if 'e' in h or 'E' in h:
        part, order = h.split('e') if 'e' in h else h.split('E')

        return abs(int(order))

    elif '.' in h:
        part1, part2 = h.split('.')

        return len(part2)

    else:
        return 0


def log_decorator(func):
    '''Декорирование функции и его переменных.
    В декорирующем замыкании происходит логирование до и после вызова функции.
    '''
    def log(oper1, oper2, operator,  tolerance):
        logger.debug(f'Введенные операнды, операция и точность: {oper1}, {oper2}, {operator}, {tolerance}')
        res = func(oper1, oper2, operator, tolerance)
        logging.info(f'Результат: {res}')
        return res
    return log


@log_decorator
def calculate(a, b, operator, tolerance = 1e-6):
  ''' Выполняет определенную арифметическую операцию над двумя числами с заданной точностью.
  Вызывается другая функция, которая извлекает значение.
  Если заданный операнд равен предложенным, то выполняется соответствующая операция и возвращается результат вычисления, который округляется до заданной точности.
  Аргументы:
  a - первое числло.
  b - второе число.
  operator - оператор, который задается и используется для выполнения операции.
  tolerance - заданная точность, которая извлекает значение точности.
  return - возвращает результат выполнения арифметической операции, которая округляется до заданной точности.
  '''

  correction = convert_precision(tolerance)

  if operator == '+':
    return round(a + b, correction)
  elif operator == '-':
    return round(a - b, correction)
  elif operator == '*':
    return round(a * b, correction)
  elif operator == '/':
    if b == 0:
      return 'На ноль делить нельзя!'
    return round(a / b, correction)
  else:
    return 'Недопустимый оператор'


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

  print(calculate(number1, number2, operator, tolerance=1e-6))

if __name__ == "__main__":
  main()