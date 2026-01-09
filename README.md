# Are Consultants More Productive When They Work Longer Hours?

## Academic Research Project | DAT5501

---

## Research Objectives

This analysis establishes two competing hypotheses:

- **H₀ (Null Hypothesis):** Working more hours does not significantly increase the hourly productivity of management consultants
- **H₁ (Alternative Hypothesis):** Working more hours significantly increases the hourly productivity of management consultants

The research seeks to determine whether extended working hours genuinely translate into enhanced productivity or whether this assumption represents a poorly constructed notion requiring dismantling for organisational wellbeing.

---

## Data Sources

### Primary Datasets

**1. ONS Productivity Estimates** (`master_productivityds.xlsx`)
- Source: "Output per hour worked by division, UK"
- Classification: Standard Industrial Classification 2007
- Variables: Gross Value Added (GVA), Hours Worked, Hourly Output
- Period: 1998 Q1 - 2025 Q2 (109 observations)
- Format: Multi-sheet Excel file with division-level metrics

**2. Revenue Data** (`total_revenue.csv`)
- Source: Office for National Statistics
- Classification: GBServTO: 70.2 (Management Consulting Services)
- Period: 1998 Q1 - 2025 Q2
- Format: Quarterly total revenue figures

---

## Methodology

### 1. Data Preparation and Cleaning

**Tools:** Python (pandas, numpy)

#### Data Extraction
- Revenue dataset processed to remove metadata rows and standardise column naming conventions
- Productivity tables extracted from multi-sheet Excel source files

#### Data Transformation
- Custom reindexing function developed to convert base year from 2023 to 2025
- Scaling factors calculated between reference periods to ensure temporal consistency
- Quarterly identifiers used to merge cleaned datasets into unified analytical dataset

<img width="1710" height="1112" alt="Screenshot 2026-01-09 at 19 54 49" src="https://github.com/user-attachments/assets/767ff6db-c23e-4fdf-84e3-4ebd0a1c254e" />

_Screenshot of data cleaning work in VScode_

**Implementation Files:**
- `cleaning_and_merging/cleaning_masterproductivityds.ipynb`
- `cleaning_and_merging/cleaning_totalrev.ipynb`
- `cleaning_and_merging/merging_datasets.ipynb`

**Output:** `datasets/management_consulting_final.csv`

---

### 2. Exploratory Data Analysis (EDA)

**Tools:** Python (pandas, matplotlib, seaborn)

#### Temporal Pattern Analysis
Initial visualisation examined variable movements over quarterly timeframe, revealing:
- Hours worked and gross value added exhibited parallel movement patterns
- Hours worked and hourly output demonstrated no such coordinated movement

#### Hierarchical Clustering Analysis
Dendrogram construction and color-coded heatmap:
- Revealed GVA and hours worked cluster closely together with similar quarterly patterns
- Hourly output appeared separated from these variables, suggesting weaker underlying relationships

#### Correlation Matrix Analysis
Correlation heatmap generation confirmed initial observations:
- Strong positive correlation between GVA and hours worked (r = 0.94)
- Modest correlation between hourly output and hours worked (r = 0.25)

<img width="515" height="435" alt="image" src="https://github.com/user-attachments/assets/d9e53528-9d58-4048-a7c4-4da85c8eb131" />

_Correlation heatmap quantifying pairwise relationships between variables_

#### Normality Testing
Statistical assumptions verified for all variables prior to parametric analysis, addressing methodological requirements for robust correlation analysis (Onwuegbuzie & Daniel, 1999).

**Implementation Files:**
- `eda_and_analysis_ipynbF/brief_eda.ipynb`

---

### 3. Statistical Analysis

**Tools:** Python (scipy, statsmodels, numpy, matplotlib, seaborn)

#### Ordinary Least Squares (OLS) Regression

**Model 1: Hours Worked vs. Gross Value Added**
- **Purpose:** Establish baseline relationship between labor input and aggregate output
- **Method:** Linear regression with confidence interval estimation
- **Results:**
  - Slope: 0.887
  - Pearson correlation coefficient: 0.938 (p = 1.57×10⁻⁵¹)
  - R² = 0.88 (hours worked explains 88% of GVA variation)
- **Validation:** Bayesian Information Criterion testing (ΔBIC = -228.49) strongly favored linear model over null model
- **Interpretation:** Confirms arithmetical truism that aggregate labor input generates aggregate output

<img width="800" height="600" alt="newplotq" src="https://github.com/user-attachments/assets/cacead74-53ec-44a1-b889-749f40b5432d" />

_Scatter plot showing the strong positive linear relationship between hours worked and gross added value in UK management consulting (2025 = 100)_

**Model 2: Hours Worked vs. Hourly Output (Primary Analysis)**
- **Purpose:** Address core research question regarding productivity per hour
- **Method:** Linear regression with multiple validation techniques
- **Results:**
  - Slope: 0.105
  - Pearson correlation: 0.250 (p = 0.008)
  - R² = 0.06 (hours worked explains only 6% of hourly productivity variance)
- **Interpretation:** Despite statistical significance, relationship proves markedly weak

<img width="800" height="600" alt="newplot" src="https://github.com/user-attachments/assets/275ce99b-925d-415f-ad42-190d08fa9b65" />

_Scatter plot illustrating the weak relationship between hourly output and hours worked in UK management consulting (2025 = 100)_

#### Non-Parametric Validation
To avoid linearity assumptions and ensure robustness:
- **Spearman correlation:** 0.271 (p = 0.004)
- **Kendall correlation:** 0.158 (p = 0.015)
- **Conclusion:** Confirmed statistical significance while reinforcing weakness of association

#### Chi-Square Analysis
Categorical validation using quantile-binned data:
- Variables categorized into "Low", "Medium", "High" groups
- χ² = 96.32 (df = 4, p = 5.98×10⁻²⁰)
- **Interpretation:** Statistically significant association between categories, but hours worked explains minimal variation in productivity groupings

**Implementation Files:**
- `eda_and_analysis_ipynbF/main.ipynb`

---

### 4. Continuous Integration and Testing

**Tools:** CircleCI, pytest

#### Automated Testing Framework
- **EDA Test Suite:** `tests/test_suite_eda.py`
  - Validates data loading procedures
  - Verifies exploratory analysis outputs
  - Ensures visualisation generation integrity

- **Main Analysis Test Suite:** `tests/test_suite_main.py`
  - Validates regression model computations
  - Verifies correlation calculations
  - Tests statistical hypothesis procedures

#### CI/CD Pipeline
- **Configuration:** `.circleci/config.yml`
- **Purpose:** Automated testing on code commits to ensure reproducibility
- **Workflow:** Test execution triggered on repository updates

---

## Key Findings

### Primary Results

1. **Hours-GVA Relationship (R² = 0.88)**
   - Strong positive relationship confirmed
   - Represents expected arithmetical relationship: more time invested generates more aggregate output
   - Does not address efficiency or productivity per hour worked

2. **Hours-Hourly Productivity Relationship (R² = 0.06)**
   - Weak association despite statistical significance
   - Hours worked explains only 6% of variance in hourly productivity
   - Validated through multiple statistical methods (Pearson, Spearman, Kendall, chi-square)
   - Scatter pattern shows highest performers distributed across varying hour ranges rather than clustering at maximum hours

---

## Conclusions

The analysis provides compelling evidence supporting the null hypothesis: **working more hours does not significantly increase the hourly productivity of management consultants**. The result emerges from examining hourly productivity, where hours worked explains only 6% of variance despite achieving statistical significance.

---

## Repository Structure

```
ConsultingHoursProductivity/
├── .circleci/
│   └── config.yml                          # CI/CD pipeline configuration
├── cleaning_and_merging/
│   ├── cleaning_masterproductivityds.ipynb # Productivity data cleaning
│   ├── cleaning_totalrev.ipynb             # Revenue data cleaning
│   └── merging_datasets.ipynb              # Dataset integration
├── datasets/
│   ├── management_consulting_final.csv     # Final merged dataset
│   ├── master_productivityds.xlsx          # Raw productivity data
│   └── total_revenue.csv                   # Raw revenue data
├── eda_and_analysis_ipynbF/
│   ├── brief_eda.ipynb                     # Exploratory data analysis
│   └── main.ipynb                          # Primary statistical analysis
├── tests/
│   ├── test_suite_eda.py                   # EDA validation tests
│   └── test_suite_main.py                  # Main analysis validation tests
├── README.md                               # This file
└── requirements.txt                        # Python dependencies
```

---

## Technical Stack

### Core Libraries
- **pandas:** Data manipulation and cleaning
- **numpy:** Numerical computations and array operations
- **scipy:** Statistical testing and correlation analysis
- **statsmodels:** Regression modeling and hypothesis testing
- **matplotlib:** Base visualization framework
- **seaborn:** Statistical data visualization

### Development Tools
- **pytest:** Automated testing framework
- **CircleCI:** Continuous integration and deployment
- **Jupyter Notebook:** Interactive analysis environment

---

## Reproducibility

### Requirements
```
pandas>=2.0.0
numpy>=1.24.0
scipy>=1.10.0
statsmodels>=0.14.0
matplotlib>=3.7.0
seaborn>=0.12.0
pytest>=7.3.0
jupyter>=1.0.0
```

### Installation
```bash
pip install -r requirements.txt
```

### Execution Order
1. **Data Cleaning:**
   - Run `cleaning_masterproductivityds.ipynb`
   - Run `cleaning_totalrev.ipynb`
   - Run `merging_datasets.ipynb`

2. **Analysis:**
   - Run `brief_eda.ipynb` for exploratory analysis
   - Run `main.ipynb` for primary statistical analysis

3. **Validation:**
   ```bash
   pytest tests/
   ```
