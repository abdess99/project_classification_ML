from sklearn import metrics
from sklearn import tree
from data import generate_datasets

def create_tree(db, criterion, splitter):  #Abdessamad
   X, y = create_datasets(db)
   max = 0
   NUM_SPLITS = 5
   clf = tree.DecisionTreeClassifier(criterion=criterion, splitter=splitter)
   # split the data
   kf = KFold(n_splits=NUM_SPLITS, shuffle=True)
   # Train, test and compute the metrics on each split
   for train_index, test_index in kf.split(X):
      X_train = X[train_index]
      y_train = y[train_index]
      X_test = X[test_index]
      y_test = y[test_index]
      clf.fit(X_train, y_train)
      # Predictions on the test set
      predictions = clf.predict(X_test)
      if max < metrics.accuracy_score(test_y, predictions):
         max = metrics.accuracy_score(test_y, predictions)
         X_train_f = X[train_index]
         y_train_f = y[train_index]
         X_test_f = X[test_index]
         y_test_f = y[test_index]
          
   predictions = clf.predict(X_test_f)
   clf.fit(train_X_f, train_y_f)
   recall = metrics.recall_score(test_y_f, predictions)
   precision=metrics.precision_score(test_y_f, predictions)
   
   return clf, precision, recall
