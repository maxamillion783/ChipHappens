from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class NoFocusButton(Button):
    """A Button that doesn't steal focus from TextInputs."""
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            return self.on_press() or True
        return super().on_touch_down(touch)

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Create TextInput widgets
        self.text_input1 = TextInput(hint_text="Input 1")
        self.text_input2 = TextInput(hint_text="Input 2")
        layout.add_widget(self.text_input1)
        layout.add_widget(self.text_input2)

        # Create a NoFocusButton
        button = NoFocusButton(text="Append Text")
        button.bind(on_press=self.append_to_focused_input)
        layout.add_widget(button)

        return layout

    def append_to_focused_input(self, instance):
        """Append text to the currently focused TextInput."""
        if self.text_input1.focus:
            self.text_input1.text += " Appended Text!"
        elif self.text_input2.focus:
            self.text_input2.text += " Appended Text!"
        else:
            print("No TextInput is currently focused")

# Run the app
if __name__ == "__main__":
    MyApp().run()