#!/usr/bin/python
# -*- coding: utf-8 -*-
import bcrypt

from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp

# kivymd
from kivymd.button import MDIconButton
from kivymd.theming import ThemeManager
from kivymd.navigationdrawer import NavigationDrawer
from kivymd.card import MDCard
from kivymd.label import MDLabel
from kivymd.dialog import MDDialog
from kivymd.textfields import SingleLineTextField

from models import *
from screens import *
from models.models import Users, Friend_List, Scan, db



class BodyScanRoot(BoxLayout):
	username = StringProperty("")
	rights = StringProperty("")

	def login(self, username, password):
		user = db.query(Users).filter_by(user_name = username).first()
		print user
		if bcrypt.hashpw(password.encode('UTF_8'), user.user_password) == user.user_password:
			self.updateUserInfo(username, 'Coach')
			self.ids.scr_mngr.current = 'home'

	def updateUserInfo(self, username, rights):
		self.username = username
		self.rights = rights

	def getUserInfo(self):
		return [app]

	def goToUserScreen(self, username):
		self.updateUserInfo(username, )

	def register(self, email, name, password):
		db.add(Users(user_email=email, user_name=name, user_password=password))
		db.commit()

class FriendTextField(SingleLineTextField):

	def __init__(self, **kwargs):
		super(FriendTextField, self).__init__(**kwargs)
		self.hint_text = "Username"

class FriendBoxLayout(BoxLayout):

	def __init__(self, **kwargs):
		super(FriendBoxLayout, self).__init__(**kwargs)
		self.orientation = 'vertical'

class AddUserContent(BoxLayout):
	selectRights = 'Friend'
	menu_items = ListProperty()
	selectRightsButton = ObjectProperty(None)

	def __init__(self, **kwargs):
		super(AddUserContent, self).__init__(**kwargs)
		self.menu_items = [
			{'viewclass': 'MDMenuItem',
			'text': 'Friend',
			'on_release': self.setSelectFriend},
			{'viewclass': 'MDMenuItem',
			'text': 'Coach',
			'on_release': self.setSelectCoach}
		]

	def setSelectFriend(self):
		self.selectRights = 'Friend'
		self.selectRightsButton.text = self.selectRights

	def setSelectCoach(self):
		self.selectRights = 'Coach'
		self.selectRightsButton.text = self.selectRights

class BodyScanNavDrawer(NavigationDrawer):
	pass

class BodyScanApp(App):
	theme_cls = ThemeManager()
	nav_drawer = ObjectProperty()
	username = StringProperty("")
	rights = StringProperty("")

	def showAddUserdialog(self):
		content = AddUserContent()
		self.dialog = MDDialog(title="Add Friend/Coach",
								content=content,
								size_hint=(.8, None),
								height=dp(200),
								auto_dismiss=False)
		self.dialog.add_action_button("Dismiss",
										action=lambda
										*x: self.dialog.dismiss())
		self.dialog.open()

	def build(self):
		self.nav_drawer = BodyScanNavDrawer()
		self.theme_cls.primary_palette = "Blue"
		self.theme_cls.primary_hue = "500"

if __name__ == "__main__":
	BodyScanApp().run()
