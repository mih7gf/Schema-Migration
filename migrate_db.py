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
	s = SamplingFeatures_Sites(site)
	c2.execute("INSERT INTO Sites VALUES ({sfid},'{cv}',{lt},'{ln}', {srid})".format(sfid=s.SamplingFeatureID, cv=s.SiteTypeCV, lt=s.Latitude, ln=s.Longitude, ssrid=s.SpatialReferenceID))


	return

def migrate_variable(var):

	return


