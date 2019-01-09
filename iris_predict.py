#!/usr/bin/env python

# IRIS PREDICTION

from sklearn.datasets import load_iris
from sklearn import tree

#load dataset of iris
iris=load_iris()

#dir(iris) give all fields in iris

#iris.feature_names gives all sepal w/l petal w/l


#iris.target_names gives 3 iris names--- 0-setosa 1-versicolor 2-virginica

#iris.target gives output for all data means which data denots which iris species

#here iris.data are features and iris.target are label 0-setosa 1-versicolor 2-virginica
#iris.data.shape gives total no. of data
iris.data

# train thiis data
features=iris.data
label=iris.target

#calling decision tree
dsc_algo=tree.DecisionTreeClassifier()
#training algo
trained_algo=dsc_algo.fit(features,label)

#predict output
prediction=trained_algo.predict([[6.5,3.2,5.8,2]])
print(prediction)






