import mysql.connector
import pandas as pd

class data_toSQL:
	def __init__(self, airline, consulted, stopovers, price):
		self.airline = airline
		self.consulted = consulted
		self.stopovers = stopovers
		self.price = price
		self.db = mysql.connector.connect(
			host = 'localhost',
			user = 'root',
			password = '290198',
			database = 'flightdatabase'
		)
	def insert(self):
		db = self.db
		#Table: Info(Airline, Consulted, Stopovers, Price)
		mycursor = db.cursor()

		mycursor.execute("INSERT INTO Info (Airline, Consulted, Stopovers, Price) VALUES (%s,%s,%s,%s)",
			(self.airline, self.consulted, self.stopovers, self.price))
		db.commit()

	def mean_price(self):
		db = self.db

		mycursor = db.cursor()
		mycursor.execute("SELECT * FROM Info")	
		rows=mycursor.fetchall()
		df = pd.DataFrame(rows,columns = ['Airline','Date','Stopovers','Price'])
		return df['Price'].mean()

