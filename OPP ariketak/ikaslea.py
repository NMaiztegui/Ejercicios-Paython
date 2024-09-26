class ikaslea:
    def __init__(self,izena,nota):
        self.izena = izena
        try:
            self.kalifikazioa = int(nota) #intenta validar nota como int, si es string  va dar error
        except ValueError:
            raise ValueError("Nota debe ser un número entero o una cadena que represente un número entero.")
    
        if 0 <= nota <= 10:
            self.kalifikazioa = nota
        else:
            raise ValueError("Kalifikazioa 0 eta 10 artean egon behar da")
    


    def mezua(self):
        if self.kalifikazioa >=5:
            print(f'{self.izena} gainditu du {self.kalifikazioa}-ko notarekin')
        elif self.kalifikazioa < 5:
              print(f'{self.izena} ez du gainditu  {self.kalifikazioa}-ko notarekin')

