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
		migrate_site(s)
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

parse_small_tables()
# buffered_parse_large_table()

print "\nMigration Complete"
conn.close()
conn2.close()