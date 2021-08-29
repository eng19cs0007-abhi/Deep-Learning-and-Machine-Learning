#K nearest neighbours
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
X = [[30],[40],[50],[60],[20],[10],[70]]
Y = [0,1,1,1,0,0,1]
# Here 0 means fail and 1 means pass
from sklearn.neighbors import KNeighborsClassifier  
classifier= KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2 )  
classifier.fit(X,Y)
a=int(input("Enter marks ")) 
X_marks=[[a]]
print(classifier.predict(X_marks))
