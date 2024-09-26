from ikaslea import*

try:
    ikaslea1=ikaslea('Ane',-1)
    ikaslea2=ikaslea('Iker',3)

    ikaslea1.mezua()
    ikaslea2.mezua()
except Exception as e:
    print("Ocurrió un error: ", e)