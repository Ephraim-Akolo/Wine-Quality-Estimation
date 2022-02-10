from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.textfield import MDTextField
from plyer import filechooser
import pandas as pd
import numpy as np

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
    
    def _next_feature(self, label, textinput):
        '''
        goes to the next feature in the list.
        '''
        if textinput.required is False and self._current_feature < 11:
            self._features[self._current_feature] = float(textinput.text)
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
        self._features
    
    def _predict_csv_features(self, dataframe):
        '''
        estimates the value of the wine with features extracted from a csv file.
        '''
        _features = np.array([self._features])
        print(_features)
    
    def _file_chooser(self):
        '''
        opens the platform filechooser to select csv file for prediction.
        '''
        self.transition.direction = "left"
        self.current = "screen3"
        try:
            self._csv_file = filechooser.open_file(title="choose csv file", multiple=False, preview=True, filters=["*.csv"])[0]
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

        


class WineQualityApp(MDApp):
    '''
    Apps window instance class.
    '''


WineQualityApp().run()