# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 12:34:41 2018

@author: senthilku
"""

import pandas as pd
import numpy as np

data=pd.read_csv('xyz.csv', header=None, index_col=0)
y=data[4].reshape(-1,1)

data.drop(4,axis=1,inplace=True)

from sklearn.cluster import KMeans

model=KMeans(n_clusters=2,random_state=0)

model.fit(data)
group=model.predict(data)
group1=group.reshape(-1,1)

out_mat=np.concatenate((group1,y),axis=1)
out_mat1=out_mat[0:33676,:]



count=0
for i in range(0,len(out_mat1)):
       if out_mat1[i,0] == out_mat1[i,1]:
           count=count+1

           
                  
count1=0;count2=0
for i in range(0,len(out_mat1)):
       if out_mat1[i,0] == 0:
           count1=count1+1
       if out_mat1[i,0]==1:
           count2=count2+1
           
df=pd.DataFrame(out_mat1)
df1=df.sort_values(by=0,axis=0)
df_arr=np.array(df1)
data_grp1=df_arr[367:33677,:]

#count=0
#out_mat2={}
#for i in range(0,len(out_mat1)):
#       if out_mat1[i,0] != out_mat1[i,1]:
#           out_mat1[i,:]=0
#          
#from sklearn.decomposition import PCA
#pca=PCA(2)
#pcafit=pca.fit(data)
#pca_data=pcafit.transform(data)
#
#import matplotlib.pyplot as plt
#plt.scatter(pca_data[:,0],pca_data[:,1],c=group)






