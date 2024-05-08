from kivy.app import App 
from kivy.network.urlrequest import UrlRequest
from kivy.uix.image import AsyncImage 
from kivy.uix.boxlayout import BoxLayout

class MinhaApp(App): 
    def build(self):
        layout= BoxLayout()
        url= "https://th.bing.com/th/id/OIP.EHu_LXz4IpAybJwsDRDJ5QHaEK?rs=1&pid=ImgDetMain"
        image= AsyncImage(source=url)
        layout.add_widget(image)
        return layout
    
if __name__ == "__main__": 
    MinhaApp().run()