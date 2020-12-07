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


