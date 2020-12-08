def create_datasets(db):
    y= data.columns[-1]
    X=data.drop(data.columns[-1],axis=1)
    
    return X, y
