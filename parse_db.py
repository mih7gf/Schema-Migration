import sqlite3
from ODM1_datavalue_objects import *
import time

sqlite_file = '../hampt_rd_data.sqlite'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()	

tables = [ #[table_name, pk_column_name]
	['datavalues', 'ValueID'],
	['qualitycontrollevels', 'QCID'],
	['sites', 'SiteID'],
	['variables', 'VariableID']
]

def get_table_in_range(table_name, column_name, start, end):
	c.execute('SELECT * FROM {tn} WHERE {cn}>={st} AND {cn}<{en}'.format(tn=table_name, cn=column_name, st=start, en=end))
	all_rows = c.fetchall()
	return all_rows

def get_table_at_row(table_name, column_name, row):
	c.execute('SELECT * FROM {tn} WHERE {cn}=={ro}'.format(tn=table_name, cn=column_name, ro=row))
	one_row = c.fetchone()
	return Datavalue(one_row)
	

		#i = Datavalue(i)
		#print(i.Value, i.ValueID)
get_table_in_range('datavalues', 'ValueID', 20, 31)
x = get_table_at_row('datavalues', 'ValueID', 20)

print(x.ValueID)
conn.close()
exit()


###-----------------

def run():

	#start = time.time()
	
	def get_by_interval(num):
		list = []
		min = str(num-interval)
		max = str(num+1)
		
		for i in all_rows:
			x = Datavalue(i)
			#print x.row
			#print i
			list.append(x)
		#print "done"

	top = 21000000
	interval = 1000
	for i in range(2000000,top+1):
		if i%interval==0:
			print i-interval,"to",i
			get_by_interval(i)
	conn.close()
			

	#print "done"
	end = time.time()
	print end-start
for i in range(10):
	run()
# for l in list:
# 	print(l.row)

exit()

one_row = c.fetchone()
print(all_rows)
print(all_rows[0])
#all_rows[1]
#conn.close()
print("done")





dv = Datavalue(all_rows[0])
print(dv.row)
print('read done')
conn.close()