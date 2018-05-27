import pandas as pd
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.metrics import precision_recall_fscore_support, accuracy_score

def TrainAndTestModel(model, TrainX, TrainY, TestX, TestY):
    model.fit(TrainX, TrainY)
    expected = TestY
    predicted = model.predict(TestX)

    print("---------------------")
    print(metrics.classification_report(expected, predicted))
    print(metrics.confusion_matrix(expected, predicted))
    print("Accuracy: "+str(accuracy_score(expected, predicted)))
    print("---------------------\n")


def FindCrossValidation(model, X, Y, foldCount):
    kf = KFold(n_splits=foldCount)
    i=1
    averagePrecision = 0
    averageRecall = 0
    averageF1 = 0
    averageAccuracy = 0
    for train_index, test_index in kf.split(X):
        X_trainFold, X_testFold = X[train_index], X[test_index]
        y_trainFold, y_testFold = Y[train_index], Y[test_index]
        model.fit(X_trainFold, y_trainFold)
        expected = y_testFold
        predicted = model.predict(X_testFold)
        precision, recall, f1, support = precision_recall_fscore_support(expected, predicted, average="weighted")
        accuracy = accuracy_score(expected, predicted)
        averagePrecision += precision
        averageRecall += recall
        averageF1 += f1
        averageAccuracy += accuracy
        i += 1

    return averageAccuracy/foldCount, averagePrecision/foldCount, averageRecall/foldCount, averageF1/foldCount


featureData = pd.read_csv('FeatureOutput.csv', engine='python')
X = featureData.get_values()[:,1:16]
Y = featureData.get_values()[:,16]
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20)

# Train and test Gaussian Naive Bayes model
model = GaussianNB()
print("Gaussian Naive Bayes Model (test-on-training)")
TrainAndTestModel(model, X, Y, X, Y)
print("Gaussian Naive Bayes Model (percentage split)")
TrainAndTestModel(model, X_train, y_train, X_test, y_test)
print("Gaussian Naive Bayes Model (cross validation) [Accuracy, Precision, Recall, F1-Score]:")
print(FindCrossValidation(model, X, Y, 10))

# Train and test Linear Regression model
model = LogisticRegression()
print("Linear Regression Model (test-on-training)")
TrainAndTestModel(model, X, Y, X, Y)
print("Linear Regression Model (percentage split)")
TrainAndTestModel(model, X_train, y_train, X_test, y_test)
print("Linear Regression Model (cross validation) [Accuracy, Precision, Recall, F1-Score]:")
print(FindCrossValidation(model, X, Y, 10))

# Train and test SVM model
model = SVC(C=1.0, kernel="linear")
print("SVM Model(test-on-training)")
TrainAndTestModel(model, X, Y, X, Y)
print("SVM Model (percentage split)")
TrainAndTestModel(model, X_train, y_train, X_test, y_test)
print("SVM Model (cross validation) [Accuracy, Precision, Recall, F1-Score]:")
print(FindCrossValidation(model, X, Y, 10))

# Train and test k-Nearest Neighbor model
model = KNeighborsClassifier()
print("k-Nearest Neighbor Model (test-on-training)")
TrainAndTestModel(model, X, Y, X, Y)
print("k-Nearest Neighbor Model (percentage split)")
TrainAndTestModel(model, X_train, y_train, X_test, y_test)
print("k-Nearest Neighbor Model (cross validation) [Accuracy, Precision, Recall, F1-Score]:")
print(FindCrossValidation(model, X, Y, 10))
