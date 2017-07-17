import sqlite3
from parse_db import *
import ODM2_table_objects as ODM2

# from parse_db import *
# from migrate_db import *
# from ODM1_table_objects import *
# from ODM2_table_objects import *


sqlite_file2 = '../ODM2_hampt_rd_data.sqlite'
conn2 = sqlite3.connect(sqlite_file2)
c2 = conn2.cursor()	


def migrate_datavalue(dval):
	migrate_Results(dval)
	migrate_TimeSeriesResults(dval)
	migrate_TimeSeriesResultValues(dval)
	# conn2.commit()
	return

def migrate_QCL(QCL):
	q = ODM2.Core_ProcessingLevel(QCL)
	c2.execute("INSERT INTO ProcessingLevels VALUES ({pid},'{cd}',{df},'{ex}')".format(pid=q.ProcessingLevelID, cd=q.ProcessingLevelCode, df=q.Definition, ex=q.Explanation))
	
	return

def migrate_site(site):
	s1 = ODM2.SamplingFeatures_Site(site)
	s2 = ODM2.SamplingFeature(site)
	c2.execute("INSERT INTO Sites VALUES ({sfid},'{cv}',{lt},'{ln}', {srid})".format(sfid=s1.SamplingFeatureID, cv=s1.SiteTypeCV, lt=s1.Latitude, ln=s1.Longitude, srid=s1.SpatialReferenceID))#-
	c2.execute("INSERT INTO SamplingFeatures VALUES ({id}, '{uid}', '{tp}', '{cd}', '{nm}', '{ds}', '{gt}', '{gm}', '{gmw}', '{em}', '{ed}')".format(id=s2.SamplingFeatureID, uid=s2.SamplingFeatureUUID, tp=s2.SamplingFeatureTypeCV, cd=s2.SamplingFeatureCode, nm=s2.SamplingFeatureName, ds=s2.SamplingFeatureDescription, gt=s2.FeatureGeometry, gm=s2.FeatureGeometry ,gmw=s2.FeatureGeometryWKT, em=s2.Elevation_m, ed=s2.ElevationDatumCV))
	conn2.commit()
	migrate_Action(site)
	migrate_FeatureAction(site.SiteID)
	return

def migrate_Action(site):
	a = ODM2.Core_Action(site)
	print a.ActionID,a.MethodID, a.BeginDateTime, a.EndDateTime
	c2.execute("INSERT INTO Actions Values ({id}, '{cv}', {mid}, '{bdt}', '{bos}', '{edt}', '{eod}', '{ad}', '{afl}')".format(id=a.ActionID, cv=a.ActionTypeCV, mid=a.MethodID, bdt=a.BeginDateTime, bos=a.BeginDateTimeUTCOffset, edt=a.EndDateTime, eod=a.EndDateTimeUTCOffset, ad=a.ActionDescription, afl=a.ActionFileLink))
	conn2.commit()
	print"migrate action completed"
	return

def migrate_FeatureAction(id):
	fa = ODM2.Core_FeatureAction(id)
	c2.execute("INSERT INTO FeatureActions Values ({fid}, {sfid}, {aid})".format(fid=fa.FeatureActionID, sfid=fa.SamplingFeatureID, aid=fa.ActionID))
	conn2.commit()
	print "migrate_FeatureAction complete"
	return

def migrate_Results(dval):
	cr = ODM2.Core_Result(dval)
	c2.execute("INSERT INTO Results VALUES ({rid}, '{ruid}', {fid}, '{rcv}', {vid}, {uid}, {tx}, {plid}, '{rdt}', {ruo}, '{vdt}', {vos}, '{scv}', '{smcv}', {vc})".format(rid=cr.ResultID, ruid=cr.ResultUUID, fid=cr.FeatureActionID, rcv=cr.ResultTypeCV, vid=cr.VariableID, uid=cr.UnitsID, tx=cr.TaxonomicClassifierID, plid=cr.ProcessingLevelID, rdt=cr.ResultDateTime, ruo=cr.ResultDateTimeUTCOffset, vdt=cr.ValidDateTime, vos=cr.ValidDateTimeUTCOffset, scv=cr.StatusCV, smcv=cr.SampledMedium, vc=cr.ValueCount))
	return

def migrate_TimeSeriesResults(dval):
	tsr = ODM2.Results_TimeSeriesResult(dval)
	c2.execute("INSERT INTO TimeSeriesResults VALUES ({rid}, {x}, {xid}, {y}, {yid}, {z}, {zid}, {sid}, {it}, {itid}, '{acv}')".format(rid=tsr.ResultID, x=tsr.XLocation, xid=tsr.XLocationUnitsID, y=tsr.YLocation, yid=tsr.YLocationUnitsID, z=tsr.ZLocation, zid=tsr.ZLocationUnitsID, sid=tsr.SpatialReferenceID, it=tsr.IntendedTimeSpacing, itid=tsr.IntendedTimeSpacingUnitsID, acv=tsr.AggregationStatisticCV))
	return

def migrate_TimeSeriesResultValues(dval):
	tr = ODM2.Results_TimeSeriesResultValue(dval)
	c2.execute("INSERT INTO TimeSeriesResultValues VALUES ({vid}, {rid}, {dv}, '{vdt}', {vos}, {ccv}, {qcv}, {tai}, {taid})".format(vid=tr.ValueID, rid=tr.ResultID, dv=tr.DataValue, vdt=tr.ValueDateTime, vos=tr.ValueDateTimeUTCOffset, ccv=tr.CensorCodeCV, qcv=tr.QualityCodeCV, tai=tr.TimeAggregationInterval, taid=tr.TimeAggregationIntervalUnitsID))
	return

def migrate_variable(var):
	v = ODM2.Core_Variable(var)
	c2.execute("INSERT INTO Variables VALUES ({id}, '{cv}', '{c}', '{n}', '{d}', '{s}', {ndv})".format(id=v.VariableID, cv=v.VariableTypeCV, c=v.VariableCode, n=v.VariableNameCV, d=v.VariableDefinition, s=v.SpeciationDV, ndv=v.NoDataValue))
	conn2.commit()
	return

def Spatial_Reference_setup():
	sr = ODM2.SpatialReference(1,"WGS84")
	c2.execute("INSERT INTO SpatialReferences VALUES ({id}, '{src}','{nm}', '{ds}','{lk}')".format(id=sr.SpatialReferenceID, src=sr.SRSCode, nm=sr.SRSName, ds=sr.SRSDescription, lk=sr.SRSLink))
	conn2.commit()
	print"spacial_ref_setup"
	return

def CV_SiteType_setup():
	cv = ODM2.SiteType('Sensor Site')
	c2.execute("INSERT INTO CV_SiteType VALUES ('{t}', '{n}','{d}', '{c}','{s}')".format(t=cv.Term, n=cv.Name, d=cv.Definition, c=cv.Category, s=cv.SourceVocabularyURI))
	conn2.commit()
	return

def Organization_setup():
	o1 = ODM2.Core_Organization(1, 'Unknown', '1', 'HRSD')
	o2 = ODM2.Core_Organization(2, 'Unknown', '2', 'NOAA')
	o3 = ODM2.Core_Organization(3, 'Unknown', '3', 'WU')
	orgs = [o1, o2, o3] 
	for org in orgs:
		c2.execute("INSERT INTO Organizations VALUES ({i}, '{t}','{c}', '{n}','{d}', '{l}', {p})".format(i=org.OrganizationID, t=org.OrganizationTypeCV, c=org.OrganizationCode, n=org.OrganizationName, d=org.OrganizationDescription, l=org.OrganizationLink, p=org.ParentOrganizationID))
	conn2.commit()
	return
def Unit_setup():
	u1 = ODM2.Unit(1, 'Length', 'in', 'inches')
	u2 = ODM2.Unit(2, 'Temperature', 'deg', 'degrees')
	u3 = ODM2.Unit(3, 'Speed', 'mph', 'miles per hour')
	u4 = ODM2.Unit(4, 'Length', 'ft', 'feet')
	u5 = ODM2.Unit(5, 'Time', 'sec', 'seconds')
	units = [u1, u2, u3, u4, u5]
	for unit in units:
		c2.execute("INSERT INTO Units VALUES ({id}, '{cv}', '{ab}', '{nm}', '{lk}')".format(id=unit.UnitID, cv=unit.UnitTypeCV, ab=unit.UnitAbbreviation, nm=unit.UnitAbbreviation, lk=unit.UnitLink))
	conn2.commit()

def Method_setup():
	m1 = ODM2.Core_Method(1)
	m2 = ODM2.Core_Method(2)
	m3 = ODM2.Core_Method(3)
	m4 = ODM2.Core_Method(4)
	methods = [m1, m2, m3, m4]
	for method in methods:
		c2.execute("INSERT INTO Methods VALUES ({id}, '{cv}', '{cd}', '{nm}', '{ds}', '{ln}', {org})".format(id=method.MethodID, cv=method.MethodTypeCV, cd=method.MethodCode, nm=method.MethodName, ds=method.MethodDescription, org=method.OrganizationID, ln=method.MethodLink))
	conn2.commit()

