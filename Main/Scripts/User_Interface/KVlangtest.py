import sys
import datetime

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.properties import ObjectProperty


class JobInfoPanel(BoxLayout):
    job_info = {'jid': None, 'sjid': None, 'bid': None, 'oid': None}
    def update_last_operator(self):
        with open('last_operator_info.txt', 'w') as f: 
            f.write(f'Job Id: {self.ids.jid.text}\n')
            self.job_info['jid'] = self.ids.jid.text
            f.write(f'Sub Job Id: {self.ids.sjid.text}\n')
            self.job_info['sjid'] = self.ids.sjid.text
            f.write(f'Batch Id: {self.ids.bid.text}\n')
            self.job_info['bid'] = self.ids.bid.text
            f.write(f'Operator Id: {self.ids.oid.text}\n')
            self.job_info['oid'] = self.ids.oid.text
    
    def get_job_info(self):
        return self.job_info
    

class CountPanel(BoxLayout):
    # pass
    def update_data(self, cnt, cnf):
        self.ids.cnt.text = str(cnt)
        self.ids.cnf.text = str(cnf)
        self.ids.tim.text = datetime.now().strftime('%m%d%Y %H:%M:%S')

class TotalPanel(BoxLayout):
    past = []
    def update_total(self, cnt, cnf, time):
        
        self.ids.p_scroll.add_widget(Label(text=str(cnt),font_size=18,size_hint=(0.2,None),height=36 ))
        self.ids.p_scroll.add_widget(Label(text=str(cnf),font_size=18,size_hint=(0.2,None),height=36 ))
        self.ids.p_scroll.add_widget(Label(text=time,font_size=18,size_hint=(0.2,None),height=36 ))

class CustomTextInput(TextInput):
    """A custom TextInput that updates the active text input in the App when focused."""
    def on_focus(self, instance, value):
        if value:  # When focused
            App.get_running_app().active_text_input = self  # Store reference in the App

class KeyboardPanel(BoxLayout):
    def enter_number(self, number):
        """Insert the number into the currently selected text input."""
        active_text_input = App.get_running_app().active_text_input  # Get active input
        if active_text_input:
            active_text_input.text += str(number)
            active_text_input.focus = True  # Restore focus

    def backspace(self):
        """Remove the last character from the currently selected text input."""
        active_text_input = App.get_running_app().active_text_input  # Get active input
        if active_text_input and active_text_input.text:
            active_text_input.text = active_text_input.text[:-1]
            active_text_input.focus = True  # Restore focus

class MyApp(App):
    init = True
    waitHome = False

    jinfop = None
    cpanel = None
    tpanel = None
    active_text_input = ObjectProperty(None)

    running = False
    def build(self):
        Clock.schedule_interval(self.check, 1)
        return Builder.load_file('load.kv')
        # return Builder.load_string(KV)
    
    def check(self, b):
        if self.init:
            for child in self.root.children:
                if isinstance(child, JobInfoPanel):
                    self.jinfop = child
                elif isinstance(child, CountPanel):
                    self.cpanel = child
                elif isinstance(child, TotalPanel):
                    self.tpanel = child
            self.init = False

            self.waitHome = True
        
        if self.waitHome:

            #check if finished

            self.waitHome = False
        if self.running:
            print("Hello")

if __name__ == '__main__':
    MyApp().run()
