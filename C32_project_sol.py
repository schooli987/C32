from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image

class WeatherApp(App):
    def build(self):
        self.layout = FloatLayout()

        # Title
        title = Label(
            text='[b]WEATHER FORECASTING APP[/b]',
            markup=True,
            font_size=34,
            color=(1, 1, 1, 1),
            size_hint=(1, None),
            height=80,
            pos_hint={'center_x': 0.5, 'top': 1}
        )
        self.layout.add_widget(title)

        # World map background
        self.map_image = Image(
            source='weather.jpeg',
            allow_stretch=True,
            keep_ratio=True,
            size_hint=(0.3, 0.3),
            pos_hint={'center_x': 0.5, 'y': 0.6}
        )
        self.layout.add_widget(self.map_image)

        # ✅ Weather data dictionary
        weather_data = {
            'weather': 'Sunny',
            'temperature': '30°C',
            'pressure': '1013 hPa',
            'humidity': '60%'
        }

        # Labels using dictionary values
        weather_label = Label(
            text=f"Weather: {weather_data['weather']}",
            font_size=20,
            color=(1, 1, 1, 1),
            size_hint=(None, None),
            pos_hint={'center_x': 0.5, 'y': 0.5}
        )
        temp_label = Label(
            text=f"Temperature: {weather_data['temperature']}",
            font_size=20,
            color=(1, 1, 1, 1),
            size_hint=(None, None),
            pos_hint={'center_x': 0.5, 'y': 0.45}
        )
        pressure_label = Label(
            text=f"Pressure: {weather_data['pressure']}",
            font_size=20,
            color=(1, 1, 1, 1),
            size_hint=(None, None),
            pos_hint={'center_x': 0.5, 'y': 0.4}
        )
        humidity_label = Label(
            text=f"Humidity: {weather_data['humidity']}",
            font_size=20,
            color=(1, 1, 1, 1),
            size_hint=(None, None),
            pos_hint={'center_x': 0.5, 'y': 0.35}
        )

        self.layout.add_widget(weather_label)
        self.layout.add_widget(temp_label)
        self.layout.add_widget(pressure_label)
        self.layout.add_widget(humidity_label)

        return self.layout

if __name__ == '__main__':
    WeatherApp().run()
