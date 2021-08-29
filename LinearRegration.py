# Linear Regression
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn
from sklearn import linear_model
height=[[4.0],[5.0],[6.0],[7.0],[8.0],[9.0],[10.0]]
weight=[  9, 11 , 13, 15, 17, 19, 21]
plt.scatter(height,weight,color='blue')
plt.xlabel("height")
plt.ylabel("weight")
reg=linear_model.LinearRegression()
reg.fit(height,weight)
a=float(input("Enter a number "))
X_height=[[a]]
print(reg.predict(X_height))
