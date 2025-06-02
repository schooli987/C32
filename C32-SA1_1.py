from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image

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

        return self.layout
if __name__ == '__main__':
    CurrencyApp().run()







