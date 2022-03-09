from app import factorial
import unittest
from app import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_1(self):
        self.assertEqual(fibonacci(1), 1)
        
    def test_fibonacci_2(self):
        self.assertEqual(fibonacci(10), 89)
        
    def test_fibonacci_3(self):
        self.assertEqual(fibonacci(30), 1346269)
class TestFActorial(unittest.TestCase):
    def test_factorial_1(self):
        self.assertEqual(factorial(1), 1)       
        
# if __name__ == '__main__':
#     unittest.main()