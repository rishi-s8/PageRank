#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import random
import graph


# In[2]:


pages, links = 100, 250  #map(int,input().split())
epsilon = 1e-4
d = 0.85
iterations = 10000000
assert links <= 2*pages*pages
assert d <= 1


# In[3]:


def mapper_mult(adjacencyFunction, pageRank):
    intermediate = {}
    for i in range(pageRank.shape[0]):
        for j in range(pageRank.shape[0]):
            key = str(i)
            if key in intermediate.keys():
                intermediate[key].append("A,{},{}".format(j,adjacencyFunction[i,j]))
            else:
                intermediate[key]=["A,{},{}".format(j,adjacencyFunction[i,j])]
    
    for i in range(pageRank.shape[0]):
        key = str(i)
        intermediate[key].append("P,{},{}".format(i,pageRank[j]))
#         print("Adding Key:")
    
#     print("intermediate: {}".format(intermediate))
    
    return intermediate


# In[4]:


def reducer_mult(intermediate):
    AVals = {}
    PVals = {}
    for i in intermediate:
        val_arr = intermediate[i]
#         print("val_arr: {}".format(val_arr))
        for j in val_arr:
            mat, ind, val = j.split(',')
            ind = int(ind)
            val = float(val)
            if mat == 'A':
                if int(i) in AVals.keys():
                    AVals[int(i)].append((ind,val))
                else:
                    AVals[int(i)]=[(ind,val)]
            else:
                PVals[ind] = val
#     print("AVals: {}".format(AVals))
#     print("PVals: {}".format(PVals))
    
    reduced = {}
    for i in AVals:
        val_arr = AVals[i]
        reduced[i] = (1-d)/pages
        for j in val_arr:
            reduced[i] += j[1] * PVals[j[0]]
            
    return reduced


# In[5]:


pageGraph = np.zeros(shape=(pages,pages))


# In[6]:


for i in range(links):
    x,y = graph.genEdges(0,pages-1,pageGraph)
    pageGraph[x,y] = 1
pageGraph


# In[7]:


outLinks = graph.getOutDegree(pageGraph)
print(outLinks)


# In[8]:


pageRank = np.zeros(shape=(pages)) + 1/pages
print(pageRank)


# In[9]:


adjacencyFunction = graph.getAdjacencyFunction(pageGraph)
print(adjacencyFunction)


# In[10]:


for i in range(iterations):
    pageRankNew = reducer_mult(mapper_mult(adjacencyFunction, pageRank))
#     print(pageRankNew)
    temp = np.zeros(shape=pageRank.shape)
    for j in pageRankNew: temp[j] = pageRankNew[j]
    if np.allclose(temp,pageRank, atol=epsilon, rtol=0.0):
        print(i)
        break
    pageRank = temp
    print(pageRank)


# In[11]:


print(pageRank)


# In[12]:


reducer_mult(mapper_mult(adjacencyFunction, pageRank))


# In[ ]:





# In[ ]:





# In[ ]:




