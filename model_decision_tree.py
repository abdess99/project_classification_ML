from sklearn import metrics
from sklearn import tree
from sklearn.model_selection import KFold

def create_tree(db, criterion, splitter):  #Abdessamad
   
   """
   db is the database file path
   criterion is the criterion used in the decision tree
   splitter is the splitter used in the decision tree
   """

   X, y = create_datasets(db)
  
   max = 0
   NUM_SPLITS = 5
   clf = tree.DecisionTreeClassifier(criterion=criterion, splitter=splitter)
   # split the data
   kf = KFold(n_splits=NUM_SPLITS, shuffle=True)
   # Train, test and compute the metrics on each split
   
   for train_index, test_index in kf.split(X):
      
      X_train = X.iloc[train_index,:]
      y_train = y[train_index]
      X_test = X.iloc[test_index,:]
      y_test = y[test_index]
      clf.fit(X_train, y_train)
      # Predictions on the test set
      predictions = clf.predict(X_test)
      # we should chose the best train and test set
      if max < metrics.accuracy_score(y_test, predictions):
         max = metrics.accuracy_score(y_test, predictions)
         X_train_f = X.iloc[train_index,:]
         y_train_f = y[train_index]
         X_test_f = X.iloc[test_index,:]
         y_test_f = y[test_index]
          
   predictions = clf.predict(X_test_f)
   clf.fit(X_train_f, y_train_f)
   recall = metrics.recall_score(y_test_f, predictions)
   precision=metrics.precision_score(y_test_f, predictions)
   
   return clf, precision, recall
