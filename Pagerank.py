#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import random
# %run src/graph.py
import graph


# In[11]:


pages, links = 3, 4  #map(int,input().split())
d = 0.85
iterations = 52
assert d <= 1


# In[3]:


pageGraph = np.zeros(shape=(pages,pages))


# In[4]:


for i in range(links):
    x,y = graph.genEdges(0,pages-1,pageGraph)
    pageGraph[x,y] = 1


# In[5]:


print(pageGraph)


# In[6]:


outLinks = graph.getOutDegree(pageGraph)


# In[7]:


print(outLinks)


# In[8]:


pageRank = np.zeros(shape=(pages)) + 1/pages


# In[9]:


print(pageRank)


# In[12]:


for i in range(iterations):
    for j in range(pages):
        for k in range(pages):
            pageRank[j] = 1 - d
            if pageGraph[j,k]:
                pageRank[j] += d * pageRank[k]/outLinks[k]


# In[14]:


print(pageRank)


# In[ ]:




