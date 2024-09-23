import mysql.connector
from taulak_sortu import*
dbConnect = {
 'host': 'localhost',
 'user': 'root',
 'password': 'Admin123',
 'database': 'erosketakdb'
}
konexioa = mysql.connector.connect(**dbConnect)
kurtsorea = konexioa.cursor()

taulak_sortu(kurtsorea,konexioa)
datuak_sartu (kurtsorea,konexioa)