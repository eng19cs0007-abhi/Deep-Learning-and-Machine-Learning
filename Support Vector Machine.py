#SVM 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.svm import SVC
X = [[30],[40],[50],[60],[20],[10],[70]]
Y = [0,1,1,1,0,0,1]
# Here 0 means fail and 1 means pass
classifier = SVC(kernel = 'linear', random_state = 0)
classifier.fit(X,Y)
a=int(input("Enter the marks "))
X_marks=[[a]]
print(classifier.predict(X_marks))
