from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
#from kivymd.uix.list import OneLineListItem, MDList, TwoLineListItem
#from kivymd.uix.button import
#from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivymd.uix.button import MDTextButton, MDIconButton
#from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.dialog import MDDialog
#from kivymd.uix.card import MDCard
import sqlite3

Window.size = (500, 600)


class LoginScreen(Screen):
    pass
class CreateAccScreen(Screen):
    pass
class MenuScreen(Screen):
    pass
class ProfileScreen(Screen):
    pass
class UploadScreen(Screen):
    pass
class HelpScreen(Screen):
    pass




class Quan_liApp(MDApp):
    def build(self):
        #Các màu chủ đề: ‘Red’, ‘Pink’, ‘Purple’, ‘DeepPurple’,
        # ‘Indigo’, ‘Blue’, ‘LightBlue’, ‘Cyan’, ‘Teal’, ‘Green’,
        # ‘LightGreen’, ‘Lime’, ‘Yellow’, ‘Amber’, ‘Orange’,
        # ‘DeepOrange’, ‘Brown’, ‘Gray’, ‘BlueGray’
        self.theme_cls.primary_palette = "Teal"
        #self.theme_cls.theme_style = "Dark"
        return Builder.load_file('giao_dien.kv')

    def logger(self):
        self.root.get_screen('man_hinh_dang_nhap').ids.quan_li.text = f'Chào {self.root.get_screen('man_hinh_dang_nhap').ids.user.text}'
    def clear(self):
        self.root.get_screen('man_hinh_dang_nhap').ids.quan_li.text = "QUẢN LÍ NHÂN KHẨU"
        self.root.get_screen('man_hinh_dang_nhap').ids.user.text = ""
        self.root.get_screen('man_hinh_dang_nhap').ids.password.text =""
    def showdata(self, instance):
        if self.root.get_screen('man_hinh_dang_nhap').ids.user.text is "" or self.root.get_screen('man_hinh_dang_nhap').ids.password.text is "":
            check_string = 'Vui lòng nhập tên tài khoản và mật khẩu'
        else:
            check_string = f'tên tài khoản: {self.root.get_screen('man_hinh_dang_nhap').ids.user.text} \nmật khẩu: {self.root.get_screen('man_hinh_dang_nhap').ids.password.text}'
        close_button = MDIconButton(icon='close', on_release=self.close_dialog)
        login_button = MDIconButton(icon='login', on_release= self.interface)
        self.dialog = MDDialog(
            title='Kiểm tra thông tin',
            text = check_string,
            size_hint=(0.8, 0.8),
            buttons=[close_button, login_button]
        )
        self.dialog.open()

    def close_dialog(self, instance):
        # Đảm bảo nhận tham số instance
        self.dialog.dismiss()
    def interface(self, instance):
        self.dialog.dismiss()
        self.root.get_screen('man_hinh_dang_nhap').manager.current = 'giao_dien_chinh'



if __name__ == '__main__':
    Quan_liApp().run()
