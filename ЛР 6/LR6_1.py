from LR1_3_1 import calculate

PARAMS = {'precision': 0.00001, 'dest': 'newoutput.txt'}

def load_params(file="params.ini"):
    global PARAMS
    try:
        with open(file, mode='r', errors='ignore') as f:
            lines = f.readlines()
            for l in lines:
                param = l.strip().split('=')
                if len(param) == 2:
                    key, value = param
                    key = key.strip()
                    value = value.strip()
                    if key != 'dest':
                        try:
                            value = eval(value)
                        except Exception as e:
                            print(f"Ошибка при парсинге значения '{value}' для параметра {key}: {e}")
                            continue
                    PARAMS[key] = value
    except FileNotFoundError:
        print(f"Файл параметров '{file}' не найден, используются значения по умолчанию.")
    return PARAMS


def write_log(*args, action=None, result=None, file='calc-history.log.txt'):
    error = None
    try:
        with open(file, mode='a', errors='ignore') as f:
            f.write(f"{action}: {args} = {result} \n")
    except PermissionError:
        print(f'Ошибка записи в файл {file}')
        file_new = file + '.txt'
        print(f'Попытка записать лог в файл с новым именем: {file_new}')
        try:
            with open(file_new, mode='a', errors='ignore') as backup_file:
                backup_file.write(f"{action}: {args} = {result} \n")
        except PermissionError as e:
            error = e

    if error:
        raise Exception(
            f'Ошибка записи в файл {file_new}. Записать не удалось.')


def main():
    load_params()
    print(f'Загруженные параметры: {PARAMS}')

    try:
        number1 = float(input('Введите первое число: '))
        number2 = float(input('Введите второе число: '))
        operator = str(input('Введите оператор (+, -, /, *): '))
        res = calculate(number1, number2, operator)

        print(f"Результат: {res}")

        try:
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
    except ValueError as e:
        print(f"Ошибка ввода: {e}")
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()