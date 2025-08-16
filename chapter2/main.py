# sample space and events

sampleSpace = [] # sample space of two dice rolling
eventSum5 = []
eventSum8 = []

for i in range(1,7): # first dice = i, second = j
    for j in range(1,7):
        sampleSpace.append((i, j))
        if i + j == 5:
            eventSum5.append((i, j))
        elif i + j == 8:
            eventSum8.append((i, j))

print(len(eventSum5) / len(sampleSpace)) # probability of rolling two dice sum of 5
print(len(eventSum8) / len(sampleSpace))

# random variables

import numpy as np

randomNum = np.random.rand(10000) # generate random num

mask1 = (randomNum >= 0) & (randomNum < 0.25) # split 4 pieces
mask2 = (randomNum >= 0.25) & (randomNum < 0.5)
mask3 = (randomNum >= 0.5) & (randomNum < 0.75)
mask4 = (randomNum >= 0.75) & (randomNum <= 1)

prob1 = np.sum(mask1) / len(randomNum)
prob2 = np.sum(mask2) / len(randomNum)
prob3 = np.sum(mask3) / len(randomNum)
prob4 = np.sum(mask4) / len(randomNum)

print(prob1, prob2, prob3, prob4)

# rules of probability




