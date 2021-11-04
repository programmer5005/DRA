from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class DRAssistantApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, Assistant", halign="center")


DRAssistantApp().run()
