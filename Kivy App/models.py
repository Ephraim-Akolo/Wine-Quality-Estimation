import pandas as pd
import pickle
class Model:
    def __init__(self, directory="./Kivy App/models/"):
        self.iscsv = True
        try:
            with open(directory + "model1b", "rb") as f:
                self._model1 = pickle.load(f)
            with open(directory + "model2c", "rb") as f:
                self._model2 = pickle.load(f)
            with open(directory + "model3b", "rb") as f:
                self._model3 = pickle.load(f)
            print("Model Loaded successfully on first attempt!")
        except (FileNotFoundError, FileExistsError) as e:
            print(f"File failed to open: {e}... attempting again...")
            try:
                with open(directory + "model1b", "rb") as f:
                    self._model1 = pickle.load(f)
                with open(directory + "model2c", "rb") as f:
                    self._model2 = pickle.load(f)
                with open(directory + "model3b", "rb") as f:
                    self._model3 = pickle.load(f)
                print("Model Loaded successfully on second attempt!")
            except (FileNotFoundError, FileExistsError) as f:
                print(f"File failed to open: {f}...")
    
    def predict(self, X:pd.DataFrame, csv=True):
        X = self.preprocess(X)
        preds = self._model1.predict(X)
        X["common"] = preds
        X1 = X[X.common == True]
        X2 = X[X.common == False]
        X1 = X1.drop("common", axis=1)
        X2 = X2.drop("common", axis=1)
        if csv:
            preds1 = self._model2.predict(X1)
            preds2 = self._model3.predict(X2)
            X1['preds'] = preds1
            X2['preds'] = preds2
            X = pd.concat([X1, X2])
            X = X.sort_index()
            return X["preds"]
        elif preds[0]:
            return self._model2.predict(X1)
        else:
            return self._model3.predict(X2)
        

    def preprocess(self, dataframe:pd.DataFrame):
        dataframe["densit_alcohol"] = dataframe["density"]/dataframe['alcohol']
        dataframe.drop("sulphates",axis=1, inplace=True)
        dataframe.drop("density",axis=1, inplace=True)
        return dataframe.drop("chlorides",axis=1)
