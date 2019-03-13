# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 16:23:31 2018

@author: senthilku
"""

import numpy as np
data=np.array([[1,2],[6,7],[1,3],[2,1],[8,6],[7,9]])
k=2
seed=np.random.randint(1,6,2)

#c1=data[seed[0]].reshape(1,-1)
#c2=data[seed[1]].reshape(1,-1)
#clust=np.concatenate((c1,c2))

c1=np.array([1,2]).reshape(1,-1)
c2=np.array([1,3]).reshape(1,-1)
clust=np.concatenate((c1,c2))

dist=np.zeros([6,2])
n=0
while(n<10):
    for i in range(k):
        for j in range(6):
            dist[j,i]=np.sqrt(sum((clust[i,:]-data[j,:])**2))
            
    mi=np.argmin(dist,axis=1)  
    
    clust1=data[mi==0]   
    clust2=data[mi==1] 
    
    c1_upd=np.mean(clust1,axis=0) 
    c1_upd=c1_upd.reshape(1,-1)
    
    c2_upd=np.mean(clust2,axis=0) 
    c2_upd=c2_upd.reshape(1,-1)
    
    print(c1_upd)
    print(c2_upd)
    
    d1=np.sum((np.abs(c1-c1_upd)))
    d2=np.sum((np.abs(c2-c2_upd)))

    if (d1==0 and d2==0):
        break
    c1=c1_upd
    c2=c2_upd
    clust=np.concatenate((c1_upd,c2_upd))
    n=n+1
print("The cluster1:") 
print(clust1)  
print("The cluster2:") 
print(clust2)
    



        

    


