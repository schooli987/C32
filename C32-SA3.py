from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

COUNTRIES = {
    "USA": {"currency": "USD", "pos": (0.14, 0.41)},
    "Canada": {"currency": "CAD", "pos": (0.13, 0.5)},
    "Europe": {"currency": "EUR", "pos": (0.55, 0.48)},
    "India": {"currency": "INR", "pos": (0.65, 0.32)},
    "Japan": {"currency": "JPY", "pos": (0.84, 0.4)}
}
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
        input_box = BoxLayout(
            orientation='horizontal',
            spacing=10,
            size_hint=(0.9, None),
            height=60,
            pos_hint={'center_x': 0.5, 'y': 0.83}
        )

        self.text_input = TextInput(
            hint_text='Enter Amount to Convert',
            multiline=False,
            input_filter='float',
            font_size=20,
            background_color=(1, 1, 1, 0.9),
            foreground_color=(0, 0, 0, 1),
            size_hint=(0.3, 1)
        )

        self.currency_spinner = Spinner(
            text='SELECT CURRENCY',
            values=['USD', 'EUR', 'CAD', 'INR', 'JPY'],
            font_size=18,
            color=(0, 0, 0, 1),
            bold=True,
            background_color=(0, 255, 0, 0.9),
            size_hint=(0.3, 1)
        )

        convert_btn = Button(
            text='CONVERT',
            font_size=18,
            background_color=(255,69,0),
            bold=True,
            color=(0, 0, 0, 1),
            size_hint=(0.3, 1),
            on_press=self.convert_and_show
        )
  

        input_box.add_widget(self.text_input)
        input_box.add_widget(self.currency_spinner)
        input_box.add_widget(convert_btn)
        self.layout.add_widget(input_box)

        self.country_labels = {}
        for country, data in COUNTRIES.items():
            label = Label(
                text=f"{country}\n...",
                halign="center",
                valign="middle",
                bold=True,
                font_size=20,
                markup=True,
                color=(1,1,1, 1),  # Black text
                size_hint=(None, None),
                size=(160, 60),
                pos_hint={'x': data['pos'][0], 'y': data['pos'][1]}
          )

            self.country_labels[country] = label
            self.layout.add_widget(label)


        return self.layout
    
    
    def convert_and_show(self, instance):
        base_currency = self.currency_spinner.text
        amount_text = self.text_input.text

        try:
            amount = float(amount_text)
        except:
            print("Invalid amount entered.")
            return

        usd_to = {
            "USD": 1.0,
            "EUR": 0.92,
            "CAD": 1.36,
            "INR": 83.5,
            "JPY": 157.4
        }

        if base_currency in usd_to:
            converted_amount = amount * usd_to[base_currency]
            for country, data in COUNTRIES.items():
                label = self.country_labels[country]
                label.text = f"{country}\n{converted_amount:.2f} {data['currency']}"


  

if __name__ == '__main__':
    CurrencyApp().run()







