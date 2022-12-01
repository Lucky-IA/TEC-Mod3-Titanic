import sys
from pathlib import Path

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression

path_root_1 = Path(__file__).parents[1]
sys.path.append(str(path_root_1))
sys.path.append("..")

from load import data_load
from transform import transform_data as ct

class TrainModel():
    def __init__(self):
        self.target = "survived"
        self.numerical_nan = ["age", "fare"]
        self.cetegorical_nan = ["embarked"]
        self.numerical_new = ["age", "sex", "embarked"]

        self.seed_model = 44
        self.seed_split = 43
        self.test_size = 0.20

    def DataRetrieval(self):
        dl = data_load.DataLoad()
        self.df = dl.data_load()

    def TitanicPipeline(self):
        self.DataRetrieval()

        self.pipeline = Pipeline([
                                ("num_sex", ct.NumericalSex()),
                                ("num_float", ct.NumericalFloat(variables=self.numerical_nan)),
                                ("num_imputer", ct.NumericalImputer(variables=self.numerical_nan)),
                                ("cat_imputer", ct.CategoricalImputer(variables=self.cetegorical_nan)),
                                ("num_emb", ct.NumericalEmbarked()),
                                ("num_round", ct.NumericalRound(variables=self.numerical_nan)),
                                ("num_int", ct.NumericalInt(variables=self.numerical_new)),
                                ("scaling", MinMaxScaler()),
                                ("log_reg", LogisticRegression(class_weight="balanced", random_state=self.seed_model))
                                ])

        X = self.df.drop(self.target, axis=1)
        y = self.df[self.target]

        return self.pipeline.fit(X, y)

if __name__ == "__main__":
    try:
        train = TrainModel()
        model = train.TitanicPipeline
        
    except Exception as err:
        print("Something went wrong...")