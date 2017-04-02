import wx
import glob
import wx.lib.scrolledpanel
from fileManipulation import fileManipulation
from EditWord import EditWindow

class EditListWord():
	"""docstring for EditListWord"""
	def __init__(self, parent):
		#Seting the scrollbar
		self.parent = parent
		self.panel = wx.lib.scrolledpanel.ScrolledPanel(parent,-1, pos=(0,0), size=(854,480))
		self.panel.SetupScrolling()
		self.bSizer = wx.BoxSizer(wx.VERTICAL)
		self.lblname = wx.StaticText(self.panel, label="Your list of words to edit:", pos=(10,0))

		self.backButton = wx.Button(self.panel, label = "Back", pos=(10,450))
		
		self.panel.Bind(wx.EVT_BUTTON, self.OnClickBack, self.backButton)

		if(len(glob.glob('*.txt'))>0):
			line = 10
			self.wordList = []
			for fileWord in glob.glob('*.txt'):
				strWord = fileWord[:fileWord.find('.txt')]
				self.wordList.append([strWord])

			self.wordList.sort()
			for index in range(0, len(self.wordList)):
				self.wordList[index].append(wx.Button(self.panel, label = self.wordList[index][0], pos=(400,line)))
				self.panel.Bind(wx.EVT_BUTTON, self.OnClickWord, self.wordList[index][1])
				self.bSizer.Add(self.wordList[index][1], 0, wx.CENTER,1)
				line +=30
			self.panel.SetSizer(self.bSizer)
		else: 
			dlg = wx.MessageDialog(self, "No word registered.","Warning", wx.OK)
			dlg.ShowModal()
			dlg.Destroy()
			self.Destroy()

	def OnClickWord(self,event):
		word = event.GetEventObject()
		strWord = word.GetLabelText()	
		file = fileManipulation(strWord)
		self.editPanel = EditWindow(self.parent,strWord,file.getDefinition())	
		self.panel.Destroy()
	
	def OnClickBack(self,event):
		self.panel.Destroy()
