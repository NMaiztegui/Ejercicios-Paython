def batuketa(zen1,zen2):
    try:
        #si al hacer la suma uno de los valores es una cadena de texto va a dar error
        emaitza= zen1+zen2
    except TabError:
        print('Akatsa:Datu mota baliogabea')
        
    
    print(emaitza)

def kenketa(zen1,zen2):
    try:
        #si al hacer la suma uno de los valores es una cadena de texto va a dar error
        emaitza= zen1-zen2
    except TabError:
        print('Akatsa:Datu mota baliogabea')
        
    
    print(emaitza)

def biderketa(zen1,zen2):
    try:
        #si al hacer la suma uno de los valores es una cadena de texto va a dar error
        emaitza= zen1*zen2
    except TabError:
        print('Akatsa:Datu mota baliogabea')
        
    
    print(emaitza)

def zatiketa(zen1,zen2):
    try:
        #si al hacer la suma uno de los valores es una cadena de texto va a dar error
        emaitza= zen1/zen2
    except ZeroDivisionError:
        print('Akatsa:Zenbakia ezin da zeroz zatitu')
        
    
    print(emaitza)