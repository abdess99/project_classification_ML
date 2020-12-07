def create_datasets(db, label_class):
    data = data_process(db)
    y= np.array(data[[label_class]])
    X=data.drop(columns=[label_class])
    if len(data.columns) - 1 > 4:
       X_n = StandardScaler().fit_transform(X[1:-1])
       X_f = np.array(doPcaOnNormalizedData(X_n))
    else:
       X_f = np.array(X[1:-1])

return X_f, y