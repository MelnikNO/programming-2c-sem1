import unittest
import LR3_code1


class Testprogrammlr22(unittest.TestCase):
    '''Тесты для модифицированного калькулятора из 2 задания ЛР 2, в которой тестируются функции вычисления заданной точности и выполнение различных арифметических действий.'''

    def test_convert1(self):
        self.assertEqual(LR3_code1.convert_precision(1e-6), 6)

    def test_convert2(self):
        self.assertEqual(LR3_code1.convert_precision(0.001), 3)

    def test_convert3(self):
        self.assertEqual(LR3_code1.convert_precision(1e-23), 23)

    def test_add(self):
        self.assertEqual(LR3_code1.calculate(3.5, 2.1, '+', 1e-6), 5.6)


    def test_sub(self):
        self.assertEqual(LR3_code1.calculate(40, 6.5, '-', 1e-6), 33.5)


    def test_mult(self):
        self.assertEqual(LR3_code1.calculate(88.56935628, 2.2586728, '*', 1e-8), 200.04919594)


    def test_div(self):
        self.assertEqual(LR3_code1.calculate(48.85694, 2, '/', 1e-6), 24.42847)


    def test_div_0(self):
        self.assertEqual(LR3_code1.calculate(10, 0, '/', 1e-6), 'На ноль делить нельзя!')


    def test_not_oper(self):
        self.assertEqual(LR3_code1.calculate(34.24, 3, '%', 1e-6), 'Недопустимый оператор')


if __name__ == '__main__':
    unittest.main()