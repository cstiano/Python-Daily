import wx
from fileManipulation import fileManipulation

class AddWindow(wx.Panel):
	def __init__ (self, parent):
		wx.Panel.__init__(self, parent, -1, pos=(0,0), size=(854,480))

		self.saveButton = wx.Button(self, label = "Save", pos=(760,450))

		self.Bind(wx.EVT_BUTTON, self.OnClickSave, self.saveButton)

		self.cancelButton = wx.Button(self, label = "Cancel", pos=(10,450))
		
		self.Bind(wx.EVT_BUTTON, self.OnClickCancel, self.cancelButton)

		self.word = wx.StaticText(self, label="Your word:", pos=(20,20))

		self.textWord = wx.TextCtrl(self, pos=(100,15), size=(650,-1))

		self.definition = wx.StaticText(self, label = "Definition:", pos=(20, 60))

		self.textDefinition = wx.TextCtrl(self, pos=(100,55), size=(650, 300), style=wx.TE_MULTILINE)

	#yes -> 5103 no -> 5104
	def OnClickSave(self, event):
		wordStr = self.textWord.GetValue()
		defStr = self.textDefinition.GetValue()
		regFile = fileManipulation(wordStr,defStr)
		if (regFile.verify()):
			dlg = wx.MessageDialog(self, "This world is already registered!\nDo you want to submit?","Warning", wx.YES_NO)
			if(dlg.ShowModal() == 5103):
				regFile.saveWord()
				endDlg = wx.MessageDialog(self, "Your word was submitted","Submitted", wx.NO_DEFAULT)
				endDlg.ShowModal()
				endDlg.Destroy()
				self.Destroy()
			dlg.Destroy()
		else:
			regFile.saveWord()
			endDlg = wx.MessageDialog(self, "Your word was submitted","Submitted", wx.NO_DEFAULT)
			endDlg.ShowModal()
			endDlg.Destroy()
			self.Destroy()

	def OnClickCancel(self,event):
		self.Destroy()		
