import sqlite3
from ODM1_table_objects import *
from ODM2_table_objects import *
from migrate_db import *

sqlite_file = '../hampt_rd_data.sqlite'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()	

tables = [ #[table_name, pk_column_name]
	['datavalues', 'ValueID'], # 25427057
	['qualitycontrollevels', 'QCID'],
	['sites', 'SiteID'],
	['variables', 'VariableID']
]


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
	c.execute ("SELECT * FROM datavalues WHERE SiteID={id} ORDER BY Datetime DESC LIMIT 1".format(id=siteID))
	end = c.fetchone()
	return end[2]

def parse_small_tables():
	print "Fetching QCL..."
	QCL_rows = get_all_rows(tables[1][0])	
	print "Migrating QCL..."
	for row in QCL_rows:
		# QCL_objs.append(QualityControlLevel(row))
		q = QualityControlLevel(row)
		#-migrate_QCL(q)
	print "Done\n"
	
	print "Fetching Sites..."
	site_rows = get_all_rows(tables[2][0])
	print "Migrating Sites..."
	#-Spatial_Reference_setup()
	#-CV_SiteType_setup()
	for row in site_rows:
		# site_objs.append(Site(row))
		s = Site(row)
		#- migrate_site(s)
		# if(s.SiteName==
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

# dval_objs = []
# QCL_objs = []
# site_objs = []
# variable_objs = []

#- Organization_setup()
#- Unit_setup()
#- Method_setup()
#- parse_small_tables()
#- buffered_parse_large_table()
# total = []
# pair = []
# # def start_end(sid):
# 	first=c.execute("SELECT * FROM  datavalues WHERE SiteID={id} LIMIT 1".format(id=sid))
# 	first = c.fetchone()
# 	firstID = first[0]

# 	nxt = c.execute("SELECT * FROM  datavalues WHERE SiteID={id} LIMIT 1".format(id=sid+1))
# 	nxt = c.fetchone()
# 	nxtID = nxt[0]
# 	last=c.execute("SELECT * FROM  datavalues WHERE ValueID={id}".format(id=nxtID-1))
# 	last = c.fetchone()
# 	if last==None:
# 		last=c.execute("SELECT * FROM  datavalues WHERE ValueID={id}".format(id=nxtID-2))
# 		last = c.fetchone()
# 	# start2 = c.execute("SELECT * FROM  datavalues WHERE SiteID={id} LIMIT 1".format(id=sid+1))
# 	# r1 = c.fetchone()
# 	# ID2 = int(r1[0])-1
# 	# end = c.execute("SELECT * FROM  datavalues WHERE SiteID={id} LIMIT 1".format(id=ID2))
# 	# end2 = c.fetchone()
# 	print sid
# 	print first
# 	print last
# 	# print end2
# 	print

# for i in range(1,23):
# 	print i,",",begin_datetime(i),',',end_datetime(i)
import json
import sys
import csv

# with open('start_end.csv', 'rb') as csvfile:
	# file = csv.reader(csvfile, delimiter=',', quotechar='|')
for row in csv.DictReader("start_end.csv"):
	# print row
	json.dump(row,sys.stdout)

 # with open('start_end.csv', 'rb') as csvfile:
# 	file = csv.reader(csvfile, delimiter=',', quotechar='|')
# 	for row in file:
# 		print row

print "\nMigration Complete"
conn.close()
conn2.close()