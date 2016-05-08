from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.properties import StringProperty


class UserScreen(Screen):

	def populateUserScans(self):
		self.ids.scr_mngr.current = 'home' # replace 'home' with addScan when created
		self.ids.userBoxLayout.add_widget(MDLabel(text = 'hei'))

#	def __init__(self, **kwargs):
#		super(UserScreen, self).__init__(**kwargs)
