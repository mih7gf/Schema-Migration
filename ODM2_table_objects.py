from ODM1_table_objects import *

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
	# def __init__(self):

class Core_Method(object):
	MethodID = 'null' #Not Null
	MethodTypeCV = 'null' #Not Null
	MethodCode = 'null' #Not Null
	MethodName = 'null' #Not Null
	MethodDescription = 'null'
	MethodLink = 'null'
	OrganizationID = 'null'
	# def __init__(self):
	
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
	# def __init__(self):
	
class Core_FeatureAction(object):
	FeatureActionID = 'null'
	SamplingFeatureID = 'null'
	ActionID = 'null'
	# def __init__(self):
	
class Core_Variable(object):
	VariableID = 'null' #Not Null
	VariableTypeCV = 'null' #Not Null
	VariableCode = 'null' #Not Null
	VariableNameCV = 'null' #Not Null
	VariableDefinition = 'null'
	SpeciationDV = 'null'
	NoDataValue = 'null' #Not Null
	# def __init__(self):
	
class Units(object):
	
	# def __init__(self):
	
class Results_TimeSeriesResultValue(object):
	ValueID = 'null' #Not Null
	ResultID = 'null' #Not Null
	DataValue = 'null' #Not Null
	ValueDateTime = 'null' #Not Null
	ValueDateTimeUTCOffset = 'null' #Not Null
	CensorCorCV = 'null' #Not Null
	TimeAggregationInterval = 'null' #Not Null
	TimeAggregationIntervalUnitsID = 'null' #Not Null
	# def __init__(self):
	
class Results_TimeSeriesResult(object):
	ResultID = 'null' #Not Null
	XLocation = 'null'
	XLocationUnitsID = 'null'
	YLocation = 'null'
	YLocationUnitsID = 'null'
	ZLocation = 'null'
	ZLocationUnitsID = 'null'
	SpatialReferenceID = 'null' #Not Null
	# def __init__(self):
	
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
	# def __init__(self):