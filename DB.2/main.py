import mysql.connector
from taulak_sortu import*
dbConnect = {
 'host': 'localhost',
 'user': 'root',
 'password': 'Admin123',
 'database': 'erosketakdba'
}
konexioa = mysql.connector.connect(**dbConnect)
kurtsorea = konexioa.cursor()

try:
    taulak_sortu(kurtsorea,konexioa)
    datuak_sartu (kurtsorea,konexioa)
except Exception as e:
         # Revertir los cambios si ocurre un error
        konexioa.rollback()
        print("Ocurrió un error: ", e)  

