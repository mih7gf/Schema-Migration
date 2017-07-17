# import sqlite3, csv
# from parse_db import *
# from migrate_db import *
# # from ODM1_table_objects import *
# from ODM2_table_objects import *



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

