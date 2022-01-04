from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty
from remove_bg_api import RemoveBg

kv = '''
MDFloatLayout:
    MDCard:
        pos_hint: {'center_x': .5, 'center_y': .7}
        size_hint: .5, .5
        canvas.before:
            Rectangle:
                pos: self.pos
                size: self.size
                source: app.path
    MDTextField:
        id: save_as
        hint_text: "Save As"
        pos_hint: {'center_x': .5, 'center_y': .35}
        size_hint: .5, .098
    MDTextField:
        id: extension
        hint_text: "Extension"
        pos_hint: {'center_x': .5, 'center_y': .25}
        size_hint: .5, .098
    MDRaisedButton:
        text: "Remove"
        pos_hint: {'center_x': .5, 'center_y': .115}
        on_release: app.remove_bg(save_as.text, extension.text)
'''


class RemoveImageBackground(MDApp):

    path = StringProperty()

    def build(self):
        Window.bind(on_dropfile=self.on_file_drop)
        return Builder.load_string(kv)

    def on_file_drop(self, window, file_path):
        self.path = str(file_path.decode("utf-8"))

    def remove_bg(self, save_as, extension):
        remove_bg = RemoveBg('Your API Key Here')
        remove_bg.remove_bg_file(input_path=self.path, out_path="./"+save_as+"."+extension, size="preview", raw=False)


if __name__ == '__main__':
    RemoveImageBackground().run()
