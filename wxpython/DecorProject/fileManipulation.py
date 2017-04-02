import os.path

class fileManipulation:
	def __init__ (self,filename,text=None):
		self.filename = filename + ".txt"
		self.text = text

	def verify(self):
		return os.path.isfile(self.filename)
	def saveWord(self):
		file = open(self.filename,"w")
		file.write(self.text)
		file.close()
	def getDefinition(self):
		file = open(self.filename,"r")
		ret = file.read()
		file.close()
		return ret

