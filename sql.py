import sqlite3

with sqlite3.connect("flabs.db") as connection:
	c = connection.cursor()
	#c.execute("""DROP TABLE anode_check""")
	c.execute("""CREATE TABLE anode_check(id PRIMARY KEY, pin INTEGER, current NUMERIC(5,3), fault TEXT)""")
	c.execute('INSERT INTO anode_check VALUES(1, 2,4.56,Null)')
	c.execute('INSERT INTO anode_check VALUES(2, 3,2.56,Null)')