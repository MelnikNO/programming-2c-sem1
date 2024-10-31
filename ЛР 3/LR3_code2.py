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
    def log(*args, operator,  tolerance):
        logger.debug(f'Введенные операнды, операция и точность: {args}, {operator}, {tolerance}')
        res = func(*args, action = operator, tolerance = tolerance)
        logging.info(f'Результат: {res}')
        return res
    return log


@log_decorator
def calculate(*args, action = None, tolerance = 1e-6):
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

  if action == '+' or action == '1' or action == 'Сложение':
    return round(sum(args), correction)

  elif action == '-' or action == '2' or action == 'Вычитание':
    return round(args[0] - sum(args[1:]), correction)

  elif action == '*' or action == '3' or action == 'Умножение':
    res = 1
    for num in args:
        res *= num
    return round(res, correction)

  elif action == '/' or action == '4' or action == 'Деление':
      res = args[0]
      for num in args:
          if num == 0:
              return 'На ноль делить нельзя!'
          else:
              res /= num
      return round(res, correction)

  elif action == '5' or action == 'Среднее значение' or action == 'medium':
      return round(sum(args) / len(args), correction)

  elif action == '6' or action == 'Дисперсия' or action == 'variance':
      srzn = sum(args) / len(args)
      res = 0
      for num in args:
          res += (num - srzn)**2
      return round(res / (len(args) - 1), correction)

  elif action == '7' or action == 'Стандартное отклонение' or action == 'std_deviation':
      srzn = sum(args) / len(args)
      res = 0
      for num in args:
          res += (num - srzn) ** 2
      return round((res / (len(args) - 1) ** 0.5), correction)

  elif action == '8' or action == 'Медиана' or action == 'median':
      array_list = sorted(args)
      print(array_list)
      if len(array_list) % 2 == 0:
          a = array_list[len(array_list) // 2]
          b = array_list[len(array_list) // 2 - 1]
          return round((a + b) / 2, correction)
      else:
          return round(array_list[len(array_list) // 2], correction)

  elif action == '9' or action == 'Межквартильный размах':
      array_list = sorted(args)
      print(array_list)
      if len(array_list) % 2 == 0:
          q2 = (array_list[len(array_list) // 2] + array_list[len(array_list) // 2 - 1]) / 2

      else:
          q2 = array_list[len(array_list) // 2]

      array_q1 = [i for i in array_list if i < q2]
      if len(array_q1) % 2 == 0:
          q1 = (array_q1[len(array_q1) // 2] + array_q1[len(array_q1) // 2 - 1]) / 2
      else:
          q1 = array_q1[len(array_q1) // 2]

      array_q3 = [i for i in array_list if i > q2]
      if len(array_q3) % 2 == 0:
          q3 = (array_q3[len(array_q3) // 2] + array_q3[len(array_q3) // 2 - 1]) / 2
      else:
          q3 = array_q3[len(array_q3) // 2]

          return round(q3 - q1, correction)

      return round(q3 - q1, correction)

  else:
    return 'Недопустимый оператор'


def main():
  ''' Основная функция.
  Аргументы:
  number1 - первое числло.
  number2 - второе число.
  operator - оператор, который задается и используется для выполнения операции.
  '''

  number = input('Введите числа через пробел: ')
  numbers = list(map(float, number.split()))
  operators = ['1 - Сложение - "+"', '2 - Вычитание - "-"', '3 - Умножение - "*"', '4 - Деление - "/"', '5 - Среднее значение - medium', '6 - Дисперсия - variance', '7 - Стандартное отклонение - std_deviation', '8 - Медиана - median', '9 - Межквартильный размах']

  for met in operators:
      print(met)

  operator = str(input('Введите оператор: '))

  print(calculate(*numbers, operator = operator, tolerance=1e-6))

if __name__ == "__main__":
  main()