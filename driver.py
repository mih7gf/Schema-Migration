import migrate_db as m
import parse_db as p


m.start_end_datetime_setup()
m.variable_info_setup()
m.Spatial_Reference_setup()#-
print "done sp_ref_setup"
m.CV_SiteType_setup()#-
print "CV_SiteType_setup"
m.Organization_setup()
print "done Org_setlup"
m.Unit_setup()
print "done unit_setup"
m.Method_setup()
print "done Method_setup"
p.parse_small_tables()
p.buffered_parse_large_table()

print "\nMigration Complete"

conn.close()
m.conn2.close()


