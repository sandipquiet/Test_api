from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
# from sklearn.model_selection import train_test_split
# from sklearn.model_selection import cross_val_score
# from sklearn.model_selection import StratifiedKFold
# from sklearn.metrics import classification_report
# from sklearn.metrics import confusion_matrix
# from sklearn.metrics import accuracy_score
# from sklearn.linear_model import LogisticRegression
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
# from sklearn.naive_bayes import GaussianNB
# from sklearn.svm import SVC


# url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
# names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
# dataset = read_csv(url, names=names)

# print(dataset.shape)
# print(dataset.head(20))
# print(dataset.describe())
# print(dataset.groupby('class').size())



# dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
# pyplot.show()

# # histograms
# dataset.hist()
# pyplot.show()
# # scatter plot matrix
# scatter_matrix(dataset)
# pyplot.show()

from sklearn.datasets import load_iris
iris = load_iris()
type(iris)
print(iris.feature_names)
print(iris.target_names)
X=iris.data
Y=iris.target

import pandas as pd

X_dframe=pd.DataFrame(data=X,columns=iris.feature_names)

print(X_dframe.describe())

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20, random_state=1, stratify=Y)

from sklearn.ensemble import RandomForestClassifier
clf_rf = RandomForestClassifier(random_state = 1, n_estimators = 10, n_jobs = -1)
estimator_rf = clf_rf
estimator_rf.fit(X=X_train, y=y_train)
print(estimator_rf.score(X_test,y_test))

from sklearn.model_selection import cross_val_score
estimator_cv = clf_rf
scores = cross_val_score(estimator_cv, X, Y, cv = 5, scoring = 'accuracy')
print(scores.mean())

from joblib import dump, load
dump(estimator_rf, 'IRISRandomForestClassifier.joblib')

loaded_classifier = load('IRISRandomForestClassifier.joblib')
loaded_classifier.score(X_test,y_test)
print(loaded_classifier.score(X_test,y_test))
print(loaded_classifier)