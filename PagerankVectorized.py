#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import random
import graph


# In[2]:


pages, links = 100, 250  #map(int,input().split())
epsilon = 1e-9
d = 0.85
iterations = 10000000
assert links <= pages*pages
assert d <= 1


# In[3]:


pageGraph = np.zeros(shape=(pages,pages))


# In[4]:


for i in range(links):
    x,y = graph.genEdges(0,pages-1,pageGraph)
    pageGraph[x,y] = 1
pageGraph


# In[5]:


outLinks = graph.getOutDegree(pageGraph)


# In[6]:


pageRank = np.zeros(shape=(pages)) + 1/pages


# In[7]:


adjacencyFunction = graph.getAdjacencyFunction(pageGraph)


# In[8]:


for i in range(iterations):
    pageRankNew = (1-d)/pages + d * np.matmul(adjacencyFunction, pageRank)
    if np.allclose(pageRankNew,pageRank, atol=epsilon, rtol=0.0):
        print(i)
        break
    pageRank = pageRankNew


# In[9]:


print(pageRank)

