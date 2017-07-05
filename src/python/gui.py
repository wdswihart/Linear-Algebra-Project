# Gui represents a GUI object, for a Linear Algebra Project on fractal compression,
# using Python 2.7.
#
# William Swihart, Nick Phillips
# University of Central Arkansas
# Summer 2017

import sys
import os
import ctypes # Used to get screen resolution, to calc frame size
import wx # wxPython 3.0 amd-64 (made for Python 2.7)

frameWidth = ctypes.windll.user32.GetSystemMetrics(0) / 1.5 # Frame width will be 1/1.5 screen width,
frameHeight = ctypes.windll.user32.GetSystemMetrics(1) / 1.5 # 	and height will be 1/1.5 screen height

class Gui(wx.Frame):
	# INITIALIZERS
	
	def initUI(self):
		self.CreateStatusBar()
		
		# Add the menu bar.
		menuBar = wx.MenuBar()
		
		# 	Add the File menu.
		fileMenu = wx.Menu()
		exitItem = fileMenu.Append(wx.ID_EXIT, 'Exit', 'Exit to Desktop')
		self.Bind(wx.EVT_MENU, self.onExit, exitItem) # Event binding for 'Exit to Desktop' File menu item.
		menuBar.Append(fileMenu, 'File')
		
		
		# 	Add the Help menu.
		helpMenu = wx.Menu()
		aboutItem = helpMenu.Append(wx.ID_ABOUT, 'About', 'About this program')
		self.Bind(wx.EVT_MENU, self.onAbout, aboutItem) # Event binding for 'About' File menu item.
		menuBar.Append(helpMenu, 'Help')
		
		# 	Add other menus (?).
		#TO-DO
		
		self.SetMenuBar(menuBar)
		
		# Add a container panel and horizontal box sizer.
		container = wx.Panel(self)
		hbox = wx.BoxSizer(wx.HORIZONTAL)
		
		# Add the image view in a panel and vertical box sizer.
		
		#TO-DO
		
		# Add the buttons in another panel and vertical box sizer.
		buttonPanel = wx.Panel(self)
		buttonVBox = wx.BoxSizer(wx.VERTICAL)
		
		self.testButton = wx.Button(buttonPanel, -1, 'TEST')
		self.testButton.Bind(wx.EVT_BUTTON, self.onPress)
		buttonVBox.Add(self.testButton, 0, wx.ALIGN_CENTER)
		
		hbox.Add(buttonVBox, 0, wx.ALIGN_CENTER)
		
		# Set the size and orientation, and show the GUI.
		self.SetSize((frameWidth, frameHeight))
		self.Centre()
		self.Show(True)
		
	def _init_(self, parent, title):
		# super()
		wx.Frame._init_(self, parent, title=title, size=(frameWidth,frameHeight))
		
	# METHODS
	
	# onAbout is the behavior associated with the 'About' File menu option.
	# 	IN: self, event
	#	OUT: void
	def onAbout(self, evt):
		dlg = wx.MessageDialog(self, 'A fractal compression demonstration', 'About LA&M Project')
		dlg.ShowModal()
		dlg.Destroy()
		
	# onPress is the handler for button presses
	# 	IN: self, event
	# 	OUT: void
	def onPress(self, evt):
		print 'Label = ', evt.GetEventObject().GetLabel()
	
	# onQuit is the behavior associated with the 'Exit to Desktop' File menu option.
	# 	IN: self, event
	# 	OUT: void
	def onExit(self, evt):
		self.Close(True)
		
app = wx.App(False)
sys.stdout.write('Initializing GUI... ')
gui = Gui(None, wx.ID_ANY, 'LA&M Project')
gui.initUI()
print 'Done!'
print 'Running main loop...'
app.MainLoop()
print 'Done! Exiting now...'
