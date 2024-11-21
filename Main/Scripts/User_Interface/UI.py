from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import openpyxl


class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Input fields
        self.name_input = TextInput(hint_text="Enter Name", multiline=False, font_size=24)
        self.date_input = TextInput(hint_text="Enter Date (YYYY-MM-DD)", multiline=False, font_size=24)

        # Adding labels and text inputs
        self.add_widget(Label(text="Name", font_size=24))
        self.add_widget(self.name_input)

        self.add_widget(Label(text="Date", font_size=24))
        self.add_widget(self.date_input)

        # On-screen keyboard (simple with only numbers and letters for example purposes)
        self.keyboard_layout = GridLayout(cols=10, size_hint_y=None, height=200)
        keys = '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for key in keys:
            button = Button(text=key, on_release=self.key_pressed, font_size=20)
            self.keyboard_layout.add_widget(button)
        self.add_widget(self.keyboard_layout)

        # Submit and Exit Buttons
        self.button_layout = BoxLayout(size_hint_y=0.3)
        submit_button = Button(text="Submit", on_release=self.submit_data, font_size=24)
        exit_button = Button(text="Exit", on_release=self.exit_app, font_size=24)
        self.button_layout.add_widget(submit_button)
        self.button_layout.add_widget(exit_button)
        self.add_widget(self.button_layout)

    def key_pressed(self, instance):
        # Detects the active TextInput and inserts the key pressed
        if self.name_input.focus:
            self.name_input.text += instance.text
        elif self.date_input.focus:
            self.date_input.text += instance.text

    def submit_data(self, instance):
        name = self.name_input.text
        date = self.date_input.text

        # Create or load an Excel workbook
        file_path = "user_data.xlsx"
        try:
            workbook = openpyxl.load_workbook(file_path)
            sheet = workbook.active
        except FileNotFoundError:
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            sheet.append(["Name", "Date"])  # Header row

        # Append data to the workbook
        sheet.append([name, date])
        workbook.save(file_path)

        # Clear inputs after submitting
        self.name_input.text = ""
        self.date_input.text = ""

    def exit_app(self, instance):
        App.get_running_app().stop()


class MyApp(App):
    def build(self):
        return MainLayout()


if __name__ == "__main__":
    MyApp().run()
