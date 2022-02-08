from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import ScreenManager


class Manager(ScreenManager):
    '''
    Apps root widget class
    '''
    def load_NN(self):
        '''
        load the trained neural nework model.
        '''
    
    def load_SM(self):
        '''
        load the statistical based model.
        '''


class WineQualityApp(MDApp):
    '''
    Apps window instance class.
    '''


WineQualityApp().run()