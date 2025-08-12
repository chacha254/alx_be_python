import unittest 
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self): # setup the SimpleCalculator instance before each tes
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-3, 3), -6)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(5, 3), 15)
        self.assertEqual(self.calc.multiply(-3, 3), -9)
   
    def test_division(self):
        if self.calc == 0:
            print("Cannot divide by Zero!")
        else:
            self.assertEqual(self.calc.divide(9, 3), 3)
            self.assertEqual(self.calc.divide(-9, 3), -3)



        

