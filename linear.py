# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 12:30:27 2018

@author: Name
"""
import numpy as np
import pandas as pd
brain = pd.read_csv('headbrain.csv')
print(brain.columns)
x= brain['Head Size(cm^3)'].values
y=brain['Brain Weight(grams)'].values
x= x.reshape(-1,1)
y= y.reshape(-1,1)
x_mean = np.mean(x)
y_mean = np.mean(y)
num = sum(( x-x_mean) * (y-y_mean))
denom = sum((x-x_mean)**2)
b1= num/denom

b0 = y_mean - b1 *(x_mean)

ypred =b1*x+b0

print(range(ypred))
out = np.concatenate((y,ypred),axis=1)

res = float(sum(ypred -y))
sq_err =float(sum((y-ypred)**2))
mse = np.mean((y-ypred)**2)
rmse = np.sqrt(np.mean((y-ypred)**2))
print("the residue is:",res)
print("the squared error is:",sq_err)
print("the mean squared error is:",mse)
print("the root mean squared error is:",rmse)

rsq = 1-( (sum((y-ypred )**2))/sum((y-y_mean)**2))
N=len(x)
p=1
rsq_adj =1-((1-rsq**2) * (N-1))/(N-p-1)
