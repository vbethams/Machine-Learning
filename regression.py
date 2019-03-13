import numpy as np
import pandas as pd
x= np.array([95,85,80,70,60])
y=np.array([85,95,70,65,70])

x_mean = np.mean(x)
y_mean = np.mean(y)


num = sum(( x-x_mean) * (y-y_mean))
denom = sum((x-x_mean)**2)
b1= num/denom

b0 = y_mean - b1 *(x_mean)

ypred =b1*x+b0
y= y.reshape(-1,1)
ypred = ypred.reshape(-1,1)
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

brain = pd.read_csv('headbrain.csv')
brain = brain.drop(['Gender',''])