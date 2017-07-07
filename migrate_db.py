import sqlite3
from ODM1_table_objects import *


sqlite_file2 = '../ODM2_hampt_rd_data.sqlite'
conn2 = sqlite3.connect(sqlite_file2)
c2 = conn2.cursor()	


def migrate_datavalue(dval):
	
	return

def migrate_QCL(QCL):
	return

def migrate_site(site):

	return

def migrate_variable(var):

	return


conn.close()