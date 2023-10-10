import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import linear_model

df=pd.read_csv(r"C:\Users\suchi\OneDrive\Desktop\Plot\table.csv")
features=['x1','x2']

target='Y'
y=df[features].values.reshape(-1,len(features))
x=df[target].values
ols=linear_model.LinearRegression()
model=ols.fit(y,x)
print("The coefficients of [x1,x2]= ",model.coef_)
print("The coefficient of Y= ",model.intercept_)
