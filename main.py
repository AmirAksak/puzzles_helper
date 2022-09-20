import pyperclip
import tkinter as tk

from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image

from my_functions import get_files_list

DEBUG = False

# Узнаём реальный размер экрана устройства
root = tk.Tk()
device_screen_size = {'width': root.winfo_screenwidth(), 'height': root.winfo_screenheight()}

# Ставим размер окна
if DEBUG:
    Window.size = (int(device_screen_size['height'] / 4), int(device_screen_size['height'] / 2))
else:
    Window.size = (device_screen_size['height'], device_screen_size['height'])

smiles_dir = 'images/smiles/'
smiles_names = [i[1][:-4] for i in get_files_list(smiles_dir)]

colors_list = ['ffffff', '000000', 'ff0000', '00ff00', '0000ff', 'ffff00', 'ff00ff', '00ffff',
               'dddddd', '333333', 'ff9999', '99ff99', '9999ff', 'ffff99', 'ff99ff', '99ffff',
               'aaaaaa', '666666', '996666', '669966', '666699', '999966', '996699', '669999',
               '999999', 'cc9999', '99cc99', '9999cc', '99cccc', 'cccc99', 'aaaa33', '33ccff',
               ]


class SmileButton(Button):
    def __init__(self, value, **kwargs):
        super().__init__(**kwargs)
        self.on_press = self.button_pressed
        self.value = value

    def button_pressed(self):
        MyApp.input_text.text += f':{self.value}:'


class ColorButton(Button):
    def __init__(self, value, **kwargs):
        super().__init__(**kwargs)
        self.on_press = self.button_pressed
        self.value = value
        self.background_color = f'#{self.value}'
        self.background_normal = ''

    def button_pressed(self):
        MyApp.input_text.text += f'[#{self.value}]'


class MyApp(App):
    input_text = TextInput(size_hint=(1, .2))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.wind_width, self.wind_height = Window.size

        # Экран заставки
        self.logo_table = AnchorLayout(anchor_y='center')
        logo_image = Image(source='images/logo.png')
        logo_image.center = (.5, .5)
        self.logo_table.add_widget(logo_image)

        # Создаём экран вставки улыбочки
        self.insert_smile_table = GridLayout(cols=7, rows=None)
        self.insert_smile_table.clear_widgets()
        for n in smiles_names:
            self.insert_smile_table.add_widget(SmileButton(n,
                                                           background_normal=f'{smiles_dir}{n}.png',
                                                           size_hint=(.02, .02),
                                                           ))

        # Создаём экран вставки цвета
        self.insert_color_table = GridLayout(cols=4, rows=8)
        self.insert_color_table.clear_widgets()
        for n in colors_list:
            self.insert_color_table.add_widget(ColorButton(n))

        # Кнопка "Копировать текст"
        self.button_copy_text = Button(
            text='Скопировать текст',
            size_hint=(1, .1),
            on_press=self.button_copy_text_pressed,
            background_color=(.5, .5, .5, 1),
            background_normal='',
        )

    def build(self):
        button_smiles = Button(
            text='Смайлы',
            font_size=16,
            on_press=self.button_input_smiles,
            background_color=(.5, .5, .5, 1),
            background_normal='',
        )

        button_colors = Button(
            text='Цвета',
            font_size=16,
            on_press=self.button_input_colors,
            background_color=(.5, .5, .5, 1),
            background_normal='',
        )

        top_buttons_layout = BoxLayout(size_hint=(1, .1))
        top_buttons_layout.add_widget(button_smiles)
        top_buttons_layout.add_widget(button_colors)

        top_menu_layout = AnchorLayout(anchor_x='center', anchor_y='top')
        top_menu_layout.add_widget(top_buttons_layout)

        self.input_data_layout = BoxLayout(size_hint=(1, .9), orientation='vertical')
        self.input_data_layout.add_widget(self.logo_table)
        self.input_data_layout.add_widget(self.button_copy_text)
        self.input_data_layout.add_widget(MyApp.input_text)

        main_layout = FloatLayout()
        with main_layout.canvas:
            Color(50 / 255, 100 / 255, 140 / 255, 1)
            Rectangle(size=Window.size)

        main_layout.add_widget(top_menu_layout)
        main_layout.add_widget(self.input_data_layout)

        return main_layout  # top_menu_layout

    def button_input_smiles(self, instance):
        # print('Вставка смайликов')
        self.input_data_layout.clear_widgets()
        self.input_data_layout.add_widget(self.insert_smile_table)
        self.input_data_layout.add_widget(self.button_copy_text)
        self.input_data_layout.add_widget(MyApp.input_text)

    def button_input_colors(self, instance):
        # print('Вставка цвета')
        self.input_data_layout.clear_widgets()
        self.input_data_layout.add_widget(self.insert_color_table)
        self.input_data_layout.add_widget(self.button_copy_text)
        self.input_data_layout.add_widget(MyApp.input_text)

    def button_copy_text_pressed(self, instance):
        text = self.input_text.text.strip()
        if text:
            pyperclip.copy(text)
        else:
            #print('НЕЧЕГО КОПИРОВАТЬ')
            pass


if __name__ == '__main__':
    MyApp().run()
