import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from classifier import titanic_classifier

class Titanic(BaseModel):
    pclass: int
    sex: object
    age: int
    fare: float
    embarked: object

app = FastAPI()
model = titanic_classifier.TitanicClassifier()

@app.get("/")
def home():
    return "Titanic classifier is ready..."

@app.post("/predict")
def predict_titanic(passenger:Titanic):
    dic = passenger.dict()
    pred = model.PredictModel(dic)

    return {"prediction": str(pred[0])}
    # {"pclass": 1, "sex": "female", "age": 29, "fare": 211.33, "embarked": "S"} # 1

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port="8000")
