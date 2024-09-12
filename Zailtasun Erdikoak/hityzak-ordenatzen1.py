esasldia = input('Sartu testu bat')
# upper() transforma los cracteres en miuscula de una cadena en mayusclas
eLarriz = esasldia.upper()
# slplit() divide la cadena dependiendo de la codición establecida y mete lo mete en um array
utsuneak_ezabatu = eLarriz.split(' ')
errepikapen_gabe = []
# bucle para miarar los elementos que estan dentro de la lista de utsuneak_ezabatu
for x in utsuneak_ezabatu :
 # si el elemento no esta en la nueva lista vacia que hemos creado lo mete en ella con appen() añade el elemento al final de la lista; de manera que si ya está de antes, lo descarta
 if x not in errepikapen_gabe : 
  errepikapen_gabe.append(x)
print(errepikapen_gabe)
#sort () ordena el array
errepikapen_gabe.sort()
# join() junat los elementos del array en foma de string , poneindo un espacio entre los elementos

esaldi_berria = ' '. join(errepikapen_gabe)

print(esaldi_berria)
