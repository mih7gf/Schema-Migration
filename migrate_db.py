import sqlite3
from ODM1_table_objects import *
from ODM2_table_objects import *

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
	# s3 = FeatureAction(site)
	c2.execute("INSERT INTO Sites VALUES ({sfid},'{cv}',{lt},'{ln}', {srid})".format(sfid=s1.SamplingFeatureID, cv=s1.SiteTypeCV, lt=s1.Latitude, ln=s1.Longitude, srid=s1.SpatialReferenceID))
	c2.execute("INSERT INTO SamplingFeatures VALUES ({id}, '{uid}', '{tp}', '{cd}', '{nm}', '{ds}', '{gt}', '{gm}', '{gmw}', '{em}', '{ed}')".format(id=s2.SamplingFeatureID, uid=s2.SamplingFeatureUUID, tp=s2.SamplingFeatureTypeCV, cd=s2.SamplingFeatureCode, nm=s2.SamplingFeatureName, ds=s2.SamplingFeatureDescription, gt=s2.FeatureGeometry, gm=s2.FeatureGeometry ,gmw=s2.FeatureGeometryWKT, em=s2.Elevation_m, ed=s2.ElevationDatumCV))
	migrate_Action(site)
	migrate_FeatureAction()

	c2.execute("INSERT INTO Actions VALUES ()"format())
	c2.execute("INSERT INTO FeatureActions VALUES ()"format())
	conn2.commit()
	return

def migrate_variable(var):
	v = Core_Variable(var)
	c2.execute("INSERT INTO Variables VALUES ({id}, '{cv}', '{c}', '{n}', '{d}', '{s}', {ndv})".format(id=v.VariableID, cv=v.VariableTypeCV, c=v.VariableCode, n=v.VariableNameCV, d=v.VariableDefinition, s=v.SpeciationDV, ndv=v.NoDataValue))
	conn2.commit()
	return

def migrate_Action():
	a = Core_Action()

	conn2.commit()
	return

def migrate_FeatureAction():
	fa = Core_FeatureAction()

	conn2.commit()
	return

def Spatial_Reference_setup():
	sr = SpatialReference(1,"WGS84")
	c2.execute("INSERT INTO SpatialReferences VALUES ({id}, '{src}','{nm}', '{ds}','{lk}')".format(id=sr.SpatialReferenceID, src=sr.SRSCode, nm=sr.SRSName, ds=sr.SRSDescription, lk=sr.SRSLink))
	conn2.commit()
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
		c2.execute("INSERT INTO Units VALUES ({id})".format(id=unit.UnitID))
	conn2.commit()

def Method_setup():
	m1 = Core_Method(1)
	m2 = Core_Method(2)
	m3 = Core_Method(3)
	# m4 = Core_Method(4)
	methods = [m1, m2, m3]
	for method in methods:
		c2.execute("INSERT INTO Methods VALUES ({id}, '{cv}', '{cd}', '{nm}', '{ds}', '{ln}', {org})".format(id=method.MethodID, cv=method.MethodTypeCV, cd=method.MethodCode, nm=method.MethodName, ds=method.MethodDescription, org=method.OrganizationID, ln=method.MethodLink))
	conn2.commit()
	# "raw QC level 0 data"


# SELECT * FROM  datavalues WHERE SiteID=2 LIMIT 1;
# SELECT * FROM  datavalues WHERE ValueID=1;