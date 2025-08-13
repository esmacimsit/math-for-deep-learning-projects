# chapter 1 based mini project: PCA visualization and statistical comparison of athlete scores
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

runner = np.random.randint(1, 11, (10, 5)) # each row = 1 runner, each column = 1 score
swimmer = np.random.randint(1, 11, (10, 5))

athlete = np.array(['runner']*len(runner) + ['swimmer']*len(swimmer)) # labeling
scoreTable = np.vstack([runner, swimmer]) # concat runner and swimmer

print(athlete.shape)
print(scoreTable.shape) # 5d

pca = PCA(n_components=2) # reduce dimension
scoreTable2d = pca.fit_transform(scoreTable)

print(scoreTable2d.shape) # 2d

colors = [] # show runner as red swimmer as blue
for tag in athlete:
    if tag == 'runner':
        colors.append('red')
    else:
        colors.append('blue')

plt.scatter(scoreTable2d[:, 0], scoreTable2d[:, 1], c=colors) # 0 = x, 1 = y
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('PCA of Athlete Scores')

for i in range(runner.shape[1]): # loop over column num
    runnerScores = runner[:, i] # i index scores
    swimmerScores = swimmer[:, i]
    t_stat, p_val = ttest_ind(runnerScores, swimmerScores)

    if p_val < 0.05:
        print(f"Test {i + 1}: p-value={p_val:.3f} → significant difference") # turn index to real order
    else:
        print(f"Test {i + 1}: p-value={p_val:.3f} → no significant difference")

plt.show() # wrote it the end cause it blocks terminal outputs