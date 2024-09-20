import mysql.connector
dbConnect = {
 'host': 'localhost',
 'user': 'root',
 'password': 'Admin123',
 'database': 'prueba'
}
konexioa = mysql.connector.connect(**dbConnect)
