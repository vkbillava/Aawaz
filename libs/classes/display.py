from kivymd.theming import ThemableBehavior
from kivy.properties import StringProperty
from kivy.uix.modalview import ModalView

class Display(ThemableBehavior, ModalView):
    code = StringProperty()

class DisplayText(ThemableBehavior, ModalView):
    txt = StringProperty()

class DisplayKey(ThemableBehavior, ModalView):
    key = StringProperty()

class DisplayHelp(ThemableBehavior, ModalView):
    help_txt = StringProperty()
