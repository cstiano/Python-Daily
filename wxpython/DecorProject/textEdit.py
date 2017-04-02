import os.path
import wx

class panelinha(wx.Panel):
	"""docstring for panelinha"""
	def __init__(self, parent, text, sPanel):
		self.parent = parent
		self.sPanel = sPanel
		wx.Panel.__init__(self, parent, -1, pos=(0,0), size=(854,480))
		self.word = wx.StaticText(self, label=text, pos=(20,20))
		self.saveButton = wx.Button(self, label = "Save", pos=(760,450))
		self.Bind(wx.EVT_BUTTON, self.OnClickSave, self.saveButton)

	def OnClickSave(self,event):
		self.Hide()
		# self.newpanel = panelinha(self.parent,"panel 2")
		if(self.sPanel!=0):
			self.sPanel.Show()


app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "Hello World", size=(854,480))
panel2 = panelinha(frame, "panel 2", 0)
panel2.Hide()
panel1 = panelinha(frame,"panel 1", panel2)
frame.Show()
app.MainLoop()

# while 1:
# 	str = raw_input("Input your word: ")
# 	filename = str+".txt"
# 	if(os.path.isfile(filename)):
# 		print "This word is already register"
# 		file = open(filename,"r")
# 		print "The definition is: " + file.read()
# 		file.close()
# 	else:
# 		file = open(filename,"w")
# 		definition = raw_input("Input your definition: ")
# 		file.write(definition)
# 		file.close()
# 		print "Your word is registed"