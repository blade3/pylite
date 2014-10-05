import sqlite3

#Intract with sqlite3 in python as simple as it can be.
class Simplite:

	#first argument is name of database that store in same name file on disk
	def __init__(self,db_name):	
		self.db_name = db_name
		self.db = sqlite3.connect(db_name)


	#Add table
	#first argument is table name.
	#other arguments have to be labled names equal to data type.for example title="text" or id="int"
	def add_table(self,table_name,**columns):

		self.cols = ""

		for col_name,col_type in columns.items():
			self.cols += col_name+" "+col_type+","
		self.cols = self.cols[0:len(self.cols)-1]

		self.db.execute("CREATE TABLE IF NOT EXISTS {}({})".format(table_name,self.cols))


	#insert data
	#first argument is table name
	#other arguments have to be a list of args of table column.
	def insert(self,table_name,*data):
		self.data = ""
		for value in data:
			self.data += '"'+value+'"'+','
		self.data = self.data[0:len(self.data)-1]

		self.db.execute("INSERT INTO {} values({})".format(table_name,self.data))
		self.db.commit()


	#remove items
	#first argument is table name
	#second argument is condition
	def remove(self,table_name,where="1"):
		self.where = where
		self.db.execute("DELETE FROM {} WHERE {}".format(table_name,self.where))
		self.db.commit()


	#get items from db
	#first argument is table name
	#second argument is condition
	def get_items(self,table_name,where=1):
		if(table_name!=1) :
			self.where = where
			self.items = self.db.execute("SELECT * FROM {} WHERE {}".format(table_name,self.where))
			self.db.commit()
			return list(self.items)
		else :
			return {}

	#return list of tables
	def get_tables(self):
		self.tables = self.db.execute("SELECT name FROM sqlite_master")
		return list(self.tables)

	#close database connection
	def close_connection(self):
		self.db.close()