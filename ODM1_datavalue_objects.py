class Datavalue(object):
	ValueID = 0
	Value = 0
	Datetime = ""
	VariableID = 0
	SiteID = 0
	QCID = 0
	row = ""
	
	def __init__(self, row):
		self.ValueID = row[0]
		self.Value = row[1]
		self.Datetime = row[2]
		self.VariableID = row[3]
		self.SiteID = row[4]
		self.QCID = row[5]
		self.row = row

# def new_datavalue(row):
# 	datavalue = Datavalue(row)
# 	return datavalue

class QualityControlLevel(object):
	QCID = 0
	name = ""
	description = ""
	row = ""

	def __init__(self, row):
		self.QCID = QCID
		self.name = name
		self.description = description
		self.row = row

class Site(object):
	SiteID = 0
	SiteCode = ""
	SiteName = ""
	SourceOrg = ""
	Lat = 0.0
	Lon = 0.0
	row = ""

	def __init__(self, row):
		self.SiteID = SiteID
		self.SiteCode = SiteCode
		self.SiteName = SiteName
		self.SourceOrg = SourceOrg
		self.Lat = Lat 
		self.Lon = Lon
		self.row = row

class Variable(object):
	VariableID = 0
	VariableCode = ""
	VariableName = ""
	VariableDescription = ""
	Units = ""
	TimeSupport = 0.0
	row = ""

	def __init__(self, row):
		self.VariableID = VariableID
		self.VariableCode = VariableCode
		self.VariableName = VariableName
		self.VariableDescription = VariableDescription
		self.Units = Units
		self.TimeSupport = TimeSupport
		self.row = row

