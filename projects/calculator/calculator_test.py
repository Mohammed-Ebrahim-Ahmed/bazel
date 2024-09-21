from projects.calculator.calculator import calculator
import unittest



class Test_calculator(unittest.TestCase):
    def testadd(self):
        cal = calculator()
        self.assertEqual(cal.add(2,3), 5)


if __name__ == "__main__":
    unittest.main()