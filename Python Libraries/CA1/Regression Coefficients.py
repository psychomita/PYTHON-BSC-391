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
y_predicted=model.predict(np.array([[21.3,1109]]))
print("Predicted value of y for x1= 21.3 and x2= 1109 is ",y_predicted)
