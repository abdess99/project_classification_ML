import numpy as np

def apply_pca(df: pd.DataFrame) -> pd.DataFrame: #Arthur
  """
  Reduce dimensions thanks to pca
  """
  pca = decomposition.PCA()
  df=pca.fit_transform(df)
  # Selecting only the best components
  max_variance = np.max(pca.explained_variance_ratio_)

  pc_number = len([v for v in pca.explained_variance_ratio_ if v >= max_variance/10000])
  df = df[:, :pc_number]
  return pd.DataFrame(df)
  


def create_datasets(db):    #Arthur
    data=preprocess_data(db)
    y= data[data.columns[-1]]
    X=data.drop(data.columns[-1],axis=1)
    X=apply_pca(X)
    X=pd.DataFrame(X)
    return X, y
