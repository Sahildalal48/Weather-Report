#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[25]:


file = (r'C:\Users\Sahil Dalal\Downloads\jan.csv')
data = pd.read_csv(file)


# In[26]:


data.head()


# In[27]:


data.plot(x='year', y=['Average of Apparent Temperature (C)','Average of Humidity'])


# In[28]:


data.plot.bar(x='year', y=['Average of Apparent Temperature (C)','Average of Humidity'])


# In[29]:


data.plot(x='year', y=['Average of Apparent Temperature (C)','Average of Humidity'], subplots=True , layout=(2,2))


# In[30]:


data.plot(x='year', y='Average of Apparent Temperature (C)')


# In[31]:


# NOW LIKE THE MONTH OF JAN WE DO THE SAME ANALYSIS FOR THE MONTH OF FEB OVER DIFFERENT YEARS 
file = (r'C:\Users\Sahil Dalal\Downloads\feb.csv')
data = pd.read_csv(file)


# In[32]:


data.head()


# In[33]:


data.plot(x='year', y=['Average of Apparent Temperature (C)','Average of Humidity'])


# In[34]:


data.plot.bar(x='year', y=['Average of Apparent Temperature (C)','Average of Humidity'])


# In[35]:


data.plot(x='year', y=['Average of Apparent Temperature (C)','Average of Humidity'], subplots=True , layout=(2,2))


# In[36]:


data.plot(x='year', y='Average of Apparent Temperature (C)')


# In[37]:


# NOW LIKE THE MONTH OF JAN WE DO THE SAME ANALYSIS FOR THE MONTH OF MARCH OVER DIFFERENT YEARS 
file = (r'C:\Users\Sahil Dalal\Downloads\march.csv')
data = pd.read_csv(file)


# In[38]:


data.head()


# In[39]:


data.plot(x='year', y=['Average of Apparent Temperature (C)','Average of Humidity'])


# In[40]:


data.plot.bar(x='year', y=['Average of Apparent Temperature (C)','Average of Humidity'])


# In[41]:


data.plot(x='year', y=['Average of Apparent Temperature (C)','Average of Humidity'], subplots=True , layout=(2,2))


# In[42]:


data.plot(x='year', y='Average of Apparent Temperature (C)')


# In[43]:


# NOW LIKE THE MONTH OF JAN WE DO THE SAME ANALYSIS FOR THE APRIL OF FEB OVER DIFFERENT YEARS 
file = (r'C:\Users\Sahil Dalal\Downloads\april.csv')
data = pd.read_csv(file)


# In[44]:


data.head()


# In[45]:


data.plot(x='year', y=['Average of Apparent Temperature (C)','Average of Humidity'])


# In[46]:


data.plot.bar(x='year', y=['Average of Apparent Temperature (C)','Average of Humidity'])


# In[47]:


data.plot(x='year', y=['Average of Apparent Temperature (C)','Average of Humidity'], subplots=True , layout=(2,2))


# In[48]:


data.plot(x='year', y='Average of Apparent Temperature (C)')


# In[49]:


# NOW LIKE THE MONTH OF JAN WE DO THE SAME ANALYSIS FOR THE MONTH OF MAY OVER DIFFERENT YEARS 
file = (r'C:\Users\Sahil Dalal\Downloads\may.csv')
data = pd.read_csv(file)


# In[50]:


data.head()


# In[51]:


data.plot(x='year', y=['Average of Apparent Temperature (C)','Average of Humidity'])


# In[52]:


data.plot.bar(x='year', y=['Average of Apparent Temperature (C)','Average of Humidity'])


# In[53]:


data.plot(x='year', y=['Average of Apparent Temperature (C)','Average of Humidity'], subplots=True , layout=(2,2))


# In[54]:


data.plot(x='year', y='Average of Apparent Temperature (C)')


# In[55]:


# NOW LIKE THE MONTH OF JAN WE DO THE SAME ANALYSIS FOR THE MONTH OF JUNE OVER DIFFERENT YEARS 
file = (r'C:\Users\Sahil Dalal\Downloads\june.csv')
data = pd.read_csv(file)


# In[56]:


data.head()


# In[57]:


data.plot(x='year', y=['Average of Apparent Temperature (C)','Average of Humidity'])


# In[58]:


data.plot.bar(x='year', y=['Average of Apparent Temperature (C)','Average of Humidity'])


# In[59]:


data.plot(x='year', y=['Average of Apparent Temperature (C)','Average of Humidity'], subplots=True , layout=(2,2))


# In[60]:


data.plot(x='year', y='Average of Apparent Temperature (C)')


# In[61]:


# NOW LIKE THE MONTH OF JAN WE DO THE SAME ANALYSIS FOR THE MONTH OF JULY OVER DIFFERENT YEARS 
file = (r'C:\Users\Sahil Dalal\Downloads\july.csv')
data = pd.read_csv(file)


# In[62]:


data.head()


# In[63]:


data.plot(x='year', y=['Average of Apparent Temperature (C)','Average of Humidity'])


# In[64]:


data.plot.bar(x='year', y=['Average of Apparent Temperature (C)','Average of Humidity'])


# In[65]:


data.plot(x='year', y=['Average of Apparent Temperature (C)','Average of Humidity'], subplots=True , layout=(2,2))


# In[66]:


data.plot(x='year', y='Average of Apparent Temperature (C)')


# In[67]:


# NOW LIKE THE MONTH OF JAN WE DO THE SAME ANALYSIS FOR THE MONTH OF AUGUST OVER DIFFERENT YEARS 
file = (r'C:\Users\Sahil Dalal\Downloads\august.csv')
data = pd.read_csv(file)


# In[68]:


data.head()


# In[69]:


data.plot(x='year', y=['Average of Apparent Temperature (C)','Average of Humidity'])


# In[70]:


data.plot.bar(x='year', y=['Average of Apparent Temperature (C)','Average of Humidity'])


# In[71]:


data.plot(x='year', y=['Average of Apparent Temperature (C)','Average of Humidity'], subplots=True , layout=(2,2))


# In[72]:


data.plot(x='year', y='Average of Apparent Temperature (C)')


# In[73]:


# NOW LIKE THE MONTH OF JAN WE DO THE SAME ANALYSIS FOR THE MONTH OF SEPT OVER DIFFERENT YEARS 
file = (r'C:\Users\Sahil Dalal\Downloads\sept.csv')
data = pd.read_csv(file)


# In[74]:


data.head()


# In[75]:


data.plot(x='year', y=['Average of Apparent Temperature (C)','Average of Humidity'])


# In[76]:


data.plot.bar(x='year', y=['Average of Apparent Temperature (C)','Average of Humidity'])


# In[77]:


data.plot(x='year', y=['Average of Apparent Temperature (C)','Average of Humidity'], subplots=True , layout=(2,2))


# In[78]:


data.plot(x='year', y='Average of Apparent Temperature (C)')


# In[79]:


# NOW LIKE THE MONTH OF JAN WE DO THE SAME ANALYSIS FOR THE MONTH OF OCT OVER DIFFERENT YEARS 
file = (r'C:\Users\Sahil Dalal\Downloads\oct.csv')
data = pd.read_csv(file)


# In[80]:


data.head()


# In[81]:


data.plot(x='year', y=['Average of Apparent Temperature (C)','Average of Humidity'])


# In[82]:


data.plot.bar(x='year', y=['Average of Apparent Temperature (C)','Average of Humidity'])


# In[83]:


data.plot(x='year', y=['Average of Apparent Temperature (C)','Average of Humidity'], subplots=True , layout=(2,2))


# In[84]:


data.plot(x='year', y='Average of Apparent Temperature (C)')


# In[85]:


# NOW LIKE THE MONTH OF JAN WE DO THE SAME ANALYSIS FOR THE MONTH OF NOV OVER DIFFERENT YEARS 
file = (r'C:\Users\Sahil Dalal\Downloads\nov.csv')
data = pd.read_csv(file)


# In[86]:


data.head()


# In[87]:


data.plot(x='year', y=['Average of Apparent Temperature (C)','Average of Humidity'])


# In[88]:


data.plot.bar(x='year', y=['Average of Apparent Temperature (C)','Average of Humidity'])


# In[89]:


data.plot(x='year', y=['Average of Apparent Temperature (C)','Average of Humidity'], subplots=True , layout=(2,2))


# In[90]:


data.plot(x='year', y='Average of Apparent Temperature (C)')


# In[91]:


# NOW LIKE THE MONTH OF JAN WE DO THE SAME ANALYSIS FOR THE MONTH OF DEC OVER DIFFERENT YEARS 
file = (r'C:\Users\Sahil Dalal\Downloads\dec.csv')
data = pd.read_csv(file)


# In[92]:


data.head()


# In[93]:


data.plot(x='year', y=['Average of Apparent Temperature (C)','Average of Humidity'])


# In[94]:


data.plot.bar(x='year', y=['Average of Apparent Temperature (C)','Average of Humidity'])


# In[95]:


data.plot(x='year', y=['Average of Apparent Temperature (C)','Average of Humidity'], subplots=True , layout=(2,2))


# In[96]:


data.plot(x='year', y='Average of Apparent Temperature (C)')


# In[ ]:




