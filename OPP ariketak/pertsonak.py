class pertsona:
    def __init__(self,izena,adina): 
        
        self.setIzena(izena)
        self.setAdina(adina)
   #get metodoak
  
    def getAdina(self):
        return self.adina
    
    def getIzena(self):
        return self.izena

    #akatsak kontrolatzeko setter metodoak erabilia
    def setAdina(self,adina):
        if not isinstance(adina, int) or adina < 0:
             raise ValueError("Adina zenbaki oso bat izan behar da eta 0 baino handiagoa.")
        self.adina = adina

    def setIzena(self,izena):
        if not isinstance(izena,str) or len(izena) ==0:
            raise ValueError('Izena ezin da hutsik egon eta string bat iznan behar du')
        self.izena=izena

    #adin nagusikoa den konprobatzeko metodoa
    def adina_nagusia (self):
        if self.getAdina()>=18:
            print(f'{self.getIzena()} adin nagusikoa da, {self.getAdina()} urte bait ditu')
        else:
            print(f'{self.getIzena()} ez da adin nagusikoa, {self.getAdina()} urte dituelako')

    def datuak(self):
        print(f'Izena:{self.getIzena()} , Adina: {self.getAdina()}')