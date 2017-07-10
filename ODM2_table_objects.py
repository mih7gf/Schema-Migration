from ODM1_table_objects import *

class Core.ProcessingLevels(object):
	ProcessingLevelID = 0
	ProcessingLevelCode = 0
	Definition = null
	Explanation = null
	
	def __init__(self, QCL):
		self.ProcessingLevelID = QCL.QCID
		self.ProcessingLevelCode = QCL.name
		# self.Definition = 
		self.Explanation = QCL.description
		



