
def gehiengo_absolutua(botoak):
    total_de_votos = sum(botoak.values())

    gehiengo = total_de_votos // 2 +1
    found = False

    for alderdia , botoa in botoak.items():
        if botoa >= gehiengo:
            print(alderdia +' irabazi du gehiengo absolutua '+ str(botoa)+ ' botoekien')
            found = True

    if not found:
     print('inorrek ez du bozken gehiengo absolutua lortu')


def bozkaketa ():
    boto_zerrenda= ['A','B','A']
    botoak = {}
    for boto in boto_zerrenda:
        botoak[boto] = boto_zerrenda.count(boto)
       
        
    
    gehiengo_absolutua(botoak)

bozkaketa()



