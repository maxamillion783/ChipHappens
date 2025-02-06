from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import datetime

import openpyxl

class JobInfoPanel(App):
    def build(self):
        return MainLayout()

class MainLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation = 'vertical'
        self.rows = 6
        self.cols = 2
        self.size_hint_max_x = 600
        self.size_hint_max_y = 600


        self.add_widget(Label(text="Job ID", font_size=24))
        self.add_widget(Label(text="Sub Job ID", font_size=24))
        self.add_widget(Label(text="Batch ID", font_size=24))
        self.add_widget(Label(text="Operator ID", font_size=24))
        self.add_widget(Label(text="002", font_size=24))
        self.add_widget(Label(text="V1", font_size=24))

if __name__ == '__main__':
    a = JobInfoPanel()
    a.run()