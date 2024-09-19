import os

def main ():
    with open ("listin.txt", mode ="a+") as file :
        
         file.seek(0)

        
        try:
          egin = int(input('zer egin nahi dozu? 1-bezero baten telefono berria sartu 2-telefonoa kontsultatu 3-telefonoa ezabatu'))
        except ValueError:
               print('Sartutakoa ez da baliozkoa, saiatu berriro')
        else:
                 while eginegin not in [1, 2, 3] :
                         print('sartutako emaitza ez da baliogarria, berriz erantzun')
                         egin = int(input('1-ezero baten telefono berria sartu 2-telefonoa kontsultatu 3-telefonoa ezabatu'))

        if egin==1:
                sartu_zenbakia(file)
        elif egin==2:
                kontsulta_zenbakia(file)
        elif egin==3:
                ezabatu_zenbakia(file)
               
                   
                    

          
        
               
         
        
            
def   kontsulta_zenbakia(file): 
   
   kontsulta=str(input('Sartu kontsultatu nahi dozun bezeroaren izena')) 
   file.seek(0)
# coger todas la lineas del fichero almacenarlas en un array
   all_bezero=file.readlines()
#comprobar todas las lineas, separarlas por coma 
   for line in all_bezero:
        #almacenar los separados en otra lista
        list_split = line.split(',')
#si coincide  devuelve
        if list_split[0]==kontsulta:
             print(list_split[1])


      
      



def ezabatu_zenbakia(file):
     kontsulta=str(input('Sartu kontsultatu nahi dozun bezeroaren izena')) 
        file.seek(0)
     all_bezero=file.readlines()
   
     
     #abrir el archivo de manera de reescribir,
     with open ("listin.txt", mode ="w") as file :
        for line in all_bezero:
          list_split = line.split(',')
     #si el bezero pedido coincide con alguno en la lista no vplver a escribir esa linea
        if list_split[0]!=kontsulta:
             file.write(f"{list_split[0]},{list_split[1]}\n")
             



def sartu_zenbakia(file):
   izena = input('Sartu izena')
   telefonoa=input('Sartu telefono zenbakia')
   bezero= {
        "bezeroa": izena,
        "telf": telefonoa
   }
   file.write(f"{bezero['bezeroa']}, {bezero["telf"]}\n")




        
   
       

        
main()
    


    