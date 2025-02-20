import sys

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

KV = '''
<JobInfoPanel>:
    GridLayout:
        cols: 2
        rows: 6
        height: 500
        width: 500
        padding: 10
        spacing: 2
        Label:
            text: "Job ID"
            color: (0,0,0,1)
            font_size: 18
            size_hint: (0.2, None)
            height: 36
        TextInput:
            hint_text: ""
            color: (0,0,0,1)
            font_size: 18
            size_hint: (0.2, None)
            height: 36
        Label:
            text: "SubJob ID"
            color: (0,0,0,1)
            font_size: 18
            size_hint: (0.2, None)
            height: 36
        TextInput:
            hint_text: ""
            color: (0,0,0,1)
            font_size: 18
            size_hint: (0.2, None)
            height: 36
        Label:
            text: "Batch ID"
            color: (0,0,0,1)
            font_size: 18
            size_hint: (0.2, None)
            height: 36
        TextInput:
            hint_text: ""
            color: (0,0,0,1)
            font_size: 18
            size_hint: (0.2, None)
            height: 36
        Label:
            text: "Operator ID"
            color: (0,0,0,1)
            font_size: 18
            size_hint: (0.2, None)
            height: 36
        TextInput:
            hint_text: ""
            color: (0,0,0,1)
            font_size: 18
            size_hint: (0.2, None)
            height: 36
        Label:
            text: "Counter Serial Number"
            color: (0,0,0,1)
            font_size: 18
            size_hint: (0.2, None)
            height: 36
        Label:
            text: "002"
            color: (0,0,0,1)
            font_size: 18
            size_hint: (0.2, None)
            height: 36
        Label:
            text: "Version"
            color: (0,0,0,1)
            font_size: 18
            size_hint: (0.2, None)
            height: 36
        Label:
            text: "V01"
            color: (0,0,0,1)
            font_size: 18
            size_hint: (0.2, None)
            height: 36

<CountPanel>:
    GridLayout:
        cols: 2
        rows: 4
        height: 500
        width: 500
        padding: 10
        spacing: 2
        Label:
            text: "Current Count"
            color: (0,0,0,1)
            font_size: 18
            size_hint: (0.2, None)
            height: 36
        TextInput:
            hint_text: ""
            color: (0,0,0,1)
            font_size: 18
            size_hint: (0.2, None)
            height: 36
            readonly: True
            
        Label:
            text: "Time Stamp"
            color: (0,0,0,1)
            font_size: 18
            size_hint: (0.2, None)
            height: 36
        TextInput:
            hint_text: ""
            color: (0,0,0,1)
            font_size: 18
            size_hint: (0.2, None)
            height: 36
            readonly: True
        Label:
            text: "Confidence Interval"
            color: (0,0,0,1)
            font_size: 18
            size_hint: (0.2, None)
            height: 36
        TextInput:
            hint_text: ""
            color: (0,0,0,1)
            font_size: 18
            size_hint: (0.2, None)
            height: 36
            readonly: True
        Button:
            text: "Run"
            background_normal: ''
            background_color: (1, 0.1, 0.2, 1)
            # color: (0,1,0,1)
            size_hint: (0.2, None)
            height: 50
            canvas.before:
                Color: 
                    rgba: (0,0,0, 1)
                Line:
                    width: 2
                    rectangle: self.x, self.y, self.width, self.height


<TotalPanel>:
    BoxLayout: 
        orientation: 'vertical'
        spacing: 1
        padding: 10
        GridLayout:
            cols: 2
            rows: 1
            padding: 10
            spacing: 2
            Label:
                text: "Running Total"
                color: (0,0,0,1)
                font_size: 18
                size_hint: (0.2, None)
                height: 36
            TextInput:
                hint_text: ""
                color: (0,0,0,1)
                font_size: 18
                size_hint: (0.2, None)
                height: 36
                readonly: True
        GridLayout:
            cols: 1
            padding: 10
            spacing: 2
            ScrollView:
                do_scroll_x: False
                do_scroll_y: True
                Label:
                    text: 
                        "Scroll\\n" * 100
                    color: (0,0,0,1)
                    font_size: 18
                    size_hint: (0.2, None)
                    height: 36


BoxLayout:
    orientation: 'vertical'
    spacing: 1
    padding: 10
    canvas.before:
        Color:
            rgb: (1,1,1,1)
        Rectangle:
            pos: self.pos
            size: self.size

    JobInfoPanel:
        canvas.before:
            Color:
                rgb: (1,1,1,1)
            Rectangle:
                pos: self.pos
                size: self.size
            Color:
                rgb: (0,0,0)
            Line:
                width:2
                rectangle: (self.x, self.y, self.width, self.height)

    CountPanel:
        canvas.before:
            Color:
                rgb: (1,1,1,1)
            Rectangle:
                pos: self.pos
                size: self.size
            Color:
                rgb: (0,0,0)
            Line:
                width:2
                rectangle: (self.x, self.y, self.width, self.height)

    TotalPanel:
        canvas.before:
            Color:
                rgb: (1,1,1,1)
            Rectangle:
                pos: self.pos
                size: self.size
'''

class JobInfoPanel(BoxLayout):
    pass

class CountPanel(BoxLayout):
    pass

class TotalPanel(BoxLayout):
    pass

class MyApp(App):
    def build(self):
        return Builder.load_string(KV)

if __name__ == '__main__':
    MyApp().run()
