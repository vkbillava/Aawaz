from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDFlatButton, MDFloatingActionButton
from kivy.core.clipboard import Clipboard
from kivymd.toast import toast
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.dialog import MDDialog
from kivy.core.window import Window
from kivy.uix.image import Image
from random import (
    randint,
    sample
)
import sys
import threading

sys.path.append("E:\\Aawaz Project\\functions")

from ImageToText.convert import image_convert
from DocToText.convert import doc_convert
from PdfToText.convert import pdf_convert
from VoiceToText.main import get_audio as gt
from Voice.voice import (
    speak,
    stop
)
from VoiceAssistant.asis import active
from Hash.hash import (
    get_hash,
    pass_hash,
    store_pass_hash,
    hash_decode
)
from Database.db import (
    create_db,
    signupdb,
    logindb,
    insertdb,
    displaydb,
    login_updatedb,
    logoutdb,
    user_deldb,
    display_all,
    dropdb,
    insertpassdb,
    update_passdb,
    show_passdb,
    forgot_passdb
)


sys.path.append("E:\\Aawaz Project\libs\classes")


from menuscreen import DialogChangeTheme
from docscreen import DocScreen
from dbscreen import DbScreen
from pdfscreen import PdfScreen
from imagescreen import ImgScreen
from menuscreen import MenuScreen
from signupscreen import SignupScreen
from loginscreen import LoginScreen
from forgetscreen import ForgetScreen
from textscreen import TextScreen
from voicescreen import VoiceScreen
from managescreen import ManageScreen
from showpass import PassShowScreen
from storepass import PassStoreScreen
from updatepass import PassUpadateScreen
from assistantscreen import AssistantScreen
from display import (
    Display,
    DisplayText,
    DisplayKey,
    DisplayHelp
)

import os.path

# Load the kv files
folder = os.path.dirname(os.path.realpath(__file__))
folder += "/libs/kv"
Builder.load_file(folder + "/imagescreen.kv")
Builder.load_file(folder + "/pdfscreen.kv")
Builder.load_file(folder + "/docscreen.kv")
Builder.load_file(folder + "/dbscreen.kv")
Builder.load_file(folder + "/signupscreen.kv")
Builder.load_file(folder + "/loginscreen.kv")
Builder.load_file(folder + "/forgetscreen.kv")
Builder.load_file(folder + "/menuscreen.kv")
Builder.load_file(folder + "/display.kv")
Builder.load_file(folder + "/textscreen.kv")
Builder.load_file(folder + "/voicescreen.kv")
Builder.load_file(folder + "/managescreen.kv")
Builder.load_file(folder + "/storepass.kv")
Builder.load_file(folder + "/showpass.kv")
Builder.load_file(folder + "/updatepass.kv")
Builder.load_file(folder + "/assistantscreen.kv")
Builder.load_file(folder + "/list_items.kv")





class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen,self).__init__(**kwargs)

class WelcomeScreen(Screen):
    pass


class AawazApp(MDApp):

    def __init__(self, **kwargs):
        Window.size = (800,600)
        super().__init__(**kwargs)

        self.theme_cls.primary_palette = "Teal"
        self.dialog_change_theme = None
        self.toolbar = None


    def build(self):

        self.src = '\FinalProject\\back1.png'

        self.sm = Screen()
        self.wing = Image(source = self.src, allow_stretch = True, size_hint = (2, 2),pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.theme_cls.theme_style = "Dark"
        self.strng = Builder.load_file('libs\kv\\aawaz.kv')
        
    
        #self.sm.add_widget(self.wing)
        self.sm.add_widget(self.strng)


        self.file_manager = MDFileManager(
            exit_manager = self.on_filemanager_exit,
            select_path = self.on_select_path,

        )

        return self.sm


    def login(self):

        loginUsername = self.strng.get_screen('loginsc').ids.login_username.text
        loginPassword = pass_hash(self.strng.get_screen('loginsc').ids.login_password.text)
        #loginPassword = pass_hash(loginPassword)
        #self.login_check = False
        result = logindb(loginUsername)
        # uname, paswd, log, key = logindb(loginUsername)
        # print(uname, paswd, log, key)

        close_btn = MDFlatButton(text="Close", on_release=self.close_dialog)

        try:
            if len(result) == 0:
                self.strng.get_screen('loginsc').ids.login_username.text = ''
                self.strng.get_screen('loginsc').ids.login_password.text = ''
                self.strng.get_screen('signupsc').manager.current = 'signupsc'
                self.dialog = MDDialog(title='User Not Found', text='You are not a registered user please signup',
                size_hint = (0.7, 0.2), buttons = [close_btn])
                self.dialog.open()
            else:
                stored_username = result[0]
                stored_password = result[1]
                print(result[3])

                if loginUsername == '':
                    self.dialog = MDDialog(title='User Name cannot be blank', size_hint=(0.7, 0.2), buttons=[close_btn])
                    self.dialog.open()

                elif loginPassword == '':
                    self.dialog = MDDialog(title='Password cannot be blank', size_hint=(0.7, 0.2), buttons=[close_btn])
                    self.dialog.open()
                else:

                    if loginUsername == stored_username:
                        if loginPassword == stored_password:
                            login_updatedb(loginUsername)
                            self.store.put('LoginInfo', username=stored_username)
                            self.strng.get_screen('loginsc').ids.login_password.text = ''
                            self.strng.get_screen('menusc').manager.current = 'menusc'
                        else:
                            self.dialog = MDDialog(title='Wrong Password', text="Please enter correct Password",
                                                   size_hint=(0.7, 0.2), buttons=[close_btn])
                            self.dialog.open()

                            self.strng.get_screen('loginsc').ids.login_password.text = ''
                    else:
                        self.dialog = MDDialog(title='Invalid Username', text="Please enter correct Username",
                                               size_hint=(0.7, 0.2), buttons=[close_btn])
                        self.dialog.open()
                        self.strng.get_screen('loginsc').ids.login_username.text = ''
                        self.strng.get_screen('loginsc').ids.login_password.text = ''


        except KeyError:
            self.strng.get_screen('loginsc').ids.login_username.text = ''
            self.strng.get_screen('loginsc').ids.login_password.text = ''
            self.strng.get_screen('signupsc').manager.current = 'signupsc'
            self.dialog = MDDialog(title='User Not Found', text='You are not a registered user please signup',
                                   size_hint=(0.7, 0.2), buttons=[close_btn])
            self.dialog.open()

    def logout(self):
        username = self.store.get('LoginInfo')['username']
        logoutdb(username)
        self.strng.get_screen('loginsc').manager.current = 'loginsc'


    def signup(self):
        # result = logindb()
        # uname = ''
        # if len(result) != 0:
        #     uname = result[0]

        self.signupUsername = self.strng.get_screen('signupsc').ids.signup_username.text
        signupPassword = self.strng.get_screen('signupsc').ids.signup_password.text

        cancel_btn_username_dialogue = MDFlatButton(text = 'Retry',on_release = self.close_dialog)

        result = logindb(self.signupUsername)
        if len(result) != 0:
            if result[0] == self.signupUsername:
                self.dialog = MDDialog(title='Exists', text='The username already exists choose different one',
                                       size_hint=(0.7, 0.2), buttons=[cancel_btn_username_dialogue])
                self.dialog.open()

        if self.signupUsername.split() == [] or signupPassword.split() == []:
            self.dialog = MDDialog(title = 'Invalid Input',text = 'Please Enter a valid Input',size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()

        elif len(self.signupUsername) < 3:
            self.dialog = MDDialog(title = 'Invalid Input',text = 'Username must be minimum 3 digits',size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()

        elif len(self.signupUsername.split())>1:
            self.dialog = MDDialog(title = 'Invalid Username',text = 'Please enter username without space',size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()

        elif len(signupPassword) < 8 or len(signupPassword) > 16:
            self.dialog = MDDialog(title = 'Invalid Input',text = 'Password must between 8 to 16 digits',size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()



        else:
            self.recovery_key = self.forgot_key()
            signupPassword = pass_hash(signupPassword)

            signupdb(self.signupUsername,signupPassword,self.recovery_key)
            self.store.put('LoginInfo',username = self.signupUsername, password = signupPassword, log = 'F', recoveryKey = self.recovery_key)
            
            self.display_key()
            
            self.strng.get_screen('loginsc').manager.current = 'loginsc'


    def showloginpass(self):

        if self.strng.get_screen('loginsc').ids.login_password.password == True:
            self.strng.get_screen('loginsc').ids.login_password.password = False
        else:
            self.strng.get_screen('loginsc').ids.login_password.password = True


    def showsignuppass(self):
        if self.strng.get_screen('signupsc').ids.signup_password.password == True:
            self.strng.get_screen('signupsc').ids.signup_password.password = False
        else:
            self.strng.get_screen('signupsc').ids.signup_password.password = True


    def changeimage(self):
        #self.wing.source = ''
        pass

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def delete_dialog(self, obj):
        self.dialog.dismiss()
        username = self.store.get('LoginInfo')['username']
        user_deldb(username)
        self.strng.get_screen('loginsc').manager.current = 'loginsc'

    def closeapp(self):
        AawazApp().stop()
    
    def forgot_key(self):
        key_int = str(randint(192312321234, 987213351234))
        key_str = 'aefghinaerbczesprln'
        key_str += key_int
        key_combine = list(key_str)
        s = sample(key_combine, 22 , counts=None)
        return(''.join(s))

    def mainimage(self):
        self.wing.source = self.src

    def talk(self):
        close_btn = MDFlatButton(text="Close", on_release=self.close_dialog)
        speak_btn = MDFloatingActionButton(icon="microphone", on_release=self.speak_dialog)
        if self.path == "":
            self.dialog = MDDialog(title='Error', text="Select The Image", size_hint=(0.7,1), buttons=[close_btn])
            self.dialog.open()
        else:
            file_hash = get_hash(self.path)
            result = displaydb(file_hash)
            if len(result) == 0:

                if self.state == 1:
                    self.text = image_convert(self.path)
                elif self.state == 2:
                    #self.strng.get_screen('pdfsc').ids.toolbar.title = 'Pdf To Text'
                    self.text = pdf_convert(self.path)
                elif self.state == 3:
                    self.text = doc_convert(self.path)

                insertdb(file_hash, self.text)
                self.show_text()

            else:
                print("present in db")
                self.text = result[1]
                self.show_text()


    def speak_dialog(self):
        #self.dialog.dismiss()
        #speak(self.text)
        threading.Thread(target=speak, args=(self.text,), daemon=True).start()

    def separate_talk(self):
        self.th = threading.Thread(target=self.talk, daemon=True)
        self.th.start()
        #self.stop = threading.Event()

    def on_filemanager_exit(self, *args):
        self.file_manager.close()

    def on_select_path(self, path):
        self.path = path
        self.file_manager.close()
        # toast(path)
        #self.dis(self.path)

        self.talk()


    def stop_speak(self):
        stop()

    def set_img(self):
        self.state = 1

    def set_pdf(self):
        self.state = 2

    def set_doc(self):
        self.state = 3

    def open_filemanager(self):
        path = "/"
        self.file_manager.show(path)

    def set_imgext(self):
        self.file_manager.ext = ['.jpg', '.png']

    def set_pdfext(self):
        self.file_manager.ext = ['.pdf']

    def set_docext(self):
        self.file_manager.ext = ['.doc', '.docx']

    
    def verify(self):
        cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_dialog)
        username = self.strng.get_screen('forgetsc').ids.forget_username.text
        res = logindb(username)
        if len(res) == 0:
            self.dialog = MDDialog(title='Invalid Username', text='You have Entered a wrong username if you dont have an account please create one', size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
            self.strng.get_screen('forgetsc').ids.forget_username.text = ""
            self.strng.get_screen('forgetsc').ids.forget_password.text = ""
        else:
            stored_key = res[3]

            if self.strng.get_screen('forgetsc').ids.forget_password.hint_text == 'security key':

                security_key = self.strng.get_screen('forgetsc').ids.forget_password.text
                if stored_key == security_key:
                    self.strng.get_screen('forgetsc').ids.forget_password.hint_text = "Enter new Password"
                    self.strng.get_screen('forgetsc').ids.forget_password.text = ""
                else:

                    self.dialog = MDDialog(title = 'Invalid Key',text = 'Please Enter a valid Recovery Key',size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                    self.dialog.open()
                    self.strng.get_screen('forgetsc').ids.forget_password.text = ""

            else:
                stored_username = res[0]
                new_pass = self.strng.get_screen('forgetsc').ids.forget_password.text
                if len(new_pass) > 7 and len(new_pass) < 17:
                    #stored_password = self.store.get('LoginInfo')['password']
                    forgot_passdb(pass_hash(new_pass), stored_username)
                    self.strng.get_screen(
                        'forgetsc').ids.forget_password.hint_text = "security key"
                    self.strng.get_screen('forgetsc').ids.forget_password.text = ""
                    toast(f"Password changed for the username \"{stored_username}\"")
                    self.strng.get_screen('loginsc').manager.current = 'loginsc'

                else:
                    self.dialog = MDDialog(title='Invalid Input', text='Password must between 8 to 16 digits',
                                           size_hint=(0.7, 0.2), buttons=[cancel_btn_username_dialogue])
                    self.dialog.open()
        


    def switch_theme_style(self):
        self.theme_cls.theme_style = (
            "Light" if self.theme_cls.theme_style == "Dark" else "Dark"
        )
        self.strng.get_screen('menusc').ids.backdrop.ids._front_layer.md_bg_color = [0, 0, 0, 0]

    def show_dialog_change_theme(self):
        if not self.dialog_change_theme:
            self.dialog_change_theme = DialogChangeTheme()
            self.dialog_change_theme.set_list_colors_themes()
        self.dialog_change_theme.open()

    def show_text(self):
        if self.theme_cls.device_orientation == "landscape":
            code = Display(
                code = self.text,
            )
            code.open()

    def converted_text(self):
        if self.theme_cls.device_orientation == "landscape":
            txt = DisplayText(
                txt = self.txt,
            )
            txt.open()

    def display_pass(self):
        if self.theme_cls.device_orientation == "landscape":
            txt = DisplayText(
                txt = self.gen_pass(),
            )
            txt.open()

    def gen_pass(self):
        s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
        return "".join(sample(s,15))

    def display_key(self):
        self.keytxt = f"Your Recovery key is \" {self.recovery_key} \" \nNote this key, It will help you to Recover your password.\nIn case if you lost key your password is not Recoverable.\nlick the above download button to download your key...\nOr else you can copy the key using copy button"
        if self.theme_cls.device_orientation == "landscape":
            key = DisplayKey(
                key = self.keytxt,
            )
            key.open()

    def download_key(self):
        save_path = f"D:/key/{self.signupUsername}.txt"
        f = open(save_path, "w")
        f.write(self.recovery_key)
        f.close()
        toast(f"key downloaded in {save_path}")


    def set_help_text(self):
        self.help_text = ""
        with open("help.txt") as file:
            for line in file:
               self.help_text += line
        if self.theme_cls.device_orientation == "landscape":
            help_txt = DisplayHelp(
                help_txt=self.help_text,
            )
            help_txt.open()

    def to_speak(self):
        txt = self.strng.get_screen('textsc').ids.text_speak.text
        speak(txt)

    def listen(self):
        self.txt = gt()

    def to_clear(self):
        self.strng.get_screen('textsc').ids.text_speak.text = ''

    def start_assistant(self):
        active()


    def delete_user(self):
        close_btn = MDFlatButton(text="Cancel", on_release=self.close_dialog)
        delete_btn = MDFlatButton(text="Delete", on_release=self.delete_dialog)

        self.dialog = MDDialog(title='Warning', text="Account Deleted are not recoverable are you sure you want to delete your Account", size_hint=(0.7, 0.2), buttons=[delete_btn, close_btn])
        self.dialog.open()

    def drop(self):
        res = dropdb()
        if res == True:
            toast("All the records are deleted")

    def store_pass(self):
        name = self.strng.get_screen('passstore').ids.store_username.text
        password = self.strng.get_screen('passstore').ids.store_password.text

        res = show_passdb(name)
        if len(res) == 0:
            insertpassdb(name, password)

            toast("Successfully stored")

        else:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_dialog)
            self.dialog = MDDialog(title='Username Exists',
                                   text='You have Entered a username which is already present in the database you can update the password in database using update password menu',
                                   size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        self.strng.get_screen('passstore').ids.store_username.text = ""
        self.strng.get_screen('passstore').ids.store_password.text = ""

    def update_pass(self):
        name = self.strng.get_screen('updatepass').ids.store_username.text
        password = self.strng.get_screen('updatepass').ids.store_password.text

        res = show_passdb(name)
        if len(res) == 0:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_dialog)
            self.dialog = MDDialog(title='Username Exists',
                                   text='username doesn\'t exists in the database please enter a valid username',
                                   size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        else:
            update_passdb(password, name)

            toast("Successfully Updated")
            self.strng.get_screen('updatepass').ids.store_username.text = ""
            self.strng.get_screen('updatepass').ids.store_password.text = ""

    def show_pass(self):
        name = self.strng.get_screen('showpass').ids.store_username.text
        res = show_passdb(name)
        if len(res) == 0:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_dialog)
            self.dialog = MDDialog(title='Username Exists',
                                   text='username doesn\'t exists in the database please enter a valid username',
                                   size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        else:
            if self.theme_cls.device_orientation == "landscape":
                txt = DisplayText(
                    txt = res[1],
                )
                txt.open()

    def show_data(self):
        # pass
        res = display_all()
        resf = []
        j = 1
        for i in res:
            resf.append(f"               {j}\n{i}\n\n\n")
            j += 1

        self.strng.get_screen('dbsc').ids.lbl.text = ''.join(resf)

    def change_menu_click(self):
        #if self.strng.get_screen('menusc').ids.imgtxt.text == "":
        self.strng.get_screen('menusc').ids.imgtxt.text = "Image To Text"
        self.strng.get_screen('menusc').ids.pdftxt.text = "Pdf To Text"
        self.strng.get_screen('menusc').ids.doctxt.text = "Doc To Text"
        self.strng.get_screen('menusc').ids.txtvoice.text = "Text to Voice"
        self.strng.get_screen('menusc').ids.voicetxt.text = "Voice to Text"
        self.strng.get_screen('menusc').ids.assist.text = "Voice Assistant"
        self.strng.get_screen('menusc').ids.helptxt.text = "Help"

        self.strng.get_screen('menusc').ids.imgsrc.source = f"assets\\transparent.png"
        self.strng.get_screen('menusc').ids.pdfsrc.source = f"assets\\transparent.png"
        self.strng.get_screen('menusc').ids.docsrc.source = f"assets\\transparent.png"
        self.strng.get_screen('menusc').ids.txtsrc.source = f"assets\\transparent.png"
        self.strng.get_screen('menusc').ids.voicesrc.source = f"assets\\transparent.png"
        self.strng.get_screen('menusc').ids.assistsrc.source = f"assets\\transparent.png"
        self.strng.get_screen('menusc').ids.helpsrc.icon = f"assets\\transparent.png"
        
    def change_menu_release(self):
        self.strng.get_screen('menusc').ids.imgtxt.text = ""
        self.strng.get_screen('menusc').ids.pdftxt.text = ""
        self.strng.get_screen('menusc').ids.doctxt.text = ""
        self.strng.get_screen('menusc').ids.txtvoice.text = ""
        self.strng.get_screen('menusc').ids.voicetxt.text = ""
        self.strng.get_screen('menusc').ids.assist.text = ""
        self.strng.get_screen('menusc').ids.helptxt.text = ""

        self.strng.get_screen('menusc').ids.imgsrc.source = f"assets\\image-to-text.png"
        self.strng.get_screen('menusc').ids.pdfsrc.source = f"assets\\pdf-to-txt.png"
        self.strng.get_screen('menusc').ids.docsrc.source = f"assets\\doc-to-text.png"
        self.strng.get_screen('menusc').ids.txtsrc.source = f"assets\\voice.png"
        self.strng.get_screen('menusc').ids.voicesrc.source = f"assets\\voice-to-text.jpeg"
        self.strng.get_screen(
            'menusc').ids.assistsrc.source = f"assets\\assistant.jpg"
        self.strng.get_screen('menusc').ids.helpsrc.icon = f"help-circle-outline"

    def back_to_home_screen(self):
        self.strng.get_screen('menusc').manager.current = 'menusc'

    def on_start(self):
        create_db()

        self.store = JsonStore("LoginInfo.json")
        try:
            username = self.store.get('LoginInfo')['username']
            result = logindb(username)
            if len(result) != 0:
                if result[2] == "T":

                    self.strng.get_screen('menusc').manager.current = 'menusc'

            else:
                self.store = JsonStore("LoginInfo.json")
                self.strng.get_screen('welcomesc').manager.current = 'welcomesc'
                self.strng.get_screen('welcomesc').manager.transition.direction = 'right'
            # if self.store.get('LoginInfo')['log'] == "T":
            #     #self.username_changer()
            #     self.strng.get_screen('menusc').manager.current = 'menusc'
                
                
        except KeyError:
            self.strng.get_screen('welcomesc').manager.current = 'welcomesc'
            self.strng.get_screen('welcomesc').manager.transition.direction = 'right'


AawazApp().run()

        
