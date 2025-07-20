from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        btn = Button(text="Нажми меня!", size_hint=(0.5, 0.5))
        btn.bind(on_press=self.on_button_click)
        layout.add_widget(btn)
        return layout

    def on_button_click(self, instance):
        print("Кнопка нажата!")

if __name__ == '__main__':
    MyApp().run()