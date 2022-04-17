#!/usr/bin/env python
# coding: utf-8

# In[10]:


import re
import numpy as np


# In[11]:


str = '{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}]}'


# In[12]:


str


# In[13]:


numbers_list = re.findall('\d+',str)


# In[14]:


numbers_list


# In[15]:


list = [int(i) for i in numbers_list]


# In[22]:


list


# In[17]:


array= np.array(list)


# In[18]:


array


# In[20]:


import re
import numpy as np
str = '{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}]}'
numbers_list = re.findall('\d+',str)
list = [int(i) for i in numbers_list]
array= np.array(list)
array


# In[ ]:




