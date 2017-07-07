import sqlite3
from ODM1_datavalue_objects import *

sqlite_file = '../hampt_rd_data.sqlite'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()	

tables = [ #[table_name, pk_column_name]
	['datavalues', 'ValueID'], # 25427057
	['qualitycontrollevels', 'QCID'],
	['sites', 'SiteID'],
	['variables', 'VariableID']
]

dval_objs = []
QCL_objs = []
site_objs =[]
variable_objs = []

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
	print "Parsing QCL..."
	QCL_rows = get_all_rows(tables[1][0])	
	for row in QCL_rows:
		QCL_objs.append(QualityControlLevel(row))
	print "Done\n"
	
	print "Parsing Sites..."
	site_rows = get_all_rows(tables[2][0])
	for row in site_rows:
		site_objs.append(Site(row))
	print "Done\n"

	print "Parsing Variables..."
	variable_rows = get_all_rows(tables[3][0])
	for row in variable_rows:
		variable_objs.append(Variable(row))
	print "Done\n"
	return

def buffered_parse_large_table():
	print "Parsing Datavalues..."
	num_rows = int(c.execute('SELECT * FROM {tn} ORDER BY ROWID DESC LIMIT 1'.format(tn=tables[0][0])).fetchone()[0])
	num_rows = 5000023
	buffer_size = 1000000
	start = 1
	sum=0
	while start < num_rows+1:
		if start+buffer_size <= num_rows:
			end = start+buffer_size
		else:
			end = num_rows+1

		rows = get_rows_in_range(tables[0][0], tables[0][1], start, end)
		# len_rows = len(rows)	# exit()
	
		sum+=len(rows)
		dval_objs = []
		for r in rows:
			dval_objs.append(r)
		print start,"to",end,": Done"
		start = end

	print "Done"
	return

parse_small_tables()
buffered_parse_large_table()
print "\nParsing Complete"
conn.close()