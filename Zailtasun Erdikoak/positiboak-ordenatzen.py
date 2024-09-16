def positiboak_ordenatu(zerrenda):
    zerrenda_ordenatua=[]
    for zenbaki in zerrenda: 
        if zenbaki > 0:
           zerrenda_ordenatua.append(zenbaki)
           zerrenda_ordenatua.sort()
   
# iter()  convierte un iterable en un iterador. 
    positiboak= iter(zerrenda_ordenatua)
    emaitza =[]
  
# next() Función integrada que se utiliza para devolver el siguiente elemento de un iterador. 
    for  zenbaki in zerrenda: 
        if zenbaki > 0:
           emaitza.append(next(positiboak))
        else:
            emaitza.append(zenbaki)
    print (emaitza)



def zerrenda():
    gure_zerrenda = [6, 3, -2, 5, -8, 2, -2]

    positiboak_ordenatu(gure_zerrenda)

zerrenda()