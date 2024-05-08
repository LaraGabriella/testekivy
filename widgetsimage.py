from kivy.app import App 
from kivy.uix.image import Image 

class MinhaApp(App): 
    def build(self): 
        return Image(source="/Users/aluno.sesipaulista/Desktop/testekivy/img/mv5byznhowfjzditotc4zs00otq0lt.jpg") 

if __name__ == "__main__": 
    MinhaApp().run()

