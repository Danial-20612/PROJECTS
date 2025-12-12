import unittest

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,5), 7)

def add(a,b):
    return a + b 
    
if __name__ == "__main__":
    unittest.main()