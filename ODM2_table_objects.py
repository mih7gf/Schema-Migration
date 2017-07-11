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
		# self.SamplingFeatureName = 'null'
		# self.SamplingFeatureDescription = 'null'
		# self.SamplingFeatureGeotypeCV = 'null'
		# self.FeatureGeometry = 'null'
		# self.FeatureGeometryWKT = 'null'
		# self.Elevation_m = 'null'
		# self.ElevationDatumCV = 'null'



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

