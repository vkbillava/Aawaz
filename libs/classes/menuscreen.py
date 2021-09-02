from kivy.uix.screenmanager import Screen

from kivy.uix.modalview import ModalView
from kivy.utils import get_color_from_hex, get_hex_from_color

from kivymd.color_definitions import colors, palette
from kivymd.theming import ThemableBehavior
from list_items import OneLineLeftWidgetItem

class MenuScreen(Screen):
    pass

class DialogChangeTheme(ThemableBehavior, ModalView):
    def set_list_colors_themes(self):
        for name_theme in palette:
            self.ids.rv.data.append(
                {
                    "viewclass": "OneLineLeftWidgetItem",
                    "color": get_color_from_hex(colors[name_theme]["500"]),
                    "text": name_theme,
                } 
            )