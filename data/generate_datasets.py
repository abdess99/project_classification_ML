def create_datasets(db):
    data=preprocess_data(db)
    y= data.columns[-1]
    X=data.drop(data.columns[-1],axis=1)
    
    return X, y
