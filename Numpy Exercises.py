#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___

# # NumPy Exercises 
# 
# Now that we've learned about NumPy let's test your knowledge. We'll start off with a few simple tasks, and then you'll be asked some more complicated questions.

# #### Import NumPy as np

# In[1]:


import numpy as np


# #### Create an array of 10 zeros 

# In[5]:


np.zeros(10)


# #### Create an array of 10 ones

# In[6]:


np.ones(10)


# #### Create an array of 10 fives

# In[8]:


np.ones(10) * 5


# #### Create an array of the integers from 10 to 50

# In[9]:


np.arange(10,51)


# #### Create an array of all the even integers from 10 to 50

# In[11]:


np.arange(10,51,2)


# #### Create a 3x3 matrix with values ranging from 0 to 8

# In[14]:


np.array([[0,1,2],[3,4,5], [6,7,8]])


# #### Create a 3x3 identity matrix

# In[13]:


np.eye(3)


# #### Use NumPy to generate a random number between 0 and 1

# In[16]:


np.random.rand(1)


# #### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution

# In[17]:


np.random.randn(25)


# #### Create the following matrix:

# In[21]:


np.arange(0.01,1.01,0.01).reshape(10, 10)


# #### Create an array of 20 linearly spaced points between 0 and 1:

# In[22]:


np.linspace(0, 1, 20)


# ## Numpy Indexing and Selection
# 
# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:

# In[23]:


mat = np.arange(1,26).reshape(5,5)
mat


# In[41]:


mat[2:,1:]


# In[44]:


mat[2:][:,1:]


# In[41]:


mat[3,4]


# In[30]:


mat[:3,1:2]


# In[31]:


mat[4]


# In[32]:


mat[3:]


# ### Now do the following

# #### Get the sum of all the values in mat

# In[33]:


np.sum(mat)


# #### Get the standard deviation of the values in mat

# In[34]:


np.std(mat)


# #### Get the sum of all the columns in mat

# In[40]:


np.sum(mat, axis=0)


# # Great Job!
