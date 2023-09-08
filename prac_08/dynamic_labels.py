from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelApp(App):
    """Main program"""

    def __init__(self, **kwargs):
        """Construct the main app"""
        super().__init__(**kwargs)
        self.colors = ["Moccasin", "Thistle", "Sea Green", "Steel Blue", "Cornsilk", "Beige",
                       "Ivory"]

    def build(self):
        """Build the kivy GUI"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create label from data and display them on GUI"""
        for color in self.colors:
            temp_label = Label(text=color)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelApp().run()
