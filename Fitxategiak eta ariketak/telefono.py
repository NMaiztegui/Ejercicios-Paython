import os

def main ():
    with open ("listin.txt", mode ="a+") as file :
        
        file.seek(0)
        try:
               egin = int(input('zer egin nahi dozu? 1-bezero baten telefono berria sartu 2-telefonoa kontsultatu 3-telefonoa ezabatu'))
        except ValueError:
               print('Sartutakoa ez da baliozkoa, saiatu berriro')
        else:
            while egin not in [1, 2, 3] :
                     print('sartutako emaitza ez da baliogarria, berriz erantzun')
                     egin = int(input('1-ezero baten telefono berria sartu 2-telefonoa kontsultatu 3-telefonoa ezabatu'))

        if egin==1:
                sartu_zenbakia(file)
        elif egin==2:
                kontsulta_zenbakia(file)
        elif egin==3:
                ezabatu_zenbakia(file)
               
                   
                    

          
        
               
         
        
            
def  kontsulta_zenbakia(file): 
   
   
   file.seek(0)
   # coger todas la lineas del fichero almacenarlas en un array
   print('Hauek dira gure bezeroak\n')
   all_bezero=file.readlines()
   bezero={}
   for line in all_bezero:
        #almacenar los separados en otra lista
        list_split =line.strip().split(',')  # Usar strip() para eliminar espacios y saltos de línea
        bezero[list_split[0]]=list_split[1]
        print(f"{list_split[0]}\n")

   
   kontsulta=str(input('Sartu kontsultatu nahi dozun bezeroaren izena')) 
   print(bezero.get(kontsulta)) #devuelve el valor correspondiente al key en este caso al nombre consultado
             


      
      



def ezabatu_zenbakia(file):
     file.seek(0)
     
     #mostrar todos los clientes
     print('Hauek dira gure bezeroak\n')
     all_bezero=file.readlines()
     bezero={}
     for line in all_bezero:
        #almacenar los separados en otra lista
        list_split =line.strip().split(',')  # Usar strip() para eliminar espacios y saltos de línea
        if len(list_split) == 2:  # Verificar que la línea tenga exactamente dos elementos
                bezero[list_split[0]] = list_split[1]
                print(f"{list_split[0]}\n")

     #konsultar el cliente a eliminar
     kontsulta=str(input('Sartu kontsultatu nahi dozun bezeroaren izena')) 
     lista_temporal=[]
    
     # Filtrar las líneas que no coincidan con el cliente a eliminar
     lista_temporal = [line for line in all_bezero if not line.startswith(kontsulta + ',')]
               
     
     with open ("listin.txt", mode ="w") as file :
       
          file.writelines(lista_temporal)



def sartu_zenbakia(file):
   izena = input('Sartu izena')
   telefonoa=input('Sartu telefono zenbakia')
   bezero= {
        "bezeroa": izena,
        "telf": telefonoa
   }
   file.write(f"{bezero['bezeroa']}, {bezero["telf"]}\n")




        
   
       

        
main()
    


    