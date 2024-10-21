
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics.texture import Texture
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
import main7
# from

# class SentencToken(Label):
#     pass

# class Sign(SentencToken):
#     pass

class Word(Label):
    pass
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.bind(texture_size=self.new_lable_size)
    #     self.size_hint = [None, None]
    #     self.padding = [0,0,10,0]

    # def new_lable_size(self, obj, value):
    #     # print(f'obj: {obj}')
    #     # print(f'value: {value}')
    #     self.size = value
    #     # print(f'self.size {self.size}')


class TranslatorApp(ScreenManager):
    translator_screen = ObjectProperty(None)
    input_screen = ObjectProperty(None)
    
    def convert_text(self, text):
        print(text)
        sentences = main7.ntlk_sentences(text=text)
        for sentenc in sentences:
            words = main7.words(sentenc)
            sentenc_view = Sentenc()
            for word in words:
                sentenc_view.add_word(Word(text=word))
            self.translator_screen.translator_area.add_widget(sentenc_view)
        self.current = self.translator_screen.name    

class TranslatorScreen(Screen):
    translator_area = ObjectProperty(None)
    pass

# class TranslatorScreenTranslatorArea()

class InputScreen(Screen):
    
    pass

class Sentenc(StackLayout):
    
    def add_word(self, word):
        self.add_widget(word)

class TestApp(App):

    def build(self):
        root = TranslatorApp()
        # root.add_widget(InputScreen())
        # root.add_widget(TranslatorScreen())
        # paragraph = Sentenc()
        # root = StackLayout(orientation='lr-tb')
        # l1 = SizedLabel(text='lable text1')
        # l2 = SizedLabel(text='lable text2')
        # l3 = SizedLabel(text='lable text3')
        # l4 = SizedLabel(text='lable text4')
        # l5 = SizedLabel(text='lable text5')

        # for i in range(100):
        #     paragraph.add_word(Word(text=f'lable text{i}'))

        # root.add_widget(paragraph)
        
        return root
    



if __name__ == '__main__':
    
    TestApp().run()
