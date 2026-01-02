import unittest
import pandas as pd
from main_eda import func  # your function to test

class TestFunc(unittest.TestCase):
    
    def test_func_returns_dataframe(self):
        """Test that func() returns a pandas DataFrame"""
        result = func()
        self.assertIsInstance(result, pd.DataFrame, "func() should return a DataFrame")
    
    def test_func_returns_head_five(self):
        """Test that func() returns exactly 5 rows"""
        result = func()
        self.assertEqual(len(result), 5, "func() should return 5 rows (head of the dataframe)")
        
    def test_columns_exist(self):
        """Optional: test that expected columns exist in the returned DataFrame"""
        result = func()
        expected_columns = ['Quarter', 'Management Consulting Services Total (£m)']
        for col in expected_columns:
            self.assertIn(col, result.columns, f"Column '{col}' should exist in the DataFrame")
            
if __name__ == '__main__':
    unittest.main()
