import unittest
from Calculator import Calculator
from Csvreader import Csvreader
from pprint import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:  # Method for setting up test fixture before exercising it. The method is called before calling the implemented test methods.
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(calculator, Calculator)

    def test_addition(self):
        test_data = Csvreader("/src/Unit Test Addition.csv").data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))


if __name__ == '__main__':
    unittest.main()
