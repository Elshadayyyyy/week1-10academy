import pandas as pd

def load_data(path: str) -> pd.DataFrame:
  
    if path.endswith(".csv"):
        return pd.read_csv(path)
    elif path.endswith(".parquet"):
        return pd.read_parquet(path)
    else:
        raise ValueError("Unsupported file type. Use CSV or Parquet.")
