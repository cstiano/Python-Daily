from math import sqrt
from math import pow

class VectorImp:
	vectorCount = 0
	def __init__ (self, x, y):
		self.x = x
		self.y = y
		VectorImp.vectorCount += 1

	def __del__ (self):
		class_name = self.__class__.__name__
		VectorImp.vectorCount -= 1
		#print class_name, "destroyed"
	
	def vMod (self):
		return sqrt(pow(self.x,2)+pow(self.y,2))

	def vCount (self):
		return VectorImp.vectorCount

	def __str__ (self):
		return 'Vector (%f, %f)' % (self.x, self.y)

	def __add__ (self, other):
		return VectorImp (self.x + other.x, self.y + other.y)

	def __sub__ (self, other):
		return VectorImp (self.x - other.x, self.y - other.y)

	def __mul__ (self, other):
		return VectorImp (self.x * other.x, self.y * other.y)

	def __div__ (self, other):
		if(other.x != 0 and other.y != 0):
			return VectorImp (self.x/other.x, self.y/other.y)
		else:
			print "Invalid operation in : ((%f / %f),(%f / %f))" % (self.x,other.x,self.y,other.y)
			return VectorImp(0,0)



