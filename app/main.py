# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp

# kivymd
from kivymd.button import MDIconButton
from kivymd.theming import ThemeManager
from kivymd.navigationdrawer import NavigationDrawer

class BodyScanRoot(BoxLayout):
	pass

class BodyScanNavDrawer(NavigationDrawer):
	pass

class BodyScanApp(App):
	theme_cls = ThemeManager()
	nav_drawer = ObjectProperty()

	def build(self):
		rootwidget = BodyScanRoot()
		self.nav_drawer = BodyScanNavDrawer()
		self.theme_cls.primary_palette = "Blue"
		self.theme_cls.primary_hue = "500"


if __name__ == "__main__":
	BodyScanApp().run()
