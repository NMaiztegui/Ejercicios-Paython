import mysql.connector
dbConnect = {
 'host': 'localhost',
 'user': 'root',
 'password': 'Admin123',
 'database': 'erosketakdb'
}
konexioa = mysql.connector.connect(**dbConnect)
kurtsorea = konexioa.cursor()