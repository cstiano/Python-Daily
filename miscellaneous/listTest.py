import wx
import glob
import wx.lib.scrolledpanel
#from fileManipulation import fileManipulation

class ListWordWindow(wx.Panel):
	def __init__ (self, parent):

		wx.Panel.__init__(self, parent)
		
		if(len(glob.glob('*.txt'))>0):
			line = 10
			self.wordList = []
			for fileWord in glob.glob('*.txt'):
				strWord = fileWord[:fileWord.find('.txt')]
				self.wordList.append([strWord])

			self.wordList.sort()
			for index in range(0, len(self.wordList)):
				self.wordList[index].append(wx.Button(self, label = self.wordList[index][0], pos=(10,line)))
				line +=30
		else: 
			dlg = wx.MessageDialog(self, "No word registered.","Warning", wx.OK)
			dlg.ShowModal()
			dlg.Destroy()
			self.Destroy()

		#line = 10
		#self.wordList = []	

		# self.list.append(wx.Button(self, label = "Save", pos=(760,450)))
		# self.Bind(wx.EVT_BUTTON, self.OnClickCancel, self.list[0])
		
		#self.saveButton = wx.Button(self, label = "Save", pos=(760,450))


		# self.Bind(wx.EVT_BUTTON, self.OnClickSave, self.saveButton)

		# self.cancelButton = wx.Button(self, label = "Cancel", pos=(10,450))
		
		# self.Bind(wx.EVT_BUTTON, self.OnClickCancel, self.cancelButton)

		# self.word = wx.StaticText(self, label="Your word:", pos=(20,20))

		# self.textWord = wx.TextCtrl(self, pos=(100,15), size=(650,-1))

		# self.definition = wx.StaticText(self, label = "Definition:", pos=(20, 60))

		# self.textDefinition = wx.TextCtrl(self, pos=(100,55), size=(650, 300), style=wx.TE_MULTILINE)

	#yes -> 5103 no -> 5104
	# def OnClickSave(self, event):
	# 	wordStr = self.textWord.GetValue()
	# 	defStr = self.textDefinition.GetValue()
	# 	regFile = fileManipulation(wordStr,defStr)
	# 	if (regFile.verify()):
	# 		dlg = wx.MessageDialog(self, "This world is already registered!\nDo you want to submit?","Warning", wx.YES_NO)
	# 		if(dlg.ShowModal() == 5103):
	# 			regFile.saveWord()
	# 			endDlg = wx.MessageDialog(self, "Your word was submitted","Submitted", wx.NO_DEFAULT)
	# 			endDlg.ShowModal()
	# 			endDlg.Destroy()
	# 			self.Destroy()
	# 		dlg.Destroy()

	def OnClickCancel(self,event):
		self.Destroy()		


app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "Hello World", size=(854,200))
# panel = ListWordWindow(frame)
# panel = wx.lib.scrolledpanel.ScrolledPanel(frame,-1)
# panel.SetupScrolling()
# button1 = wx.Button(panel,label="Button 1",pos=(0,50),size=(50,50))
# button2 = wx.Button(panel,label="Button 2",pos=(0,100), size=(50,50))
# button3 = wx.Button(panel,label="Button 3",pos=(0,150),size=(50,50))
# button4 = wx.Button(panel,label="Button 4",pos=(0,200), size=(50,50))
# button5 = wx.Button(panel,label="Button 5",pos=(0,250),size=(50,50))
# button6 = wx.Button(panel,label="Button 6",pos=(0,300), size=(50,50))
# button7 = wx.Button(panel,label="Button 7",pos=(0,350), size=(50,50))
# button8 = wx.Button(panel,label="Button 8",pos=(0,400), size=(50,50))

# bSizer = wx.BoxSizer( wx.VERTICAL )
# bSizer.Add( button1, 0, wx.ALL, 20 )
# bSizer.Add( button2, 0, wx.ALL, 20 )
# bSizer.Add( button3, 0, wx.ALL, 20 )
# bSizer.Add( button4, 0, wx.ALL, 20 )
# bSizer.Add( button5, 0, wx.ALL, 20 )
# bSizer.Add( button6, 0, wx.ALL, 20 )
# bSizer.Add( button7, 0, wx.ALL, 20 )
# bSizer.Add( button8, 0, wx.ALL, 20 )
# panel.SetSizer( bSizer )
frame.Show()
app.MainLoop()

# fruits = ['banana', 'apple', 'mango']
# num = [2,4,1]
# list = []
# for f in range(0,3):
# 	print f
# 	list.append([fruits[f],num[f]])

# list.sort()
# for i in range(0,3):
#  	print list[i]

# text = 'cris.txt'
# print text.find('.txt')
# print text[:text.find('.txt')]

# for file in glob.glob("*.txt"):
# 	print file[:file.find('.txt')]
# print len(glob.glob('*.txt'))
