#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install matplotlib==3.4')


# In[3]:


from matplotlib import pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np


# In[4]:


fig = plt.figure()
ax = plt.axes()


# In[13]:


fig = plt.figure()
ax = plt.axes()

x = np.linspace(0, 10, 1000)
ax.plot(x, np.sin(x));


# In[14]:


fig = plt.figure()
ax = plt.axes()

x = np.linspace(0, 10, 1000)
ax.plot(x, np.sin(x))
ax.set_title('Today Class')
ax.set_xlabel('Day label')
ax.set_ylabel('Calss label');


# In[15]:


fig = plt.figure()
ax = plt.axes()

x = np.linspace(0, 10, 1000)
ax.plot(x, np.sin(x))
ax.plot(x, np.cos(x))
ax.set_title('Multiple Lines');
ax.set_xlabel('x label')          
ax.set_ylabel('y label')         
plt.show()


# In[16]:



fig = plt.figure()
ax = plt.axes()

x = np.linspace(0, 10, 1000)
ax.plot(x, np.sin(x), label = 'sin')
ax.plot(x, np.cos(x), label = 'cos')
ax.set_title('Multiple Lines');
ax.set_xlabel('x label')          
ax.set_ylabel('y label')
ax.legend()          
plt.show()


# In[17]:



fig = plt.figure()
ax = plt.axes()

x = np.linspace(0, 10, 1000)
ax.plot(x, np.sin(x), label = 'sin', color = 'red')
ax.plot(x, np.cos(x), label = 'cos', color = 'g')
ax.set_title('Multiple Lines');
ax.set_xlabel('x label')          
ax.set_ylabel('y label')
ax.legend();  


# In[18]:




fig = plt.figure()
ax = plt.axes()
x = np.linspace(0, 10, 1000)
ax.plot(x, np.sin(x), label = 'sin', linestyle = 'dashed')   
ax.plot(x, np.cos(x), label = 'cos', linestyle = 'dotted')
ax.plot(x, np.sin(x+1), label = 'cos', linestyle = 'dashdot')
ax.set_title('Multiple Lines');
ax.set_xlabel('x label')          
ax.set_ylabel('y label')
ax.legend();


# In[ ]:




