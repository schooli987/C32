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
            hint_text='Enter Amount in USD',
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
       
        reset_btn = Button(
            text='RESET',
            font_size=18,
            background_color=(255, 0, 0, 1),
            bold=True,
            color=(1, 1, 1, 1),
            size_hint=(0.2, 1)
        )
       

        input_box.add_widget(self.text_input)
        input_box.add_widget(self.currency_spinner)
        input_box.add_widget(convert_btn)
        input_box.add_widget(reset_btn)
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
        except ValueError:
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


    base_currency = "EUR"                        # Example: base currency selected is EUR
    amount_text = "100"                         # Example: user input amount as string "100"
    amount = float(amount_text)                  # Convert input string to float: 100.0

    usd_to = {                                  # Hardcoded exchange rates with USD as base
        "USD": 1.0,
        "EUR": 0.92,
        "CAD": 1.36,
        "INR": 83.5,
        "JPY": 157.4
    }

    usd_per_unit = 1 / usd_to[base_currency]   # Convert base currency to USD (1 EUR ≈ 1/0.92 ≈ 1.087 USD)

    amount_in_usd = amount * usd_per_unit       # Convert input amount to USD (100 EUR ≈ 108.7 USD)

    for country, data in COUNTRIES.items():     # Loop through each country in the dictionary
        label = self.country_labels[country]    # Get label for current country
        target_currency = data['currency']      # Target currency for the country

        target_per_usd = usd_to[target_currency]    # USD to target currency rate (e.g. USD to INR = 83.5)
        converted_amount = amount_in_usd * target_per_usd   # Convert USD amount to target currency

        label.text = f"{country}\n{converted_amount:.2f} {target_currency}"  # Update label text with converted value

if __name__ == '__main__':
    CurrencyApp().run()







