import unittest
from main_eda import func

class TestFunc(unittest.TestCase):
    
    def test_func_runs(self):
        """Test that func() runs without errors and returns something"""
        result = func()
        self.assertTrue(result, "func() should return something")

if __name__ == '__main__':
    unittest.main()
