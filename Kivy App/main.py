from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.textfield import MDTextField
from plyer import filechooser
import pandas as pd
import numpy as np
from models import Model

class FeaturesInput(MDTextField):
    '''
    The widget that takes features as input.
    '''


class Manager(ScreenManager):
    '''
    Apps root widget class
    '''
    _wine_features = np.array(('fixed acidity',
                'volatile acidity',
                'citric acid',
                'residual sugar',
                'chlorides',
                'free sulfur dioxide',
                'total sulfur dioxide',
                'density',
                'pH',
                'sulphates',
                'alcohol'))

    _current_feature = 0
    _features = np.array([None for i in range(11)])
    def load_NN(self):
        '''
        load the trained neural nework model.
        '''
    
    def load_SM(self):
        '''
        load the statistical based model.
        '''
        self._model = Model()
    
    def _next_feature(self, label, textinput):
        '''
        goes to the next feature in the list.
        '''
        if textinput.required is False and self._current_feature < 11:
            self._features[self._current_feature] = np.float32(textinput.text)
            if self._current_feature < 10:
                label.text = label.text.replace(f"{self._wine_features[self._current_feature]}", self._wine_features[self._current_feature+1])
            self._current_feature += 1
            textinput.text = ""
            textinput.hint_text = textinput.hint_text.replace(f'{12-self._current_feature}', f'{12-self._current_feature-1}')
            if self._current_feature == 11:
                self._predict_features()
            print(self._features)

    def _prev_feature(self, label, textinput):
        '''
        goes to the previous feature in the list.
        '''
        if self._current_feature > 0:
            self._current_feature -= 1
            label.text = label.text.replace(f"{self._wine_features[self._current_feature+1]}", self._wine_features[self._current_feature])
            textinput.text = ""
            textinput.hint_text = textinput.hint_text.replace(f'{12-self._current_feature-2}', f'{12-self._current_feature-1}')

    def _predict_features(self):
        '''
        estimates the value of the wine with the given features.
        '''
        self.transition.direction = "left"
        self.current = "screen3"
        df = self.createdFrame(self._wine_features, self._features)
        self._predictions = self._model.predict(df, csv=False)
    
    def _predict_csv_features(self, dataframe):
        '''
        estimates the value of the wine with features extracted from a csv file.
        '''
        self._predictions = self._model.predict(dataframe)
        print(self._predictions)
    
    def _file_chooser(self):
        '''
        opens the platform filechooser to select csv file for prediction.
        '''
        try:
            self._csv_file = filechooser.open_file(title="choose csv file", multiple=False, preview=True, filters=["*.csv"])[0]
            if len(self._csv_file) == 0:
                return
            self.transition.direction = "left"
            self.current = "screen3"
            dataframe = pd.read_csv(self._csv_file)
            if np.sum(self._wine_features == dataframe.columns) == len(self._wine_features):
                self._predict_csv_features(dataframe)
            else:
                self._incorrect_csv()
        except IndexError as e:
            print("Caught: ", e)
        except:
            print("Akolo Unknown Error from filechooser!")
    
    def _incorrect_csv(self):
        '''
        Triggered when an incorrect csv is passed.
        '''

    def createdFrame(self, col, val):
        return pd.DataFrame([val], columns=col)


class WineQualityApp(MDApp):
    '''
    Apps window instance class.
    '''


WineQualityApp().run()