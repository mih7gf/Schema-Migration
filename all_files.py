import sqlite3, csv
sqlite_file = '../hampt_rd_data.sqlite'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()	

tables = [ #[table_name, pk_column_name]
	['datavalues', 'ValueID'], # 25427057
	['qualitycontrollevels', 'QCID'],
	['sites', 'SiteID'],
	['variables', 'VariableID']
]

start_end = []























###################DOM1
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


class QualityControlLevel(object):
	QCID = 0
	name = ""
	description = ""
	row = ""

	def __init__(self, row):
		self.QCID = row[0]
		self.name = row[1]
		self.description = row[2]
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
		self.SiteID = row[0]
		self.SiteCode = row[1]
		self.SiteName = row[2]
		self.SourceOrg = row[3]
		self.Lat = row[4] 
		self.Lon = row[5]
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
		self.VariableID = row[0]
		self.VariableCode = row[1]
		self.VariableName = row[2]
		self.VariableDescription = row[3]
		self.Units = row[4]
		self.TimeSupport = row[5]
		self.row = row










##################ODM2
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
		self.BeginDateTime = start_end[site.SiteID][1]
		self.BeginDateTimeUTCOffset = -5
		self.EndDateTime = start_end[site.SiteID][2]
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



























############# migrate_db
sqlite_file2 = '../ODM2_hampt_rd_data.sqlite'
conn2 = sqlite3.connect(sqlite_file2)
c2 = conn2.cursor()	


def migrate_datavalue(dval):
	
	return

def migrate_QCL(QCL):
	q = Core_ProcessingLevel(QCL)
	c2.execute("INSERT INTO ProcessingLevels VALUES ({pid},'{cd}',{df},'{ex}')".format(pid=q.ProcessingLevelID, cd=q.ProcessingLevelCode, df=q.Definition, ex=q.Explanation))
	
	return

def migrate_site(site):
	s1 = SamplingFeatures_Site(site)
	s2 = SamplingFeature(site)
	c2.execute("INSERT INTO Sites VALUES ({sfid},'{cv}',{lt},'{ln}', {srid})".format(sfid=s1.SamplingFeatureID, cv=s1.SiteTypeCV, lt=s1.Latitude, ln=s1.Longitude, srid=s1.SpatialReferenceID))#-
	c2.execute("INSERT INTO SamplingFeatures VALUES ({id}, '{uid}', '{tp}', '{cd}', '{nm}', '{ds}', '{gt}', '{gm}', '{gmw}', '{em}', '{ed}')".format(id=s2.SamplingFeatureID, uid=s2.SamplingFeatureUUID, tp=s2.SamplingFeatureTypeCV, cd=s2.SamplingFeatureCode, nm=s2.SamplingFeatureName, ds=s2.SamplingFeatureDescription, gt=s2.FeatureGeometry, gm=s2.FeatureGeometry ,gmw=s2.FeatureGeometryWKT, em=s2.Elevation_m, ed=s2.ElevationDatumCV))
	conn2.commit()
	migrate_Action(site)
	return

def migrate_Action(site):
	a = Core_Action(site)
	print a.ActionID,a.MethodID, a.BeginDateTime, a.EndDateTime
	c2.execute("INSERT INTO Actions Values ({id}, '{cv}', {mid}, '{bdt}', '{bos}', '{edt}', '{eod}', '{ad}', '{afl}')".format(id=a.ActionID, cv=a.ActionTypeCV, mid=a.MethodID, bdt=a.BeginDateTime, bos=a.BeginDateTimeUTCOffset, edt=a.EndDateTime, eod=a.EndDateTimeUTCOffset, ad=a.ActionDescription, afl=a.ActionFileLink))
	conn2.commit()
	print"migrate action completed"
	return

def migrate_variable(var):
	v = Core_Variable(var)
	c2.execute("INSERT INTO Variables VALUES ({id}, '{cv}', '{c}', '{n}', '{d}', '{s}', {ndv})".format(id=v.VariableID, cv=v.VariableTypeCV, c=v.VariableCode, n=v.VariableNameCV, d=v.VariableDefinition, s=v.SpeciationDV, ndv=v.NoDataValue))
	conn2.commit()
	return

def Spatial_Reference_setup():
	sr = SpatialReference(1,"WGS84")
	c2.execute("INSERT INTO SpatialReferences VALUES ({id}, '{src}','{nm}', '{ds}','{lk}')".format(id=sr.SpatialReferenceID, src=sr.SRSCode, nm=sr.SRSName, ds=sr.SRSDescription, lk=sr.SRSLink))
	conn2.commit()
	print"spacial_ref_setup"
	return

def CV_SiteType_setup():
	cv = SiteType('Sensor Site')
	c2.execute("INSERT INTO CV_SiteType VALUES ('{t}', '{n}','{d}', '{c}','{s}')".format(t=cv.Term, n=cv.Name, d=cv.Definition, c=cv.Category, s=cv.SourceVocabularyURI))
	conn2.commit()
	return

def Organization_setup():
	o1 = Core_Organization(1, 'Unknown', '1', 'HRSD')
	o2 = Core_Organization(2, 'Unknown', '2', 'NOAA')
	o3 = Core_Organization(3, 'Unknown', '3', 'WU')
	orgs = [o1, o2, o3] 
	for org in orgs:
		c2.execute("INSERT INTO Organizations VALUES ({i}, '{t}','{c}', '{n}','{d}', '{l}', {p})".format(i=org.OrganizationID, t=org.OrganizationTypeCV, c=org.OrganizationCode, n=org.OrganizationName, d=org.OrganizationDescription, l=org.OrganizationLink, p=org.ParentOrganizationID))
	conn2.commit()
	return
def Unit_setup():
	u1 = Unit(1, 'Length', 'in', 'inches')
	u2 = Unit(2, 'Temperature', 'deg', 'degrees')
	u3 = Unit(3, 'Speed', 'mph', 'miles per hour')
	u4 = Unit(4, 'Length', 'ft', 'feet')
	units = [u1, u2, u3, u4]
	for unit in units:
		c2.execute("INSERT INTO Units VALUES ({id}, '{cv}', '{ab}', '{nm}', '{lk}')".format(id=unit.UnitID, cv=unit.UnitTypeCV, ab=unit.UnitAbbreviation, nm=unit.UnitAbbreviation, lk=unit.UnitLink))
	conn2.commit()

def Method_setup():
	m1 = Core_Method(1)
	m2 = Core_Method(2)
	m3 = Core_Method(3)
	m4 = Core_Method(4)
	methods = [m1, m2, m3, m4]
	for method in methods:
		c2.execute("INSERT INTO Methods VALUES ({id}, '{cv}', '{cd}', '{nm}', '{ds}', '{ln}', {org})".format(id=method.MethodID, cv=method.MethodTypeCV, cd=method.MethodCode, nm=method.MethodName, ds=method.MethodDescription, org=method.OrganizationID, ln=method.MethodLink))
	conn2.commit()


























##########################################parse_db
def get_all_rows(table_name):
	c.execute('SELECT * FROM {tn}'.format(tn=table_name))
	all_rows = c.fetchall()
	return all_rows

def get_rows_in_range(table_name, column_name, start, end):
	c.execute('SELECT * FROM {tn} WHERE {cn}>={st} AND {cn}<{en}'.format(tn=table_name, cn=column_name, st=start, en=end))
	all_rows = c.fetchall()
	return all_rows

def get_row_by_pk(table_name, pk_name, row):
	c.execute('SELECT * FROM {tn} WHERE {cn}=={ro}'.format(tn=table_name, cn=pk_name, ro=row))
	one_row = c.fetchone()
	return one_row

def begin_datetime(siteID):
	c.execute("SELECT * FROM datavalues WHERE SiteID={id} ORDER BY Datetime LIMIT 1".format(id=siteID))
	start = c.fetchone()
	return start[2]

def end_datetime(siteID):
	c.execute("SELECT * FROM datavalues WHERE SiteID={id} ORDER BY Datetime DESC LIMIT 1".format(id=siteID))
	end = c.fetchone()
	return end[2]

def start_end_datetime_setup():
	start_end.append(['null','null','null'])
	with open('start_end.csv', 'rb') as csvfile:
		file = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in file:
			start_end.append(row)

def parse_small_tables():
	print "Fetching QCL..."
	QCL_rows = get_all_rows(tables[1][0])	
	print "Migrating QCL..."
	for row in QCL_rows:
		# QCL_objs.append(QualityControlLevel(row))
		q = QualityControlLevel(row)
		migrate_QCL(q) #-
	print "Done\n"
	
	print "Fetching Sites..."
	site_rows = get_all_rows(tables[2][0])
	print "Migrating Sites..."
	# Spatial_Reference_setup()#-
	# CV_SiteType_setup()#-
	for row in site_rows:
		# site_objs.append(Site(row))
		s = Site(row)
		migrate_site(s)#- 
	print "Done\n"

	print "Fetching Variables..."
	variable_rows = get_all_rows(tables[3][0])
	print "Migrating Variables..."
	for row in variable_rows:
		# variable_objs.append(Variable(row))
		v = Variable(row)
		migrate_variable(v)
	print "Done\n"
	conn2.commit()
	return


def buffered_parse_large_table():
	
	num_rows = int(c.execute('SELECT * FROM {tn} ORDER BY ROWID DESC LIMIT 1'.format(tn=tables[0][0])).fetchone()[0])
	# num_rows = 25000000
	buffer_size = 100000
	start = 1
	print "Fetching & Migrating Datavalues..."

	while start < num_rows+1:

		if start+buffer_size <= num_rows:
			end = start+buffer_size
		else:
			end = num_rows+1

		rows = get_rows_in_range(tables[0][0], tables[0][1], start, end)
		# dval_objs = []
		for row in rows:
			# dval_objs.append(Datavalue(row))
			migrate_datavalue(Datavalue(row))
		print start,"to",end,"("+str(100*end/num_rows)+"%) : Done"
		start = end

	print "Done"
	return


#####################################

# dval_objs = []
# QCL_objs = []
# site_objs = []
# variable_objs = []
start_end_datetime_setup()
Spatial_Reference_setup()#-
print "done sp_ref_setup"
CV_SiteType_setup()#-
print "CV_SiteType_setup"
Organization_setup()
print "done Org_setlup"
Unit_setup()
print "done unit_setup"
Method_setup()
print "done Method_setup"
parse_small_tables()
#- buffered_parse_large_table()

print "\nMigration Complete"
conn.close()
conn2.close()
