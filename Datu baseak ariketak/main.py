import mysql.connector

#importar funciones desde modulos
from hasieratze import*
from ezabatu import*
from aukerak import*

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

try:
    erantzuna=input('Aldaketarik egin nahi duzu datu basean? B/E')

    while erantzuna=='B':
        egin=int(input('Hemen dituzu egin ditzazkezun aldaketak:\n 1-Ikasle berri bat gehitu\n 2-Irakasgai berri bat gehitu\n 3-Nota berri bat sartu\n 4-Ikasle baten nota aldatu\n 5-Ikale bat erregistrotik ezabatu\n'))

        if egin==1:
            gehitu_ikaslea(kurtsorea,konexioa)
        elif egin==2:
            gehitu_ikasgaia (kurtsorea,konexioa)
        elif egin==3:
            nota_sartu (kurtsorea,konexioa)
        elif egin==4:
            nota_aldatu (kurtsorea,konexioa)
        elif egin==5:
            ezabatu_ikaslea (kurtsorea,konexioa)
        else:
            print('Sartutako erantzuna ez da baliogarria')
        
        erantzuna=input('Aldaketak egiten jarraitu nahi duzu? B/E')
   
    if erantzuna=='E':
        ezabatu=input('Nahi izanez gero tauletako datuak edo taulak ezabatzeko aukera duzu. Aurrera jarraitu nahi dezu? B/E')

        if ezabatu=='B':
            egin=int(input('Aukeratu:\n 1-Datuak ezabatu\n 2-Taulak ezabatu\n'))

            if egin==1:
                datuak_ezabatu (kurtsorea,konexioa)
            elif egin==2:
                tablak_ezabatu (kurtsorea,konexioa)
            else:
                print('Sartutako erantzuna ez da baliogarria')
        if ezabatu=='E':
            print('Programa amaitu da')
    
    kurtsorea.close()
    konexioa.close()
except Exception as e:
    # Revertir los cambios si ocurre un error
    konexioa.rollback()
    print("Ocurrió un error: ", e)