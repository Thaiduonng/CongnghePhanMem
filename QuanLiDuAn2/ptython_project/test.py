from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import MDTextButton
from kivymd.uix.button import MDRoundFlatIconButton
from kivymd.uix.label import MDLabel

Window.size = (800, 600)

screen_helper = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:
<MenuScreen>:
    name: 'menu'
    Screen:
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "chức năng"
                        elevation: 10
                        left_action_items: [['account-circle', lambda x: nav_drawer.toggle_nav_drawer()]]
                    Widget:
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
                Image:
                    source: 'user3.png'
                MDLabel:
                    text: 'Người dùng'
                    size_hint_y: None
                    height:self.texture_size[1]
                    
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Thông tin cá nhân'
                            IconLeftWidget:
                                icon: 'account-details'
                                on_press: root.manager.current = 'profile'
                        OneLineIconListItem:
                            text: 'Cập nhật thông tin'
                            on_press: root.manager.current = 'upload'
                            IconLeftWidget:
                                icon: 'account-edit'
                        OneLineIconListItem:
                            text: 'Đăng xuất'
                            IconLeftWidget:
                                icon: 'logout'
<ProfileScreen>:
    name: 'profile'
    MDLabel:
        text: 'Profile'
    MDTextButton:
        text: 'Back'
        on_press: root.manager.current = 'menu'
<UploadScreen>:
    name: 'upload'
    MDLabel:
        text: 'Upload'
    MDTextButton:
        text: 'Back'
        on_press: root.manager.current = 'menu'
"""

class MenuScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

class UploadScreen(Screen):
    pass

class DemoApp(MDApp):
    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen

if __name__ == '__main__':
    DemoApp().run()
