def gehiengo_absolutua (votos):
    total_de_votos = sum(votos.values())
    gehiengo_absolutua= total_de_votos // 2 
    found = False

    for alderdia , botoa in votos.items():
        if botoa >= gehiengo_absolutua:
            print(alderdia +' irabazi du gehiengo absolutua '+ str(botoa)+ ' botoekien')
            found = True

    if not found:
     print('inorrek ez du bozken gehiengo absolutua lortu')

    



bozkaketa ={
    "x": 25,
    "b": 42,
    "a" : 17,
    
}
gehiengo_absolutua(bozkaketa)