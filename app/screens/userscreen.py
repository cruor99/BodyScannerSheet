from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.properties import StringProperty
from kivy.clock import Clock

class UserScreen(Screen):
	user = StringProperty("")

	def on_enter(self):
		Clock.schedule_once(self.populateUserScans())

	def populateUserScans(self):
		self.ids.userBoxLayout.add_widget(MDLabel(text = 'hei'))

#	def __init__(self, **kwargs):
#		super(UserScreen, self).__init__(**kwargs)
