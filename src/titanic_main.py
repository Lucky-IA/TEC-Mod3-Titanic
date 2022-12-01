from classifier import titanic_classifier

model = titanic_classifier.TitanicClassifier()

dic = {"pclass": 1, "sex": "female", "age": 29, "fare": 211.33, "embarked": "S"}
pred = model.PredictModel(dic)

print(pred)

