import unittest
import pandas as pd
import numpy as np
import os

class TestBriefEDA(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data_path = os.path.join(os.path.dirname(__file__), "../datasets/management_consulting_final.csv")
        df = pd.read_csv(cls.data_path)
        #take a small sample to make tests fast and self-contained
        cls.sample_df = df.sample(n=10, random_state=42).reset_index(drop=True)

    #test 1 - check columns exist
    def test_columns_exist(self):
        expected_columns = [
            "Quarter",
            "Management Consulting Services Total (£m)",
            "Gross Added Value",
            "Hours Worked",
            "Hourly Output"
        ]
        for col in expected_columns:
            self.assertIn(col, self.sample_df.columns)

    #test 2 - check numeric columns are numeric
    def test_numeric_columns(self):
        numeric_cols = [
            "Management Consulting Services Total (£m)",
            "Gross Added Value",
            "Hours Worked",
            "Hourly Output"
        ]
        for col in numeric_cols:
            self.assertTrue(pd.api.types.is_numeric_dtype(self.sample_df[col]), f"{col} is not numeric")

    #test 3 - check no NaNs in sampled data
    def test_no_nans(self):
        self.assertFalse(self.sample_df.isna().any().any(), "Sample contains NaN values")

    #test 4 - basic summary stats produce expected keys
    def test_summary_stats(self):
        stats = self.sample_df.agg({
            "Management Consulting Services Total (£m)": ["min", "max", "median", "mean", "std"],
            "Gross Added Value": ["min", "max", "median", "mean", "std"],
            "Hours Worked": ["min", "max", "median", "mean", "std"],
            "Hourly Output": ["min", "max", "median", "mean", "std"]
        })
        expected_stats = ["min", "max", "median", "mean", "std"]
        for col in stats.columns:
            for stat in expected_stats:
                self.assertIn(stat, stats.index, f"{stat} missing for {col}")

    #test 5 - quarter column format check
    def test_quarter_format(self):
        for q in self.sample_df["Quarter"]:
            self.assertRegex(q, r"^\d{4} Q[1-4]$", f"Quarter format invalid: {q}")


if __name__ == "__main__":
    unittest.main()
