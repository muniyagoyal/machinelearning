#!usr/bin/env python
import pandas as pd
import  seaborn  as  sb
from  sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from  sklearn.neighbors  import KNeighborsClassifier
import matplotlib.pyplot as plt

#  reading csv file and converting into data frames
df=pd.read_csv('diabetes.csv')
#df.head(5) this wil, display first 5 rows of dataset

#  creating  training and testing datasets 
diabetes_target=df['Outcome']  # df['outcome'] gives all output means complete labels of dataset

diabetes_data=df[df.columns[:-1]]   # df[df.colums[:-1]] gives all features of complete dataset 

#sb.countplot(df['Outcome']) countplot function of seaborn which count total of different outcome or other feature

#df.info()   to check all info about  data with null values

#df.hist(figsize=(14,14)) this will display histogram of all features

#df.groupby('Outcome').size()  group different values of outcome feature and size print total value

#spliting dataset with test size 10%
split_data_10=train_test_split(diabetes_data,diabetes_target,test_size=0.1)

train_data_10,test_data_10,train_target_10,test_target_10=split_data_10

#implementing decision tree classifier
dsc_algo=DecisionTreeClassifier()

trained_dsc_10=dsc_algo.fit(train_data_10,train_target_10)

output_dsc_10=trained_dsc_10.predict(test_data_10)

#to check accuracy score
acc_dsc_10=accuracy_score(test_target_10,output_dsc_10)
print("Accuracy score using Decision Tree Classifier with 10% splitted data:",acc_dsc_10)


#spliting dataset with test size 20%
split_data_20=train_test_split(diabetes_data,diabetes_target,test_size=0.2)

train_data_20,test_data_20,train_target_20,test_target_20=split_data_20

trained_dsc_20=dsc_algo.fit(train_data_20,train_target_20)

output_dsc_20=trained_dsc_20.predict(test_data_20)

#to check accuracy score
acc_dsc_20=accuracy_score(test_target_20,output_dsc_20)
print("Accuracy score using Decision Tree Classifier with 20% splitted data:",acc_dsc_20)

#implementing KNN with 10% splitted data
knn_clf=KNeighborsClassifier(n_neighbors=5)

trained_knn_10=knn_clf.fit(train_data_10,train_target_10)
print(test_data_10)
output_knn_10=trained_knn_10.predict(test_data_10)

#to check accuracy score
acc_knn_10=accuracy_score(test_target_10,output_knn_10)
print("Accuracy score using KNN with 10% splitted data:",acc_knn_10)

#implementing KNN with 20% splitted data
trained_knn_20=knn_clf.fit(train_data_20,train_target_20)

output_knn_20=trained_knn_20.predict(test_data_20)

#to check accuracy score
acc_knn_20=accuracy_score(test_target_20,output_knn_20)
print("Accuracy score using KNN with 20% splitted data:",acc_knn_20)


plt.bar(acc_dsc_10,output_dsc_10,label="Decision Tree Classifier")
#plt.bar(acc_knn_10,label="KNN Algorithm")
plt.show()
plt.legend()
plt.xlabel("Accuracy score")
plt.ylabel("Algorithm")




