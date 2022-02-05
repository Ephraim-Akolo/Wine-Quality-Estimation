from tkinter import Label
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class WineQualityApp(MDApp):
    def build(self):
        return MDLabel(text="Hello World!", halign="center")


WineQualityApp().run()