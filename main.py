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
from kivy.clock import Clock

##############################
# MODULES
##############################
import os
from os import path
import random
import sys
import json
import time
import logging

try:
    from android.permissions import request_permissions, Permission
except:
    toast('Error 101')
try:
    request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE,Permission.CAMERA])
except:
    toast('Error 102')


if not os.path.exists('Pics'):
    os.mkdir('Pics')

if not os.path.exists('/storage/emulated/0/Pictures/Drive Cam'):
    os.makedirs('/storage/emulated/0/Pictures/Drive Cam')
    
from home import SendPage, CameraWin

SendPage()
CameraWin()
        
class MainApp(MDApp):
    nam = 'Drive Cam'
    def build(self):
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        
        self.set_bars_colors()
        
        sm=ScreenManager()       
        sc_lst = [
        CameraWin(name='camp'),
        SendPage(name='sendp')
        ]
        for sc in sc_lst:
            sm.add_widget(sc)
        return sm

    def set_bars_colors(self):
        set_bars_colors(self.theme_cls.primary_color,self.theme_cls.primary_color,"Light")

MainApp().run()
