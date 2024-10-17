def func():
  '''Обычная функция для создания замыкания.
  Аргументы:
  name - некое имя;
  birthday - некая дата рождения;
  place - место рождения.
  Функция возвращает внутреннюю функцию.
  '''
  name = 'Natalya'
  birthday = '31.03.1789'
  place = 'Russia'

  def func_second():
    '''Внутренняя функция для создания замыкания.
    Возвращает словарь с именем, датой рождения и местом рождения.
    '''
    return {'name': name, 'birthday': birthday, 'place': place}

  return func_second


print(func()())
