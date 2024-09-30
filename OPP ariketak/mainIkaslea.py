import ikaslea

try:
    ikaslea1=ikaslea.ikaslea('Ane',5)
    ikaslea2=ikaslea.ikaslea('Iker',3)

    ikaslea1.mezua()
    ikaslea2.mezua()
except Exception as e:
    print("Ocurrió un error: ", e)