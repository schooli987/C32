from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
class CurrencyApp(App):
    def build(self):
       return  Label(text="Welcome to the Currency Converter App")


if __name__ == '__main__':
    CurrencyApp().run()