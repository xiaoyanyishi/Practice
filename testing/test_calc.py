import unittest

from python.calc import Calc


class TestCalc(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calc()

    def test_add(self):
        self.assertEqual(3, self.calc.add(1, 2))

        def test_add2(self):
            self.assertEqual(0.03, self.calc.add(0.01, 0.02))
