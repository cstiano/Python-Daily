import wx
from AddWord import AddWindow
from EditListWord import EditListWord

class initialWindow(wx.Panel):
	"""docstring fos initialWindow"""
	def __init__(self, parent):
		wx.Panel.__init__(self, parent, -1, pos=(0,0), size=(854,480))

		self.parent = parent

		self.addButton = wx.Button(self, label = "Add Word", pos=(130,280))
		self.Bind(wx.EVT_BUTTON, self.OnClickAdd, self.addButton)
		
		self.editButton = wx.Button(self, label = "Edit Word", pos=(381,280))
		self.Bind(wx.EVT_BUTTON, self.OnClickEdit, self.editButton)

		self.studyButton = wx.Button(self, label = "Study", pos=(632,280))
		self.Bind(wx.EVT_BUTTON, self.OnClickStudy, self.studyButton)
	
	def OnClickAdd(self,event):
		self.addWin = AddWindow(self.parent)
	def OnClickEdit(self,event):
		self.editWin = EditListWord(self.parent)
	def OnClickStudy(self,event):
		print "Study"

app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "Hello World", size=(854,480))
test = initialWindow(frame)
frame.Show()
app.MainLoop()