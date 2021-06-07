import os, sys
import random
from kivy.resources import resource_add_path, resource_find
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image

Builder.load_file('arith_arranger.kv')


class Arithmetic(Widget):
	pass


class ArithmeticArrangerApp(App):
	def build(self):
		return Arithmetic()

if __name__ == '__main__':
	ArithmeticArrangerApp().run()