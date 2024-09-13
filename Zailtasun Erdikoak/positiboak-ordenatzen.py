def positiboak_ordenatu(zerrenda):
    zerrenda_ordenatua=[]
    for zenbaki in zerrenda: 
        if zenbaki > 0:
           zerrenda_ordenatua.append(zenbaki)
           zerrenda_ordenatua.sort()
    #     else:
    #         zerrenda_ordenatua[zenbaki] = zenbaki

    print (zerrenda_ordenatua)



def zerrenda():
    gure_zerrenda = [6, 3, -2, 5, -8, 2, -2]

    positiboak_ordenatu(gure_zerrenda)

zerrenda()