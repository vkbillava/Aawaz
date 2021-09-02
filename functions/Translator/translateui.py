from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

from translate import trans, talk

help_str = '''
ScreenManager:
    MainScreen:
    ResultScreen:

<MainScreen>:
    name: "main"
    MDTextField:
        id: txt
        pos_hint: {'center_y':0.6,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Text'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"

    MDRaisedButton:
        text:'Translate'
        size_hint: (0.13,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press:
            app.transs()
            root.manager.current = 'result'
            root.manager.transition.direction = 'left'

<ResultScreen>:
    name: "result"
    MDLabel:
        id: lbl
        text:''
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.9}
        font_name: ''

'''

class MainScreen(Screen):
    pass

class ResultScreen(Screen):
    pass

class MainApp(MDApp):

    def build(self):
        #self.sm = Screen()
        self.strng = Builder.load_string(help_str)

        #self.sm.add_widget(self.strng)
        
        return self.strng

    def transs(self):
        txt = self.strng.get_screen('main').ids.txt.text
        res = trans(txt, 'en', 'kn')
        print(res)
        
        talk(res)

        self.strng.get_screen('result').ids.lbl.font_name = 'Lohit-Kannada.ttf'
        self.strng.get_screen('result').ids.lbl.text = res

MainApp().run()