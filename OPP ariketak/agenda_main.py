import Agenda
def main():
    # Crear la instancia de la Agenda
    mi_agenda = Agenda.Agendaa()
    while True:
        print('***ZURE AGENDA***')
        print('Ongi etrorri zure agendara, zer egin nahi dud?')
        print('1-Kontaktu berria sartu\n 2-Agenda listatu\n 3-Bilatu kontaktua\n 4-Editatu kontaktua\n 5-Atera')
        try:
            aukera=int(input('Aukeratzeko sartu aldaketaren zenbakia(1/2/3/4)\n'))
        except ValueError:
            print('Upss, zenaki bat sartu behar duzu aukeratzeko')
        
        if aukera==1:
            izena=input('Sartu izena\n')
            tel=input('Sartu telefono zenbakia\n')
            post=input('Sartu posta eolektronikoa\n')

            kontaktu_berria=Agenda.Kontaktua(izena,tel,post)
            mi_agenda.gehitu_kontaktua(kontaktu_berria)
        elif aukera==2:
           mi_agenda.iprimatu_agenda()
        elif aukera==3:
            izena=input('Sartu bilatu nahi duzun kontaktuaren izena')
            aurkitutako_kontaktua=mi_agenda.bilatu_kontaktua(izena)
            if aurkitutako_kontaktua: #comprobar si ay contenido dentro de la variable
                print(f'Izena: {aurkitutako_kontaktua.izena} Telefonoa: {aurkitutako_kontaktua.telefonoa} Posta Elektronikoa: {aurkitutako_kontaktua.post_elektro}')
            else:
                print('Ez da aurkitu kontaktua')
        elif aukera==4:
            izena=input('Sartu editatu nahi duzun kontaktuaren izena\n')
            mi_agenda.editatu_kontaktua(izena)
        elif aukera==5:
            break
        else:
            print('Sartutako zenbakia ez da aukera baliiogarria')



main()