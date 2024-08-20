#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = np.array([1,2,3,4,5]).reshape(-1,1)
y = np.array([50,55,60,70,80])

model = LinearRegression()
model.fit(x,y)

beta_0 =model.intercept_
beta_1 = model.coef_[0]

y_pred = model.predict(x)

plt.scatter(x,y,color = 'red')
plt.plot(x,y_pred,color = 'green')
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.show()


# In[ ]:




