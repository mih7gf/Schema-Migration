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
	s = SamplingFeatures_Site(site)
	s2 = SamplingFeature(site)
	#-c2.execute("INSERT INTO Sites VALUES ({sfid},'{cv}',{lt},'{ln}', {srid})".format(sfid=s.SamplingFeatureID, cv=s.SiteTypeCV, lt=s.Latitude, ln=s.Longitude, srid=s.SpatialReferenceID))
	c2.execute("INSERT INTO SamplingFeatures VALUES ({id}, '{uid}', '{tp}', '{cd}', '{nm}', '{ds}', '{gt}', '{gm}', '{gmw}', '{em}', '{ed}')".format(id=s2.SamplingFeatureID, uid=s2.SamplingFeatureUUID, tp=s2.SamplingFeatureTypeCV, cd=s2.SamplingFeatureCode, nm=s2.SamplingFeatureName, ds=s2.SamplingFeatureDescription, gt=s2.FeatureGeometry, gm=s2.FeatureGeometry ,gmw=s2.FeatureGeometryWKT, em=s2.Elevation_m, ed=s2.ElevationDatumCV))
	conn2.commit()
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