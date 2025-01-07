#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
txt = "The rain in Spain"
x = re.findall("ai", txt) 
print(x)


# In[2]:


x = re.search("\AThe", txt)

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")


# In[3]:


x = re.findall("\d", txt)
print(x)


# In[4]:


x = re.findall("[irn]", txt)
print(x)


# In[5]:


x = re.split("\s",txt)
print(x)


# In[6]:


x = re.sub("\s", "9", txt)
print(x) 


# In[7]:


x = re.split("\s", txt, 1)
print(x) 


# In[8]:


x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start()) 


# In[9]:


x = re.findall("[^arn]", txt)

print(x)


# In[10]:


x = re.findall("[A-Z]", txt)

print(x)


# In[11]:


x = re.findall("[a-z]", txt)

print(x)


# In[ ]:




