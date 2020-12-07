import pandas as pd

def load_data(file : string) -> pd.DataFrame:   #Baptiste
  """
  Load the dataset
  """
  na_val = ["n/a", "na", "?"]
  df = pd.read_csv(file, na_values = na_val)
  return df

def replace_na_values(df : pd.DataFrame) -> pd.DataFrame: #Baptiste
  """
  Return the data with the na values filled by the mean of the column
  """
  n = len(df.columns)
  for i in range(n):
    if df.columns[i].dtype != "string":
      df[df.columns[i]].fillna(df[df.columns[i]].mean())
    else:
      df[df.columns[i]].fillna(df[df.columns[i]].mode()[0])
  return df


def categoric_to_one_hot(df: pd.DataFrame) -> pd.DataFrame: #Baptiste
  """
  Transform categorical data to one hot encoded vectors
  """
  n = len(df.columns)
  cols = [] #Categorical columns we will drop at the end
  for i in range(n):
    if df.columns[i].dtype == "string":
      cols.append(i)
      df[df.columns[i]] = pd.Categorical(df[df.columns[i]])
      #One hot encoded version of the categorical column#
      new_cols = pd.get_dummies(df[df.columns[i]], prefix = list(data.columns)[i] )
      df = pd.concat([df, new_cols] , axis=1, sort=False)
  df.drop(cols)
  return df

def preprocess_data(file : string) -> pd.DataFrame:
  df = load_data(file) 
  df = replace_na_values(df)
  df = categoric_to_one_hot(df)
  return df

                      
  
