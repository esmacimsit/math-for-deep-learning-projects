# warm up for each library on chapter 1
# !!do not name your file as library name it can overlap with actual lib

# numpy: python library for fast numerical computing.
import numpy as np

numArr = np.array([[1, 2, 3, 4], [5, 6, 7, 8.0]]) # 2d array

print(numArr)
print(numArr.size)
print(numArr.shape)
print(numArr.dtype) # float64
print(numArr[1, 2])

numArr = numArr.astype('uint8')

print(numArr.dtype) # uint8
# watch out for overflow while dtyping it can cause data loss silently!!

zeroArr = np.zeros((3, 4), dtype='uint32') # create 3x4 matrix with zeros
zeroArr[0, 3] = 42 # put 42 at row index 0 and column index 3
zeroArr[1, 1] = 66 # put 66 at row 1 column 1

print(zeroArr)

oneArr = 11*np.ones((3, 1)) # create a 3x1 matrix with ones and multiply by 11

print(oneArr)

arangedArr = np.arange(12).reshape(3, 4) # arange() works like range(), reshape() makes it 3x4

print(arangedArr)
print(arangedArr[1]) # give row index 1

arangedArr[1] = [44, 55, 66, 77] # replace it

print(arangedArr)
print(arangedArr[:2]) # start : stop : step, first 2 rows
print(arangedArr[:2,:]) # first two rows and all columns
print(arangedArr[:2,:3]) # 2 rows 3 columns

anotherAranged = np.arange(12)

print(anotherAranged)
print(anotherAranged[::2]) # 2 steps
print(anotherAranged[::3]) # 3 steps
print(anotherAranged[::-1]) # reverse
print('***')

threeDarr = np.arange(24).reshape((4,3,2)) # x, depth(times) y, row z, column

print(threeDarr)

threeDarr[1,:,:] = [[11,22],[33,44],[55,66]] # index 1 depth all, first 3x2 matrix

print(threeDarr)

threeDarr[2,...] = [[99,99],[99,99],[99,99]] # == [2,;,:]

print(threeDarr)
print('***')

unsavedArr = np.random.randint(0,5,(3,4)) # 3x4 matrix w random 0-5

print(unsavedArr)

np.save('random.npy', unsavedArr) # saving
savedArr = np.load('random.npy')

print(savedArr)

# scipy = python library that builds on numpy and provides advanced functions.
from scipy.stats import ttest_ind
# t test == compare statistically, p value == coincidence prob
arrA = np.random.normal(0,1,1000) # Gaussian distribution
arrB = np.random.normal(0,0.5,1000)
arrC = np.random.normal(0.1,1,1000)

print(ttest_ind(arrA, arrB)) # give result and p value
print(ttest_ind(arrA, arrC)) # smaller p value == real result

# matplotlib = python library for creating visualizations like plots and charts.
import matplotlib.pylab as plt

exp = np.random.random(100)

plt.plot(exp) # draw graph
plt.show() # display it

x = np.random.random(20)
y = np.random.random(20)
z = np.random.random(20)

fig = plt.figure() # create empty figure
ax = fig.add_subplot(111, projection='3d') # make it 3d and 1 by 1

ax.scatter(x,y,z) # draw graph
plt.show() # display it

# scikit-learn = python library for machine learning.
from sklearn.datasets import load_digits
from sklearn.neural_network import MLPClassifier

loaded = load_digits() # get images and tags
digits = loaded['data'] # images
labels = loaded['target'] # tags
N = 200 # examples

idx = np.argsort(np.random.random(len(labels))) # random num
x_test, y_test = digits[idx[:N]], labels[idx[:N]] # test set until N
x_train, y_train = digits[idx[N:]], labels[idx[N:]] # train rest of it
clf = MLPClassifier(hidden_layer_sizes=(128,))

clf.fit(x_train, y_train) # train model
score = clf.score(x_test, y_test) # accuracy
pred = clf.predict(x_test) # predictions
err = np.where(y_test != pred)[0] # misclassfied test samples

print("score : ", score)
print("errors: ")
print("actual : ", y_test[err])
print("predicted: ", pred[err])
# load dataset -> shuffle and split as train, test -> set MLP(classifier) -> fit, train -> compute accuracy -> list misclassified ones

