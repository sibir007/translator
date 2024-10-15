
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics.texture import Texture
# from

class SizedLabel(Label):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(texture_size=self.new_size)
        self.size_hint = [None, None]

    def new_size(self, obj, value):
        print(f'obj: {obj}')
        print(f'value: {value}')
        self.size = value
        print(f'self.size {self.size}')

class TestApp(App):

    def build(self):
        roott = StackLayout(orientation='lr-tb')
        # l1 = SizedLabel(text='lable text1')
        # l2 = SizedLabel(text='lable text2')
        # l3 = SizedLabel(text='lable text3')
        # l4 = SizedLabel(text='lable text4')
        # l5 = SizedLabel(text='lable text5')

        for i in range(100):
            roott.add_widget(SizedLabel(text=f'lable text{i}'))

        return roott
    



if __name__ == '__main__':
    
    TestApp().run()
