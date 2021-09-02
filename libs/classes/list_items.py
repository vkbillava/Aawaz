from kivy.properties import ListProperty, StringProperty

from kivymd.uix.list import OneLineAvatarListItem, OneLineIconListItem



class OneLineLeftWidgetItem(OneLineAvatarListItem):
    color = ListProperty()

class IconListItem(OneLineIconListItem):
    icon = StringProperty()