# import sqlite3, csv
# from parse_db import *
# from migrate_db import *
# from ODM1_table_objects import *
# # from ODM2_table_objects import *
import parse_db as p

class Core_ProcessingLevel(object):
	ProcessingLevelID = 0
	ProcessingLevelCode = 0
	Definition = 'null'
	Explanation = 'null'
	def __init__(self, QCL):
		self.ProcessingLevelID = QCL.QCID
		self.ProcessingLevelCode = QCL.name
		# self.Definition = 
		self.Explanation = QCL.description


class SamplingFeature(object):
	SamplingFeatureID = 'null' #Not Null
	SamplingFeatureUUID = 'null' #Not Null
	SamplingFeatureTypeCV = 'null' #Not Null
	SamplingFeatureCode = 'null' #Not Null
	SamplingFeatureName = 'null'
	SamplingFeatureDescription = 'null'
	SamplingFeatureGeotypeCV = 'null'
	FeatureGeometry = 'null'
	FeatureGeometryWKT = 'null'
	Elevation_m = 'null'
	ElevationDatumCV = 'null'
	def __init__(self, site):
		self.SamplingFeatureID = site.SiteID #Not Null
		self.SamplingFeatureUUID = site.SiteID #Not Null
		self.SamplingFeatureTypeCV = 'Sensor Site'
		self.SamplingFeatureCode = site.SiteCode #Not Null
		



class SamplingFeatures_Site(object):
	SamplingFeatureID = 'null'
	SiteTypeCV = 'null'
	Latitude = 'null'
	Longitude = 'null'
	SpatialReferenceID = "null" #"WGS84"
	def __init__(self, Site):
		self.SamplingFeatureID = Site.SiteID
		self.SiteTypeCV = 'Sensor Site'
		self.Latitude = Site.Lat
		self.Longitude = Site.Lon
		self.SpatialReferenceID = 1

class SpatialReference(object):
	SpatialReferenceID = 'null' #Not Null
	SRSCode = 'null'
	SRSName = 'null' #Not Null
	SRSDescription = 'null'
	SRSLink = 'null'
	def __init__(self, pk, name):
		self.SpatialReferenceID = pk
		self.SRSCode = name
		self.SRSName = name

class SiteType(object):
	Term = 'null' #Not Null
	Name = 'null' #Not Null, PK
	Definition = 'null'
	Category = 'null'
	SourceVocabularyURI = 'null'
	def __init__(self, s):
		self.Term = s
		self.Name = s

####
class Core_Organization(object):
	OrganizationID = 'null' #Not Null
	OrganizationTypeCV = 'null' #Not Null
	OrganizationCode = 'null' #Not Null
	OrganizationName = 'null' #Not Null
	OrganizationDescription = 'null'
	OrganizationLink = 'null'
	ParentOrganizationID = 'null'
	def __init__(self, i, t, c, n):
		self.OrganizationID = i
		self.OrganizationTypeCV = t
		self.OrganizationCode = c
		self.OrganizationName = n



class Core_Variable(object):
	VariableID = 'null' #Not Null
	VariableTypeCV = 'null' #Not Null
	VariableCode = 'null' #Not Null
	VariableNameCV = 'null' #Not Null
	VariableDefinition = 'null'
	SpeciationDV = 'null'
	NoDataValue = 'null' #Not Null
	def __init__(self, var):
		self.VariableID = var.VariableID
		self.VariableTypeCV = 'Unknown'
		self.VariableCode = var.VariableCode
		self.VariableNameCV = var.VariableName
		self.VariableDefinition = var.VariableDescription
		self.SpeciationDV = 'Unknown'
		self.NoDataValue = 0
	
class Unit(object):
	UnitID = 'null' #Not Null
	UnitTypeCV = 'null' #Not Null
	UnitAbbreviation = 'null' #Not Null
	UnitName = 'null' #Not Null
	UnitLink = 'null' 
	def __init__(self, ID, ty, ab, name):
		self.UnitID = ID
		self.UnitTypeCV = ty
		self.UnitAbbreviation = ab
		self.UnitName = name
		self.UnitLink = "Unknown"

		
class Core_Method(object):
	MethodID = 'null' #Not Null
	MethodTypeCV = 'null' #Not Null
	MethodCode = 'null' #Not Null
	MethodName = 'null' #Not Null
	MethodDescription = 'null'
	MethodLink = 'null'
	OrganizationID = 'null'
	def __init__(self, ID):
		self.MethodID = ID
		self.MethodTypeCV = "Instrument deployment"
		self.MethodCode = ID
		self.MethodName = "raw QC level 0 data"
		self.MethodDescription = "raw QC level 0 data"
		self.MethodLink = "Unknown"
		self.OrganizationID = ID

####	
class Core_Action(object):
	ActionID = 'null' #Not Null
	ActionTypeCV = 'null' #Not Null
	MethodID = 'null' #Not Null
	BeginDateTime = 'null' #Not Null
	BeginDateTimeUTCOffset = 'null' #Not Null
	EndDateTime = 'null'
	EndDateTimeUTCOffset = 'null'
	ActionDescription = 'null'
	ActionFileLink = 'null'
	def __init__(self, site):
		self.ActionID = site.SiteID
		self.ActionTypeCV = "Observation"
		self.MethodID = method_id(site.SiteID)
		self.BeginDateTime = p.start_end[site.SiteID][1]
		self.BeginDateTimeUTCOffset = -5
		self.EndDateTime = p.start_end[site.SiteID][2]
		self.EndDateTimeUTCOffset = -5
def method_id(s):
	if(s==22): #WU
		return 3
	elif(s>=17 and s<=20):
		return 2 # NOAA
	elif(s<=22):
		return 1  # HRSD
	else:
		return 0 # else

class Core_FeatureAction(object):
	FeatureActionID = 'null'
	SamplingFeatureID = 'null'
	ActionID = 'null'
	def __init__(self,id):
		self.FeatureActionID = id
		self.SamplingFeatureID = id
		self.ActionID = id


class Core_Result(object):
	ResultID = 'null' #Not Null
	ResultUUID = 'null' #Not Null
	FeatureActionID = 'null' #Not Null
	ResultTypeCV = 'null' #Not Null
	VariableID = 'null' #Not Null
	UnitsID = 'null' #Not Null
	TaxonomicClassifierID = 'null'
	ProcessingLevelID = 'null' #Not Null
	ResultDateTime = 'null'
	ResultDateTimeUTCOffset = 'null'
	ValidDateTime = 'null'
	ValidDateTimeUTCOffset = 'null'
	StatusCV = 'null'
	SampledMedium = 'null' #Not Null
	ValueCount = 'null' #Not Null
	def __init__(self, dval):
		self.ResultID = dval.ValueID
		self.ResultUUID = dval.ValueID
		self.FeatureActionID = dval.SiteID
		self.ResultTypeCV = "Time Series Coverage"
		self.VariableID = dval.VariableID
		self.UnitsID = p.unit_id[p.variable_info[dval.VariableID][1]]
		# self.TaxonomicClassifierID = 
		self.ProcessingLevelID = ProcLevelID_check(dval.QCID)
		self.ResultDateTime = dval.Datetime
		self.ResultDateTimeUTCOffset = -5
		# self.ValidDateTime
		# self.ValidDateTimeUTCOffset
		# self.StatusCV
		self.SampledMedium = 'water'
		self.ValueCount = 1

def ProcLevelID_check(ID):
	if(ID==None):  return -1
	return ID

class Results_TimeSeriesResult(object):
	ResultID = 'null' #Not Null
	XLocation = 'null'
	XLocationUnitsID = 'null'
	YLocation = 'null'
	YLocationUnitsID = 'null'
	ZLocation = 'null'
	ZLocationUnitsID = 'null'
	SpatialReferenceID = 'null' #Not Null
	IntendedTimeSpacing = 'null'
	IntendedTimeSpacingUnitsID = 'null'
	AggregationStatisticCV = 'null'
	def __init__(self, dval):
		self.ResultID = dval.ValueID
		self.AggregationStatisticCV = 'Unknown'

class Results_TimeSeriesResultValue(object):
	ValueID = 'null' #Not Null
	ResultID = 'null' #Not Null
	DataValue = 'null' #Not Null
	ValueDateTime = 'null' #Not Null
	ValueDateTimeUTCOffset = 'null' #Not Null
	CensorCodeCV = 'null' #Not Null
	QualityCodeCV = 'null' #Not Null
	TimeAggregationInterval = 'null' #Not Null
	TimeAggregationIntervalUnitsID = 'null' #Not Null
	def __init__(self,dval):
		self.ValueID = dval.ValueID
		self.ResultID = dval.ValueID
		self.DataValue = Value_NotNull(dval.Value)
		self.ValueDateTime = dval.Datetime
		self.ValueDateTimeUTCOffset = -5
		self.CensorCodeCV = -1
		self.QualityCodeCV = -1
		self.TimeAggregationInterval = p.variable_info[dval.VariableID][2]
		self.TimeAggregationIntervalUnitsID = 5
def Value_NotNull(v):
	if(v==None):  return -1
	return v	