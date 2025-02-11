from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

KV = '''
<JobInfoPanel>:
    GridLayout:
        cols: 2
        rows: 6
        spacing: 5
        padding: 10
        Label:
            text: "Job ID"
            color: (0,0,0,1)
        TextInput:
            hint_text: ""
            color: (0,0,0,1)
        Label:
            text: "SubJob ID"
            color: (0,0,0,1)
        TextInput:
            hint_text: ""
            color: (0,0,0,1)
        Label:
            text: "Batch ID"
            color: (0,0,0,1)
        TextInput:
            hint_text: ""
            color: (0,0,0,1)
        Label:
            text: "Operator ID"
            color: (0,0,0,1)
        TextInput:
            hint_text: ""
            color: (0,0,0,1)
        Label:
            text: "Serial Number"
            color: (0,0,0,1)
        Label:
            text: "002"
            color: (0,0,0,1)
        Label:
            text: "Version"
            color: (0,0,0,1)
        Label:
            text: "V01"
            color: (0,0,0,1)

<Panel2>:
    BoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 5
        Label:
            text: "Box Label"
        TextInput:
            hint_text: "Type here"
        Button:
            text: "Click Me"

<Panel3>:
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'center'
        Button:
            text: "Centered Button"

BoxLayout:
    orientation: 'vertical'
    spacing: 10
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
                rgb: (1,1,1,1)  # Red background
            Rectangle:
                pos: self.pos
                size: self.size
            Color:
                rgb: (0,0,0)
            Line:
                width:2
                rectangle: (self.x, self.y, self.width, self.height)

    Panel2:
        canvas.before:
            Color:
                rgb: (0.3, 0.8, 0.3)  # Green background
            Rectangle:
                pos: self.pos
                size: self.size

    Panel3:
        canvas.before:
            Color:
                rgb: (0.3, 0.3, 0.8)  # Blue background
            Rectangle:
                pos: self.pos
                size: self.size
'''

class JobInfoPanel(BoxLayout):
    pass

class Panel2(BoxLayout):
    pass

class Panel3(BoxLayout):
    pass

class MyApp(App):
    def build(self):
        return Builder.load_string(KV)

if __name__ == '__main__':
    MyApp().run()
