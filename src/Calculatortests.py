import unitest
from Calculator import calculator

class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        calculator = calculator()
        self.assertIsInstance(calculator, calculator)

if _name_== '_main_':
    unittest.main()