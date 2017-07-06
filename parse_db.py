import sqlite3
from ODM1_datavalue_objects import *
import time

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
	QCL_rows = get_all_rows(tables[1][0])	
	for row in QCL_rows:
		QCL_objs.append(QualityControlLevel(row))
	print "QCL parsed..."
	
	site_rows = get_all_rows(tables[2][0])
	for row in site_rows:
		site_objs.append(Site(row))
	print "Sites parsed..."

	variable_rows = get_all_rows(tables[3][0])
	for row in variable_rows:
		variable_objs.append(Variable(row))
	print "Variables parsed..."

big_list = []
#### Still Working on this function.
def buffered_parse_large_table():
	num_rows = int(c.execute('SELECT * FROM {tn} ORDER BY ROWID DESC LIMIT 1'.format(tn=tables[0][0])).fetchone()[0])
	num_rows = 100
	buffer_size = 3
	for i in range(1, num_rows+1):
		if(i%buffer_size==0):
			start = i-buffer_size+1
			end = i
			if(i==buffer_size*(num_rows/buffer_size)):
				end = num_rows
			print "doing",start,"to",end
			list = []
			rows = get_rows_in_range(tables[0][0], tables[0][1], start, end+1)

			for row in rows:
				if(row!=None):
					list.append(Datavalue(row))
					print(row)
				else:
					print("None")
			print "littleList",len(list)
			big_list.append(list)
			print "bigList",len(big_list)
			print
			continue
		
	print "Datavalues parsed..."



dval_objs = []
QCL_objs = []
site_objs =[]
variable_objs = []

parse_small_tables()
buffered_parse_large_table()
print "Completed"
print "len_big_list",len(big_list)

sum = 0
for l in big_list:
	print "len",len(l)
	sum+=len(l)

print "sum",sum

conn.close()
