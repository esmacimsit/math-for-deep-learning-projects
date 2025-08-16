# Chapter 01 – PCA & t-test Mini Project

## Objective
This project compares the performance of two athlete groups (**runners** vs. **swimmers**) using:  
- **Principal Component Analysis (PCA)** for dimensionality reduction  
- **t-test** for statistical hypothesis testing  

---

## Data
- Each athlete has 5 features (score columns).  
- Sample size: 10 runners + 10 swimmers.  
- Data generated with NumPy random functions.  

---

## Methods
1. PCA was applied to reduce the original 5-dimensional feature space to 2D.  
2. Independent two-sample t-tests were performed on each feature to check whether runners and swimmers differ significantly.  
3. Results include a scatter plot (from PCA) and p-values for each column.  

---

## Results

### PCA Visualization
*(scatter plot of runners vs. swimmers in 2D PCA space)*

### t-test Results (example)
| Feature | t-stat | p-value |
|---------|--------|---------|
| col_1   | 0.57   | 0.57    |
| col_2   | -1.23  | 0.23    |
| col_3   | 2.31   | 0.03    |
| col_4   | -0.87  | 0.39    |
| col_5   | 1.44   | 0.16    |

---

## Additional Implementations (libs.py)
The `libs.py` file contains small demonstrations of four libraries:  
- **NumPy** → array creation, type casting, and basic operations  
- **SciPy** → statistical tests such as `ttest_ind`  
- **matplotlib** → simple plotting and visualization  
- **scikit-learn (digits dataset)** → applying PCA and training an MLPClassifier for digit recognition  

These implementations were added as supporting experiments to practice fundamental concepts in numerical computing, statistics, visualization, and machine learning workflows.

---

## Learnings
- PCA is a useful method for reducing high-dimensional data into a lower-dimensional space for visualization and analysis.  
- t-tests are effective for comparing the means of two groups and checking whether observed differences are statistically significant.  
- Working with synthetic data helps to understand statistical methods without the complexity of real-world datasets.  
- Combining theory (math concepts) with implementation (NumPy, scikit-learn) provides a deeper understanding of machine learning foundations.  

---

## How to Run
```bash
python main.py
