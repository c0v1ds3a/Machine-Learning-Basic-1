# Import necessary libraries
import numpy as np
from sklearn import datasets
from sklearn import svm

# Load the iris dataset
iris = datasets.load_iris()

# Create a support vector machine classifier
clf = svm.SVC(gamma=0.001, C=100.)

# Fit the model to the data
clf.fit(iris.data, iris.target)

# Predict the label for a new sample
print(clf.predict([[5.0, 3.6, 1.3, 0.25]]))
