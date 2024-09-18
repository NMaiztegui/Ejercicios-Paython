import os

def main ():
    with open ("listin.txt", mode ="a+") as file :
        
        
        if egin.lower()=='a':
             sartu_zenbakia(file)
        elif egin.lower()=='b':
             tel_kontsultau(file)
        
        try:
          egin = str(input('zer egin nahi dozu? a)ezero baten telefono berria sartu b)telefonoa kontsultatu c)telefonoa ezabatu'))
        except ValueError:
               print('Sartutakoa ez da baliozkoa, saiatu berriro')
        finally:
               while egin.lower()!="a" or egin.upper()!="b" or :
                  print('sartutako emaitza ez da baliogarria, berriz erantzun')
                  erantzuna = str(input('Telefono zenbaki bat sartu nahi duzu? B/E'))
                if erantzuna()
          
        

       
            


        while True: 
           try: 
               erantzuna = str(input('Telefono zenbaki bat sartu nahi duzu? B/E'))
               break
           

           finally :
                if (erantzuna=="B"):
                        sartu_zenbakia(file)
      

               
         
        
            
        
        
        




def sartu_zenbakia(file):
   inf= []
   izena = input('Sartu izena')
   inf.append(izena)
   telefonoa=input('Sartu telefono zenbakia')
   inf.append(telefonoa)
   file.write( ";".join(inf) +"\n")




        
   
       

        
main()
    


    