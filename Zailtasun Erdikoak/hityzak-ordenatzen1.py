esasldia = input('Sartu testu bat')
eLarriz = esasldia.upper()
utsuneak_ezabatu = eLarriz.split(' ')
errepikapen_gabe = []
for x in utsuneak_ezabatu :
 if x not in errepikapen_gabe : 
  errepikapen_gabe.append(x)
print(errepikapen_gabe)
errepikapen_gabe.sort()

esaldi_berria = ' '. join(errepikapen_gabe)

print(esaldi_berria)
