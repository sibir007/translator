from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.button import Button
from kivy.input.shape import ShapeRect

class MyPaintWidget(Widget):
    def on_touch_down(self, touch):
        print(f'touch.profile: {touch.profile}')
        print(f'touch.button: {touch.button}')
        if 'multitouch_sim' in touch.profile:
            print(f'touch.multitouch_sim: {touch.multitouch_sim}')
        if touch.is_double_tap:
            print('Touch is a double tap !')
            print(' - interval is', touch.double_tap_time)
            print(' - distance between previous is', touch.double_tap_distance)
        if isinstance(touch.shape, ShapeRect):
            print('My touch have a rectangle shape of size',
                (touch.shape.width, touch.shape.height))
        if touch.is_triple_tap:
            print('Touch is a triple tap !')
            print(' - interval is', touch.triple_tap_time)
            print(' - distance between previous is', touch.triple_tap_distance)
        with self.canvas:
            color = (random(), 1, 1)
            Color(*color, mode='hsv')
            d = 30.
            Ellipse(pos=(touch.x - d/2, touch.y - d/2), size=(d,d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))


    # def on_touch_up(self, touch):
    #     print(touch)
    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

class MyPaintApp(App):
    def build(self):
        parent = Widget()
        self.painter = MyPaintWidget()
        clearbutton = Button(text='Clear')
        clearbutton.bind(on_release=self.clear_canvase)
        parent.add_widget(self.painter)
        parent.add_widget(clearbutton)
        return parent
    
    def clear_canvase(self, obj):
        print('def clear_canvase(self):')
        self.painter.canvas.clear()
    
if __name__ == '__main__':
    MyPaintApp().run()