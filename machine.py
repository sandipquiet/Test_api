import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from  sklearn.model_selection import  train_test_split
import joblib
from sklearn import  tree

music_data=pd.read_csv("D:\\Music.csv")
#print(df.shape)
#print(df.describe())
#df.values

X=music_data.drop(columns=["Music_Type"])
y=music_data["Music_Type"]
model=DecisionTreeClassifier()
model.fit(X,y)
tree.export_graphviz(model,out_file='music_recommender.dot',feature_names=['age','gender']
                     ,class_names=sorted(y.unique()),label='all',rounded=True,filled=True)
# p=model.predict([[17,0],[55,0]])
# print(p)
# joblib.dump(model,'music_recommender.joblib')
#model=joblib.load('music_recommender.joblib')
#p=model.predict([[17,0],[55,0]])
#print(p)

# X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
# model1=DecisionTreeClassifier()
# model1.fit(X_train,y_train)
# p1=model1.predict(X_test)
# a=accuracy_score(y_test,p1)
# print(a)



