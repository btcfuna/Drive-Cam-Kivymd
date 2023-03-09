##############################
# KIVY MAIN APP CLASSES
##############################
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.lang import Builder
from kivymd.utils.set_bars_colors import set_bars_colors
from kivy.core.window import Window
from kivy.core.audio import SoundLoader

##############################
# KIVYMD WIDGETS 
##############################
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDIconButton,MDFlatButton,MDRaisedButton,MDRectangleFlatIconButton
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.card import MDCard
from kivy.properties import DictProperty
from kivymd.uix.dialog import MDDialog
from kivymd.toast import toast
from kivymd.utils import asynckivy as ak
from kivy.core.audio import SoundLoader
from kivymd.uix.filemanager import MDFileManager
from kivy.base import EventLoop

import os 
from os import path
import sys
import time
from datetime import datetime
import shutil
import logging

name = ''

class SendPage(Screen):
    def hook_keyboard(self, window, key, *largs):
        if key == 27:
            self.manager.current = 'camp'
            return True
            
    def enter(self):
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)
        self.ids.pic.source = name
        
    def save(self):
        try:
            img = name.replace('Pics/','')
            shutil.copy(name, f'/storage/emulated/0/Pictures/Drive Cam/{img}')
            from kvdroid.tools import share_file
            share_file(f'/storage/emulated/0/Pictures/Drive Cam/{img}', title='Share your file', chooser=True, app_package=None,call_playstore=False, error_msg="application unavailable")
        except:
            toast('Error 102')
        
    def camera(self):
        self.manager.current = 'camp'
        
class TimerDia(BoxLayout):
    pass
    
class CameraWin(Screen):
    def enter(self):
        try:
            for file in os.listdir('Pics'):
                try:
                    os.remove(f"Pics/{file}")
                except:
                    toast('Unable to clear earlier pictures')
        except:
            toast('Unable to clear earlier pictures')
            
    time_dia = None
    def timer(self):
        if self.time_dia == None:
            ccls = TimerDia()
            self.time_dia = MDDialog(
                title="Timer",
                type='custom',
                width=Window.width-100,
                content_cls=ccls,
                buttons=[
                    MDFlatButton(text="CANCEL",on_release= self.cancel),
                    MDRaisedButton(text="Capture",on_release= lambda *args: self.tcap(ccls ,*args))]
                )
        else:
            pass
        self.time_dia.open()
        
    def cancel(self,obj):
        self.time_dia.dismiss() 
        
    def tcap(self, ccls, obj):
        textfield = ccls.ids.sval
        val = textfield._get_text()
        val = str(val).split('.')[0]
        val = int(val)
        if val > 20:
            toast('Max Value allowed is 20')
        else:
            self.time_dia.dismiss() 
            async def do():
                n = 0
                for x in range(val):
                    n = n + 1
                    self.ids.time.text = str(n)
                    await ak.sleep(1)
                self.capture()
            ak.start(do())
    
    def capture(self):
        global name
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        try:
            SoundLoader.load('cam_cap.mp3').play()
        except:
            toast("Captured")
        try:
            camera.export_to_png(f"Pics/IMG_{timestr}.png")
            name = f"Pics/IMG_{timestr}.png"
            self.manager.current = 'sendp'
        except:
            toast("Unable to save captured images")
        
    def flip(self):
        try:
            self.ids.camera.index = 1
        except:
            toast('Selfi Camera Not Allowed')
    
    def home(self):
        self.manager.current = 'homep'