import pandas as pd

def load_data(file : str) -> pd.DataFrame:   #Baptiste
  """
  Load the dataset
  """
  na_val = ["n/a", "na", "?", "NaN"]
  df = pd.read_csv(file, na_values = na_val)
  return df

def replace_na_values(df : pd.DataFrame) -> pd.DataFrame: #Baptiste
  """
  Return the data with the na values filled by the mean of the column
  """
  n = len(df.columns)
  
  for i in range(n):

    index = 0
    
    while type(df[df.columns[i]][index]) == float:
        print("While",type(df[df.columns[i]][index]))
        index+=1

    if type(df[df.columns[i]][index])!= str:# and df[df.columns[i]].dtype != object:
        df[df.columns[i]].fillna(df[df.columns[i]].mean())
        print("If",df[df.columns[i]].dtype)
    
        
    else:
      df[df.columns[i]].fillna(df[df.columns[i]].mode()[0])
      print("Else",df[df.columns[i]].dtype, type(df[df.columns[i]][1]) )
  df = df.applymap(lambda x: x.replace("\t", "") if type(x) == str else x)
  df = df.applymap(lambda x: x.replace(" ", "") if type(x) == str else x)
 
  return df

def categoric_to_one_hot(df: pd.DataFrame) -> pd.DataFrame: #Baptiste
  """
  Transform categorical data to one hot encoded vectors
  """
  n = len(df.columns)
  cols = [] #Categorical columns we will drop at the end
  for i in range(n):
    #print(df[df.columns[i]].dtype)
    if df[df.columns[i]].dtype == str or df[df.columns[i]].dtype == object:
      cols.append(i)
      df[df.columns[i]] = pd.Categorical(df[df.columns[i]])
      #One hot encoded version of the categorical column#
      new_cols = pd.get_dummies(df[df.columns[i]], prefix = list(df.columns)[i] )
      df = pd.concat([df, new_cols] , axis=1, sort=False)
  df.drop(df.columns[cols], axis=1, inplace=True)
  print(cols)
  return df

def preprocess_data(file : str) -> pd.DataFrame:
  df = load_data(file) 
  df = replace_na_values(df)
  df = categoric_to_one_hot(df)
  return df
