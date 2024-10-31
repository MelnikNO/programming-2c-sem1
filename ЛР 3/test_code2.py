import unittest
import LR3_code2


class Testprogrammlr22(unittest.TestCase):
    '''Тесты для модифицированного калькулятора из 2 задания ЛР 2, в которой тестируются функции вычисления заданной точности и выполнение различных арифметических действий.'''

    def test_convert1(self):
        self.assertEqual(LR3_code2.convert_precision(1e-6), 6)

    def test_convert2(self):
        self.assertEqual(LR3_code2.convert_precision(0.001), 3)

    def test_convert3(self):
        self.assertEqual(LR3_code2.convert_precision(1e-23), 23)

    def test_add(self):
        self.assertEqual(LR3_code2.calculate(23, 45, 67, 3, 5, 1, 2, operator = '+', tolerance = 1e-6), 146)


    def test_sub(self):
        self.assertEqual(LR3_code2.calculate(23, 45, 67, 3, 5, 1, 2, operator = '-', tolerance = 1e-6), -100.0)


    def test_mult(self):
        self.assertEqual(LR3_code2.calculate(23, 45, 67, 3, 5, 1, 2, operator = '*', tolerance= 1e-6), 2080350.0)


    def test_div(self):
        self.assertEqual(LR3_code2.calculate(23, 45, 67, 3, 5, 1, 2, operator = '/', tolerance = 1e-6), 1.1e-05)


    def test_div_0(self):
        self.assertEqual(LR3_code2.calculate(23, 0, 67, 3, 5, 1, 2, operator = '/', tolerance = 1e-6), 'На ноль делить нельзя!')


    def test_medium(self):
        self.assertEqual(LR3_code2.calculate(23, 45, 67, 3, 5, 1, 2, operator = 'medium', tolerance = 1e-6), 20.857143)


    def test_variance(self):
        self.assertEqual(LR3_code2.calculate(23, 45, 67, 3, 5, 1, 2, operator = 'variance', tolerance = 1e-6), 672.809524)


    def test_stddeviation(self):
        self.assertEqual(LR3_code2.calculate(23, 45, 67, 3, 5, 1, 2, operator='std_deviation', tolerance=1e-6), 1648.040027)


    def test_median(self):
        self.assertEqual(LR3_code2.calculate(23, 45, 67, 3, 5, 1, 2, operator='median', tolerance=1e-6), 5.0)


    def test_mehcv(self):
        self.assertEqual(LR3_code2.calculate(23, 45, 67, 3, 5, 1, 2, operator='9', tolerance=1e-6), 43.0)


    def test_not_oper(self):
        self.assertEqual(LR3_code2.calculate(23, 45, 67, 3, 5, 1, 2, operator = '%', tolerance = 1e-6), 'Недопустимый оператор')


if __name__ == '__main__':
    unittest.main()