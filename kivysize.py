from kivy.app import App
from kivy.uix.label import Label

class MinhaApp(App):
    def build(self):
        return Label(text="Olá, Senai!")
    
if __name__ == "__main__":
    MinhaApp().run() 