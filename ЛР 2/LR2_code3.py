from functools import partial

t1_2_elems = {"U_234": 7.74 * 10**12, "U_235": 2.22 * 10**16, "U_238": 1.41 * 10**17}
radioactive_funcs = {"U_234": None, "U_235": None, "U_238": None}

def decay_amount(N0, t, t1_2):
    '''Вычисляет количество радиоактивного вещества, оставшегося в некоторый момент t по закону распада.
    Аргументы:
    N0 - изначальное количества вещества;
    t - некоторый момент времени;
    t1_2 - период полураспада вещества.
    '''
    N = N0 * (1/2) ** (t/t1_2)
    res = "Масса радиоактивного вещества, t1_2=" + str(t1_2)
    print(f'{res} с периодом полураспада {t1_2}, N0 = {N0}, t = {t}')
    return N

f1 = partial(decay_amount, t1_2 = t1_2_elems['U_234'])
f2 = partial(decay_amount, t1_2 = t1_2_elems['U_235'])
f3 = partial(decay_amount, t1_2 = t1_2_elems['U_238'])

def main():
    '''Основной код программы, где вызываются каррированные функции.
    И организован цикл по словарю с распечаткой на экране сколько вещества осталось от одного и того же N0 в некоторый момент времени t.
    '''
    N0 = 100
    t = 4006.9
    radioactive_funcs["U_234"] = f1
    radioactive_funcs["U_235"] = f2
    radioactive_funcs["U_238"] = f3

    for isotope, func in radioactive_funcs.items():
        result = func(N0, t)
        print(f'Изотоп: {isotope}, Остаток: {result}')


main()