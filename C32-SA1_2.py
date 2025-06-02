from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class CurrencyApp(App):
    def build(self):
        self.layout = FloatLayout()

          # Title
        title = Label(
            text='[b]REALTIME CURRENCY MAP[/b]',
            markup=True,
            font_size=34,
            color=(1, 1, 1, 1),
            size_hint=(1, None),
            height=80,
            pos_hint={'center_x': 0.5, 'top': 1}
        )
        self.layout.add_widget(title)

        # World map background
        self.map_image = Image(source='world_map.png', allow_stretch=True, keep_ratio=True,
                               size_hint=(1, 0.8), pos_hint={'center_x': 0.5, 'y': -0.01})
        self.layout.add_widget(self.map_image)

         # Input BoxLayout
        input_box = BoxLayout( orientation='horizontal',spacing=10, size_hint=(0.9, None), height=60,
                              pos_hint={'center_x': 0.5, 'y': 0.83}
        )

        self.text_input = TextInput( hint_text='Enter Amount in USD',multiline=False,input_filter='float',font_size=20,
            background_color=(1, 1, 1, 0.9),foreground_color=(0, 0, 0, 1),size_hint=(0.3, 1)
        )

        self.currency_spinner = Spinner(text='SELECT CURRENCY', values=['USD', 'EUR', 'CAD', 'INR', 'JPY'],font_size=18,
            color=(0, 0, 0, 1), bold=True, background_color=(0, 255, 0, 0.9), size_hint=(0.3, 1)
        )

        convert_btn = Button( text='CONVERT',font_size=18,background_color=(255,69,0),bold=True,color=(0, 0, 0, 1),size_hint=(0.3, 1)
        )
       
        reset_btn = Button( text='RESET', font_size=18, background_color=(255, 0, 0, 1), bold=True, color=(1, 1, 1, 1),
            size_hint=(0.2, 1)
        )
       

        input_box.add_widget(self.text_input)
        input_box.add_widget(self.currency_spinner)
        input_box.add_widget(convert_btn)
        input_box.add_widget(reset_btn)
        self.layout.add_widget(input_box)


        return self.layout
if __name__ == '__main__':
    CurrencyApp().run()







