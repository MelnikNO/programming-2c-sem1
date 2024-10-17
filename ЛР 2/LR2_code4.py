import unittest
import LR2_code3
import LR1_3_1


class Testprogramm3(unittest.TestCase):
    '''Тесты для задания 3, в которой тестируются функции радиоактивного распада, взятые из модуля LR2_code3.py.'''

    def test_uranium_234(self):
        self.assertEqual(LR2_code3.radioactive_funcs["U_234"](100, 3850.9), 99.99999996551368)

    def test_uranium_235(self):
        self.assertEqual(LR2_code3.radioactive_funcs["U_235"](100, 3980.9), 99.99999999998757)

    def test_uranium_238(self):
        self.assertEqual(LR2_code3.radioactive_funcs["U_238"](100, 4006.9), 99.99999999999804)


class Testprogrammlr11(unittest.TestCase):
    '''Тесты для задания 1 ЛР 1, в которой тестируются функции для тестирования арефмитических действий, взятые из модуля LR1_3_1.py.'''

    def test_add(self):
        self.assertEqual(LR1_3_1.calculate(1, 2, '+'), 3)

    def test_sub(self):
        self.assertEqual(LR1_3_1.calculate(4, 65, '-'), -61)

    def test_mult(self):
        self.assertEqual(LR1_3_1.calculate(5, 5, '*'), 25)

    def test_div(self):
        self.assertEqual(LR1_3_1.calculate(10, 2, '/'), 5)

    def test_div_0(self):
        self.assertEqual(LR1_3_1.calculate(10, 0, '/'), 'На ноль делить нельзя!')

if __name__ == '__main__':
    unittest.main()