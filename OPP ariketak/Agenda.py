#klase para crar objeto de cada contacto
class Kontaktua:
    def __init__(self, izena, telefonoa, posta_elektronikoa):
        self.izena=izena
        self.telefonoa=telefonoa
        self.post_elektro=posta_elektronikoa
# clase que construye una lista bacia el cual sera la agenda donde se van metiendo los contactos

class Agendaa:
    def __init__(self):
        self.kontaktuak=[] #Kontaktuak es = a una lista vacia

    def gehitu_kontaktua(self,Kontaktua):
        self.kontaktuak.append(Kontaktua) #sartutako kontaktu berria Agenda listan sartu
    
    def iprimatu_agenda(self):
        if not self.kontaktuak: #si la agenda de contactos esta vacia 
            print('Agenda hutsik dago, ez dago kontakturik barruan')
        else:
            print('Hauek dira agendan dituzun kontaktuak')
            for Kontaktua in self.kontaktuak:
                print(f'{Kontaktua}\n')
    
    def bilatu_kontaktua(self, izena):
        for Kontaktua in self.kontaktuak:
            if Kontaktua.izena.lower == izena.lower:
               return Kontaktua #usamos return para que despues la variable se pueda utilar en otros metdos, y de esta manera editar sus atributos
        return None # devolver vacio si no se ha encontrado el nobre    
    
    def editatu_kontaktua(self, izen):
        aurkitutako_kontaktua=self.bilatu_kontaktua(izen)

        if aurkitutako_kontaktua: #comprobar si la variable tiene conteido dentro
            print('Kontaktua aurkitu da, zer nahi duzu editatu?')
            print('***Editatzeko***\n')
            print('1-Izena\n 2-Telefonoa\n 3-Posta Elektronikoa\n')

            try:
                aukera=int(input('Aukeratzeko sartu aldaketaren zenbakia(1/2/3)\n'))
            except ValueError:
                print('Upss, zenaki bat sartu behar duzu aukeratzeko')
            
            if aukera==1:
                izen_berria=str(input('Sartu izen berria\n'))
                if any(char.isdigit() for char in izen_berria):
                    print('Upss, izenak ezin du zenbakirik izan')
                else:
                    aurkitutako_kontaktua.izena=izen_berria
                    print(f'Izena arrakastaz aldatu da:{aurkitutako_kontaktua.izena}')
            elif aukera==2:
               tel_berria=input('Sartu telefono zenbaki berria\n')
               aurkitutako_kontaktua.telefonoa=tel_berria
               print(f' Telefonoa arrakastaz aldatu da: {aurkitutako_kontaktua.telefonoa}')
            elif aukera==3:
                helbi_berria=input('Sartu posta elektroniko berria\n')
                aurkitutako_kontaktua.post_elektro=helbi_berria
                print(f' Telefonoa arrakastaz aldatu da: {aurkitutako_kontaktua.post_elektro}')
            else:
                print('Sartutako zenbakia ez da aukera baliiogarria')
        else:
            print('Kontaktua ez da aurkitua')

