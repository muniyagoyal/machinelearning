#!/usr/bin/env python
# coding: utf-8

# In[36]:


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score


# In[37]:


iris=load_iris()


# In[38]:


#  now  splitting  training and testing dataset testing data 10% 
split_data=train_test_split(iris.data,iris.target,test_size=0.1)


# In[39]:



train_data,test_data,train_target,test_target=split_data


# In[40]:


features=train_data
label=train_target


# In[41]:


#calling classifier
dsc_clf=tree.DecisionTreeClassifier()
trained=dsc_clf.fit(train_data,train_target)
#predicting output
output=trained.predict(test_data)


# In[42]:


#to check accuracy
acc=accuracy_score(test_target,output) #test_target splitted output
print("Algo accuracy is:",acc)


# In[ ]:




