# Chapter 01 – PCA & t-test Mini Project

## Objective
In this project, synthetic data was generated to compare the performance of two athlete groups: **runners** and **swimmers**.  
The focus is on applying:  
- **Principal Component Analysis (PCA)** for dimensionality reduction  
- **t-test** for statistical comparison of group means  

---

## Data
- Each athlete has 5 features (score columns).  
- Sample size: 10 runners + 10 swimmers.  
- Data was generated with NumPy random functions.  

---

## Methods
1. PCA was applied to reduce the original 5-dimensional feature space to 2D.  
2. t-tests were performed on each feature to test whether the mean scores of runners and swimmers differ significantly.  
3. Results include a scatter plot (from PCA) and p-values for each column.  

---

## How to Run
```bash
python main.py

Results
PCA Visualization
(Scatter plot of runners vs. swimmers in 2D space)
t-test results (example output):
t-test results for each column:
col_1: t=0.57, p=0.57
col_2: t=-1.23, p=0.23
col_3: t=2.31, p=0.03
col_4: t=-0.87, p=0.39
col_5: t=1.44, p=0.16