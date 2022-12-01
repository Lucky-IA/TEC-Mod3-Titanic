import sys
from pathlib import Path
import pandas as pd

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))
sys.path.append("..")

from train import train_model

class TitanicClassifier():
    def __init__(self):
        pass

    def PredictModel(self, dic):
        train = train_model.TrainModel()
        model = train.TitanicPipeline()

        value = pd.DataFrame(data=dic, index=[0])
        class_pred = model.predict(value)

        return class_pred

if __name__ == "__main__":
    try:
        model = TitanicClassifier()

        dic = {"pclass": 1, "sex": "female", "age": 29, "fare": 211.33, "embarked": "S"}
        pred = model.PredictModel(dic)

        print(pred[0])
        
    except Exception as err:
        print("Something went wrong...")
