import mysql.connector
from hasieratzea import*
dbConnect = {
 'host': 'localhost',
 'user': 'root',
 'password': 'Admin123',
 'database': 'taulaksortu'
}
konexioa = mysql.connector.connect(**dbConnect)
kurtsorea = konexioa.cursor()



taulak_sortu(kurtsorea)