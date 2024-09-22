import mysql.connector

#importar funciones desde modulos
from hasieratze import*
from ezabatu import*

dbConnect = {
 'host': 'localhost',
 'user': 'root',
 'password': 'Admin123',
 'database': 'taulaksortu'
}
konexioa = mysql.connector.connect(**dbConnect)
kurtsorea = konexioa.cursor()


try:
    taulak_sortu(kurtsorea,konexioa)
    datuak_hasieratu(kurtsorea,konexioa)
except Exception as e:
    # Revertir los cambios si ocurre un error
    konexioa.rollback()
    print("Ocurrió un error: ", e)