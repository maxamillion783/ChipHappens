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

        fsize = 18
        box_h = 36
        # self.orientation = 'vertical'
        self.rows = 6
        self.cols = 2
        self.size_hint_max_x = 600
        self.size_hint_max_y = 600

        self.jtext = TextInput(hint_text="Job ID", multiline=False, font_size=fsize, size_hint=(0.2,None), height=box_h)
        self.sjtext = TextInput(hint_text="Sub Job ID", multiline=False, font_size=fsize, size_hint=(0.2,None), height=box_h)
        self.btext = TextInput(hint_text="Batch ID", multiline=False, font_size=fsize,  size_hint=(0.2,None), height=box_h)
        self.otext = TextInput(hint_text="Operator ID", multiline=False, font_size=fsize, size_hint=(0.2,None), height=box_h)


        self.add_widget(Label(text="Job ID: ", font_size=fsize, size_hint=(0.2,None), height=box_h))
        self.add_widget(self.jtext)
        self.add_widget(Label(text="Sub Job ID: ", font_size=fsize, size_hint=(0.2,None), height=box_h))
        self.add_widget(self.sjtext)
        self.add_widget(Label(text="Batch ID: ", font_size=fsize, size_hint=(0.2,None), height=box_h))
        self.add_widget(self.btext)
        self.add_widget(Label(text="Operator ID: ", font_size=fsize, size_hint=(0.2,None), height=box_h))
        self.add_widget(self.otext)

        self.add_widget(Label(text='Serial Number: ', font_size=fsize, size_hint=(0.2,None), height=box_h))
        self.add_widget(Label(text="002", font_size=fsize, size_hint=(0.2,None), height=box_h))
        self.add_widget(Label(text='Version: ', font_size=fsize, size_hint=(0.2,None), height=box_h))
        self.add_widget(Label(text="V1", font_size=fsize, size_hint=(0.2,None), height=box_h))



if __name__ == '__main__':
    a = JobInfoPanel()
    a.run()