# Random forest
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
X = [[30],[40],[50],[60],[20],[10],[70]]
Y = [0,1,1,1,0,0,1]
# Here 0 means fail and 1 means pass
RandomForestRegModel = RandomForestRegressor()
RandomForestRegModel.fit(X,y)
classifier.fit(X,Y)
a=int(input("Enter the marks "))
X_marks=[[a]]
print(RandomForestRegModel.predict(X_marks))
