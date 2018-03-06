"""Code written by Nícolas Brandão"""

import string
import secrets
from kivy.app import App
from kivy.config import Config
Config.set('graphics', 'resizable', False)
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class ApplicationLayout(FloatLayout):

    def spinnerValues(self, min_value, max_value):

        self.possible_values = []
        for k in range(min_value, max_value + 1):
            self.possible_values.append("" + str(k) + "")

        return self.possible_values

    def clearSelection(self):

        self.ids.sp_passw_length.text = '6'
        self.ids.cb_word.active = False
        self.ids.cb_letters.active = False
        self.ids.cb_lowercase.active = False
        self.ids.cb_uppercase.active = False
        self.ids.cb_repeated_chars.active = False
        self.ids.cb_numbers.active = False
        self.ids.cb_special_chars.active = False
        self.ids.lb_strength.text = 'Weak'
        self.ids.pb_strength.value = int(self.ids.sp_passw_length.text) * 2
        self.ids.it_word.text = ''
        self.ids.sp_quantity.text = '1'

    def currentValue(self, size):

        return size

    def updateStrength(self, value):

        if value <= 33.33:
            return 'Weak'
        elif value <= 66.67:
            return 'Medium'
        else:
            return 'Strong'

    def getSelectedOptions(self, pass_length):
        separator = ''  # no separator
        allowed_chars = ''

        try:
            if self.ids.cb_word.active:
                pass  # implement later

            else:
                pass

            if self.ids.cb_uppercase.active:
                allowed_chars = string.ascii_uppercase

            else:
                pass

            if self.ids.cb_lowercase.active:
                allowed_chars += string.ascii_lowercase

            else:
                pass

            if self.ids.cb_numbers.active:
                allowed_chars += string.digits

            else:
                pass

            if self.ids.cb_special_chars.active:
                allowed_chars += string.punctuation

            else:
                pass

            user_passwords = [(separator.join(secrets.choice(allowed_chars) for _ in range(pass_length)))
                              for _ in range(int(self.ids.sp_quantity.text))]

            """------------------------Float Layout to hold the passwords------------------------------"""
            box_passwords = BoxLayout(orientation='vertical', spacing=100, padding=[0, 50, 0, 50])

            lb_passwords = Label(text='\n'.join(map(str, user_passwords)),
                                  size_hint=[1.0, 0])

            btn_ok = Button(text="OK",
                            size_hint=[0.18, None],
                            pos_hint={'center_x': 0.5},
                            background_normal='',
                            background_color=(63/255, 191/255, 191/255, 0.6))

            box_passwords.add_widget(lb_passwords)
            box_passwords.add_widget(btn_ok)

            popup_passwd = Popup(title="Your Password(s)",
                                 content=box_passwords,
                                 size_hint=(None, None),
                                 auto_dismiss=False,
                                 size=(500, 500))

            btn_ok.bind(on_press=popup_passwd.dismiss)

            popup_passwd.open()

        except IndexError:

            """ Kivy popup doesn't accept more than one widget, so create a container that holds all of them """

            box = BoxLayout(orientation="vertical", spacing=80, padding=[0, 50, 0, 50])
            error_msg = "Cannot generate password without characters!\n Please, select at least one type of character."

            lb_error_msg = Label(text=error_msg,
                                 size_hint=[1.0, 0.1],
                                 pos_hint={'center_x': 0.5, 'top': 0.4})

            btn_close = Button(text="Got it!",
                               size_hint=[0.3, 0.04],
                               pos_hint={'center_x': 0.5, 'bottom': 0.65},
                               background_normal='',
                               background_color=(63/255, 191/255, 191/255, 0.6))

            box.add_widget(lb_error_msg)
            box.add_widget(btn_close)

            popup = Popup(title="Error",
                          content=box,
                          size_hint=(None, None),
                          auto_dismiss=False,
                          size=(400, 400))

            btn_close.bind(on_press=popup.dismiss)

            popup.open()


class PasswordGeneratorApp(App):

    def build(self):
        Window.clearcolor = (67 / 255, 67 / 255, 67 / 255, 1)
        self.title = 'Password Generator Beta'
        return ApplicationLayout()


if __name__ == "__main__":
    PasswordGeneratorApp().run()
