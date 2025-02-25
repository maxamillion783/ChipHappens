import sys

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.clock import Clock

class JobInfoPanel(BoxLayout):
    pass

class CountPanel(BoxLayout):
    pass

class TotalPanel(BoxLayout):
    pass

class MyApp(App):

    running = False
    def build(self):
        Clock.schedule_interval(self.check, 1)
        return Builder.load_file('load.kv')
        # return Builder.load_string(KV)
    
    def check(self, b):
        if self.running:
            print("Hello")

if __name__ == '__main__':
    MyApp().run()
