#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import random
import graph


# In[18]:


pages, links = 3, 4  #map(int,input().split())
d = 0.85
epsilon = 1
assert links <= pages*pages
assert d <= 1


# In[6]:


pageGraph = np.zeros(shape=(pages,pages))


# In[8]:


for i in range(links):
    x,y = graph.genEdges(0,pages-1,pageGraph)
    pageGraph[x,y] = 1


# In[9]:


print(pageGraph)


# In[10]:


inLinks, outLinks = graph.getInDegree(pageGraph), graph.getOutDegree(pageGraph)


# In[11]:


print(inLinks)


# In[12]:


print(outLinks)


# In[13]:


pageRank = np.zeros(shape=(pages))


# In[16]:


for i in range(pages):
    pageRank[i] = inLinks[i]/(epsilon+outLinks[i]) # Issue: Divide by Zero


# In[17]:


print(pageRank)


# In[ ]:




