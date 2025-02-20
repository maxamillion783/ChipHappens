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
        spacing: 0
        padding: 10
        GridLayout:
            cols: 3
            rows: 1
            padding: 10
            spacing: 2
            size_hint_y: 0.5
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
            BoxLayout:
                padding: 10
                spacing: 0
                size_hint_x: 0.1
                Button:
                    text: "Print"
                    background_normal: ''
                    background_color: (1, 0.1, 0.2, 1)
                    canvas.before:
                        Color: 
                            rgba: (0,0,0, 1)
                        Line:
                            width: 2
                            rectangle: self.x, self.y, self.width, self.height
        GridLayout:
            cols: 3
            # padding: 10
            spacing: 2
            size_hint_y: 0.4
            size_hint_x: 0.5

            Label:
                text: "Time"
                color: (0,0,0,1)
                font_size: 18
                size_hint: (0.2, None)
                height: 36
            Label:
                text: "Count"
                color: (0,0,0,1)
                font_size: 18
                size_hint: (0.2, None)
                height: 36
            Label:
                text: "Metrics"
                color: (0,0,0,1)
                font_size: 18
                size_hint: (0.2, None)
                height: 36
        GridLayout:
            cols: 1
            spacing: 2
            size_hint_x: 0.5
            ScrollView:
                do_scroll_x: False
                do_scroll_y: True
                size_hint_y: None
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                # size_y: 600
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1
                    Line:
                        width:2
                        rectangle: (self.x, self.y, self.width, self.height)
                GridLayout:
                    cols: 3
                    size_hint_y: None
                    height: self.minimum_height
                    # padding: 10
                    spacing: 2
                    Label:
                        text: 
                            "Scroll"
                        color: (0,0,0,1)
                        font_size: 18
                        size_hint: (0.2, None)
                        height: 36
                    Label:
                        text: 
                            "Scroll"
                        color: (0,0,0,1)
                        font_size: 18
                        size_hint: (0.2, None)
                        height: 36
                    Label:
                        text: 
                            "Scroll"
                        color: (0,0,0,1)
                        font_size: 18
                        size_hint: (0.2, None)
                        height: 36
                    Label:
                        text: 
                            "Scroll"
                        color: (0,0,0,1)
                        font_size: 18
                        size_hint: (0.2, None)
                        height: 36
                    Label:
                        text: 
                            "Scroll"
                        color: (0,0,0,1)
                        font_size: 18
                        size_hint: (0.2, None)
                        height: 36
                    Label:
                        text: 
                            "Scroll"
                        color: (0,0,0,1)
                        font_size: 18
                        size_hint: (0.2, None)
                        height: 36
                    Label:
                        text: 
                            "Scroll"
                        color: (0,0,0,1)
                        font_size: 18
                        size_hint: (0.2, None)
                        height: 36
                    Label:
                        text: 
                            "Scroll"
                        color: (0,0,0,1)
                        font_size: 18
                        size_hint: (0.2, None)
                        height: 36
                    Label:
                        text: 
                            "Scroll"
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
            Color:
                rgb: (0,0,0)
            Line:
                width:2
                rectangle: (self.x, self.y, self.width, self.height)
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
