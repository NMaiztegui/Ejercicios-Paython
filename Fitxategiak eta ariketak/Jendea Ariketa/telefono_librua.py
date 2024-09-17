import os

def main ():
    with open ("listin.txt", mode ="a+") as file :
        erantzuna = input('Telefono zenbaki bat sartu nahi duzu? B/E')
        if (erantzuna=="B"):
             sartu_zenbakia(file)
        




def sartu_zenbakia(file):
   inf= []
   while True:
    try :
            izena = str(input('Sartu iznea'))
            telefonoa= int(input('Sartu telefono zenbakia'))
    except ValueError:
            print('Sartutako ez da zuzena, berriz sartu')
    else : 
         inf.append(izena,telefonoa)
        
         file.write( ";".join(inf))

    


    