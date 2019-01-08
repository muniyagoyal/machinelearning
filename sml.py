from sklearn import tree
#this data is about apple and orange
#smooth=1 red=100 pred=80
#bumpy=0 orange=150 porange=130
features=[[1,100],[1,80],[0,150],[0,130]]
label=["Apple","Apple","Orange","Orange"]
#calling decision tree classifier and algo is variable of decision tree classifier
algo=tree.DecisionTreeClassifier()
#train this data fit() always took input in float
trained_algo=algo.fit(features,label)
#time for giving input
prediction=trained_algo.predict([[1,100]])
print(prediction)
