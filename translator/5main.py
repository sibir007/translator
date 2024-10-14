'''
Camera Example
==============

This example demonstrates a simple use of the camera. It shows a window with
a buttoned labelled 'play' to turn the camera on and off. Note that
not finding a camera, perhaps because gstreamer is not installed, will
throw an exception during the kv language processing.

'''

# Uncomment these lines to see all the messages
# from kivy.logger import Logger
# import logging
# Logger.setLevel(logging.TRACE)

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import time
Builder.load_string('''
<AppController>:
    orientation: 'vertical'

    # camera: camera_id
    
    Camera:
        id: camera
        resolution: (640, 480)
        play: False
    ToggleButton:
        id: bn_play
        text: 'Play'
        on_press: root.play()
        size_hint_y: None
        height: '48dp'
    Button:
        id: bn_capture
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()
''')


class AppController(BoxLayout):
    
    def play(self):
        self.ids['camera'].play = not self.ids['camera'].play
    
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")


class TestCamera(App):

    def build(self):
        return AppController()


TestCamera().run()
