def gehitu_ikaslea(kurtsorea,konexioa):
    #iaslearen datuak eskatu
    try:
        izena = input("Sartu ikaslearen izena")
        abizena = input("Sartu ikaslearen abizena")
        
        insert_ikaslea= "INSERT INTO ikasleak (  izena  , abizena) VALUES (%s, %s)"
        kurtsorea.execute(insert_ikaslea,(izena,abizena)) #pasar los datos como parametros

        konexioa.commit()

    except Exception as e:
    # Revertir los cambios si ocurre un error
        konexioa.rollback()
        print("Ocurrió un error: ", e)
    

def gehitu_ikasgaia (kurtsorea,konexioa):
    try:
     ikasgaia = input('Sartu ikasgaiaren izena')
     maila= input('Sartu ikasgairen maila: Hasiberriak,Ertaina edo Aurreratua')
     hizkuntza = input('Ze hizkuntzatan ematen da ikasgaia?')


     insert_ikasgia= "INSERT INTO ikasgaiak (  izena, maila, hizkuntza ) VALUES (%s, %s, %s)"
     kurtsorea.execute(insert_ikasgia,(ikasgaia,maila,hizkuntza)) #pasar los datos como parametros

     konexioa.commit()

    except Exception as e:
    # Revertir los cambios si ocurre un error
        konexioa.rollback()
        print("Ocurrió un error: ", e)

def nota_sartu (kurtsorea,konexioa):
    try:
        ikaslea = input('Sartu ikasleraen izena')
        ikasgaia = input('Sartu ikasgaia')
        oharra = input('Sartu oharra')
        nota= int(input('sartu ikaslearen nota'))

        #ikaslearen id-a eskuratu
        kurtsorea.execute(
            "Select ikasle_id From ikasleak where izena = %s",(ikaslea,)
        )
        print(kurtsorea.fetchone() )
        #kontsultaren emaitza eskuratzeko
        if kurtsorea.fetchone() is None:
            print('Ez da ikaslea aurkitu')
        else:
            print('ikaslea aurkitu da')
            ikaslea_id =kurtsorea.fetchone()
        
        #ikasgaiaren id-a eskuratu
        kurtsorea.execute(
            "Select ikasgai_id From ikasgaiak where izena = %s",(ikasgaia,)
        )
        print(kurtsorea.fetchone() )
        #kontsultaren emaitza eskuratzeko
        if kurtsorea.fetchone() is None:
            print('Ez da ikasgai aurkitu')
        else:
            print('ikasgaia aurkitu da')
            ikasgaia_id =kurtsorea.fetchone()
        
        #baloreak taulen notan sartu
        insert_notak ="INSERT INTO notak ( nota ,  oharra , ikasle_id , ikasgai_id ) VALUES (%s, %s, %s, %s)"
        kurtsorea.execute(insert_notak,(nota,oharra,ikaslea_id,ikasgaia_id)) #pasar los datos como parametros

    except Exception as e:
    # Revertir los cambios si ocurre un error
        konexioa.rollback()
        print("Ocurrió un error: ", e)


def nota_aldatu (kurtsorea,konexioa):
     nota = input('sartu nota')

def ezabatu_ikaslea (kurtsorea,konexioa):
    nota = input('sartu nota')
