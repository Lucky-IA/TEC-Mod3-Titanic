import pandas as pd
import numpy as np
from pathlib import Path

class DataLoad():
    def __init__(self):
        self.drop_cols = ["name", "sibsp", "parch", "ticket", "cabin", "boat", "body", "home.dest"]

    def data_load(self):
        path = str(Path(__file__).parent).replace("/src/load","")
        data_dir = f"{path}/data/raw/phpMYEkMl.csv"
        self.df = pd.read_csv(data_dir)

        self.df = self.df.replace("?", np.nan)
        self.df = self.df.drop(columns=self.drop_cols)

        return self.df

if __name__ == "__main__":
    try:
       pass
        
    except Exception as e:
        print("Something went wrong...")