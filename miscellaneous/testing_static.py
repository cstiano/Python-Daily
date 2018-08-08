
class CenterBackRight:
	"""docstring for CenterBackRight"""
	@staticmethod
	def think(Agent):
		print Agent

class CenterBackLeft:
	"""docstring for CenterBackRight"""
	@staticmethod
	def think(Agent):
		print Agent

CenterBackRight.think("Ola")

roles_mapping = {"CenterBack_L": CenterBackLeft, "CenterBack_R": CenterBackRight}

eval('CenterBack_L',{'__builtins__':None},roles_maping).think("Dales")
eval('CenterBack_R',{'__builtins__':None},roles_maping).think("OOOOOOO")

roles_mapping = {
	CenterForward_C		
}
Goalie_C
CenterForward_C
SideBack_R
OffensiveHalf_R
SideForward_L
SideForward_R
SideBack_L
CenterBack_R
OffensiveHalf_L
SideForward_L
DefensiveHalf_C
CenterBack_R
SideForward_R
SideBack_R
CenterBack_L
SideBack_L
OffensiveHalf_R
OffensiveHalf_L
CenterForward_C
CenterBack_L
SideForward_R
roles_mapping = {"CenterBack_L": CenterBackLeft,"CenterBack_R": CenterBackRight,"SideBack_L": SideBackLeft,"SideBack_R": SideBackRight,"DefensiveHalf_C" : DefensiveHalf,"OffensiveHalf_L": OffensiveHalfLeft,"OffensiveHalf_R": OffensiveHalfRight,"SideForward_L": SideForwardLeft ,"SideForward_R": SideForwardRight,"CenterForward_C": CenterForward}