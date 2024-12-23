# test_main3.py

import unittest
from main3 import add, subtract, multiply, divide, check

class TestMain3(unittest.TestCase):
    # Тесты для функции add
    def test_add(self):
        self.assertEqual(add(2, 3), 5)  # 2 + 3 = 5
        self.assertEqual(add(-1, 1), 0)  # -1 + 1 = 0
        self.assertEqual(add(0, 0), 0)  # 0 + 0 = 0
        self.assertNotEqual(add(3, 7), 9) # 3 + 7 = 9

    # Тесты для функции subtract
    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)  # 10 - 5 = 5
        self.assertEqual(subtract(-5, -5), 0)  # -5 - (-5) = 0
        self.assertEqual(subtract(0, 5), -5)  # 0 - 5 = -5
        self.assertNotEqual(subtract(4, 2), 1) # 4 - 2 = -1

    # Тесты для функции multiply
    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)  # 3 * 4 = 12
        self.assertEqual(multiply(0, 100), 0)  # 0 * 100 = 0
        self.assertEqual(multiply(-2, 3), -6)  # -2 * 3 = -6
        self.assertNotEqual(multiply(2, 5), 12) # 2 * 5 = 12

    # Тесты для функции divide
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)  # 10 / 2 = 5
        self.assertEqual(divide(-9, 3), -3)  # -9 / 3 = -3
        self.assertNotEqual(divide(4, 2), 3)  # 4 / 2 = 3
        with self.assertRaises(ZeroDivisionError):  # Проверяем, что деление на 0 вызывает исключение
            divide(10, 0)

    # Тесты для функции check
    def test_check(self):
        self.assertEqual(check(2), True)  # 2 четное
        self.assertEqual(check(3), False)  # 3 нечетное
        self.assertEqual(check(0), True)  # 0 четное

if __name__ == '__main__':
    unittest.main()
