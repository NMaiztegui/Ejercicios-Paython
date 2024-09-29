import pertsonak
izena=input('Sartu pertsonaren izena')
adina=int(input('Sartu pertsonaren adina'))

try:
    prson= pertsonak.pertsona(izena,adina)
except Exception as e:
    print("Ocurrió un error: ", e)

prson.datuak()
prson.adina_nagusia()