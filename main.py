from kivy.config import Config
Config.set('graphics','fullscreen','auto')

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivy.loader import Loader
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

from datetime import datetime

import os
import constant
import random

class RootLayout(Screen):
    pass

class MainApp(App):
    def build(self):
        self.title = 'Photo Frames'
        self.load_kv('main.kv')
        self.rootLayout = RootLayout()
        Clock.schedule_interval(self.refreshTime, 1.0)

        path = 'asset'
        self.files = []
        # r=root, d=directories, f = files
        for r, d, f in os.walk(path):
            for file in f:
                self.files.append(os.path.join(r, file))
        self.refreshImage(self)
        Clock.schedule_interval(self.refreshImage, 60.0)

        return self.rootLayout
    
    def refreshTime(self, dt):
        dt_now = datetime.now()
        self.rootLayout.ids.txtDate.text = constant.WEEKDAYS[dt_now.weekday()] + ", ngày " + dt_now.strftime("%d") + " tháng " + dt_now.strftime("%m") + " năm " + dt_now.strftime("%Y")
        self.rootLayout.ids.txtTime.text = dt_now.strftime("%I:%M:%S %p")

    def refreshImage(self, dt):
        if (self.files == None or len(self.files) == 0):
            return
        index = random.randint(0, len(self.files) - 1)
        path = self.files[index]
        proxyImage = Loader.image(path)
        proxyImage.bind(on_load=self._image_loaded)

    def _image_loaded(self, proxyImage):
        if proxyImage.image.texture:
            self.rootLayout.ids.imgMain.texture = proxyImage.image.texture

MainApp().run()
