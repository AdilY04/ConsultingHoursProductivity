import unittest
import pandas as pd
import numpy as np
from scipy.stats import linregress, spearmanr, kendalltau, chi2_contingency

#mock sample data (small subset to run tests without loading full CSV)
sample_data = {
    "Quarter": ["2023 Q1", "2023 Q2", "2023 Q3", "2023 Q4"],
    "Gross Added Value": [100, 110, 105, 115],
    "Hours Worked": [40, 42, 41, 43],
    "Hourly Output": [2.5, 2.62, 2.56, 2.67],
    "Management Consulting Services Total (£m)": [50, 55, 53, 57]
}

raw_hours_sample = {
    "Quarter": ["2023 Q1", "2023 Q2", "2023 Q3", "2023 Q4"],
    "Raw Hours Worked": [1000, 1050, 1020, 1080]
}

raw_output_sample = {
    "Quarter": ["2023 Q1", "2023 Q2", "2023 Q3", "2023 Q4"],
    "Raw Hourly Output": [25, 26, 25.5, 27]
}

class TestEDAAnalysis(unittest.TestCase):

    def setUp(self):
        self.mc_final = pd.DataFrame(sample_data)
        self.raw_hours = pd.DataFrame(raw_hours_sample)
        self.raw_output = pd.DataFrame(raw_output_sample)

    def test_columns_exist(self):
        #test 1 - check essential columns exist
        cols = ["Quarter", "Gross Added Value", "Hours Worked", "Hourly Output"]
        for col in cols:
            self.assertIn(col, self.mc_final.columns)

    def test_dtypes(self):
        #test 2 - ensure numeric columns are numeric
        numeric_cols = ["Gross Added Value", "Hours Worked", "Hourly Output"]
        for col in numeric_cols:
            self.assertTrue(pd.api.types.is_numeric_dtype(self.mc_final[col]))

    def test_linregress_gva_hours(self):
        x = self.mc_final["Hours Worked"]
        y = self.mc_final["Gross Added Value"]
        result = linregress(x, y)
        self.assertIsInstance(result.slope, float)
        self.assertIsInstance(result.intercept, float)
        self.assertGreaterEqual(result.rvalue**2, 0)
        self.assertGreaterEqual(result.pvalue, 0)

    def test_linregress_hours_output(self):
        x = self.mc_final["Hours Worked"]
        y = self.mc_final["Hourly Output"]
        result = linregress(x, y)
        self.assertIsInstance(result.slope, float)
        self.assertIsInstance(result.intercept, float)

    def test_correlations(self):
        x = self.mc_final["Hours Worked"]
        y = self.mc_final["Hourly Output"]
        spearman_corr, spearman_p = spearmanr(x, y)
        kendall_corr, kendall_p = kendalltau(x, y)
        #test 3 - check correlations are numeric
        self.assertIsInstance(spearman_corr, float)
        self.assertIsInstance(kendall_corr, float)

    def test_merge_and_bins(self):
        #test 4 - merge sample raw hours/output like in main code
        merged = pd.merge(self.raw_hours, self.raw_output, on='Quarter', how='inner')
        self.assertEqual(len(merged), 4)  # all quarters present

        #test 5 - test binning
        merged['Hours_bin'] = pd.qcut(merged['Raw Hours Worked'], q=3, labels=['Low', 'Medium', 'High'])
        merged['Output_bin'] = pd.qcut(merged['Raw Hourly Output'], q=3, labels=['Low', 'Medium', 'High'])

        self.assertIn('Hours_bin', merged.columns)
        self.assertIn('Output_bin', merged.columns)
        #test 6 - check all labels exist
        self.assertTrue(set(merged['Hours_bin'].unique()) <= set(['Low', 'Medium', 'High']))
        self.assertTrue(set(merged['Output_bin'].unique()) <= set(['Low', 'Medium', 'High']))

        #test 7 - chi-squared
        contingency = pd.crosstab(merged['Hours_bin'], merged['Output_bin'])
        chi2, p, dof, expected = chi2_contingency(contingency)
        self.assertGreaterEqual(chi2, 0)
        self.assertGreaterEqual(dof, 1)
        self.assertGreaterEqual(p, 0)

if __name__ == "__main__":
    unittest.main()
