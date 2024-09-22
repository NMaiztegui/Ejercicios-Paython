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

        emaitza =kurtsorea.fetchone()
       
        #kontsultaren emaitza eskuratzeko
        if emaitza[0] is None:
            print('Ez da ikaslea aurkitu')
        else:
            print('ikaslea aurkitu da')
            ikaslea_id=emaitza[0]
            print(ikaslea_id)
        
        #ikasgaiaren id-a eskuratu
        kurtsorea.execute(
            "Select ikasgai_id From ikasgaiak where izena = %s",(ikasgaia,)
        )
        emaitza =kurtsorea.fetchone()
       
        #kontsultaren emaitza eskuratzeko
        if  emaitza[0] is None:
            print('Ez da ikasgai aurkitu')
        else:
            print('ikasgaia aurkitu da')
            ikasgaia_id= emaitza[0]
            print(ikasgaia_id)
        
        #baloreak taulen notan sartu
        insert_notak ="INSERT INTO notak ( nota ,  oharra , ikasle_id , ikasgai_id ) VALUES (%s, %s, %s, %s)"
        kurtsorea.execute(insert_notak,(nota,oharra,ikaslea_id,ikasgaia_id)) #pasar los datos como parametros

        konexioa.commit()

    except Exception as e:
    # Revertir los cambios si ocurre un error
        konexioa.rollback()
        print("Ocurrió un error: ", e)


def nota_aldatu (kurtsorea,konexioa):
    try:
        kurtsorea.execute(
                "select notak.nota As nota, ikasleak.izena As ikaslea, ikasgaiak.izena As ikasgaia From notak, ikasgaiak, ikasleak where notak.ikasle_id=ikasleak.ikasle_id and notak.ikasgai_id=ikasgaiak.ikasgai_id"
            )
        nota_guztiak=kurtsorea.fetchall()

        if nota_guztiak is None:
            print('Ez dira notarik aurkitua')
        else:    
         print('Hauek dira erregistraturiko ikasleen notak')
         for ikasle in nota_guztiak:
            print(F'Ikaslea: {ikasle[0]}, Ikasgaia: {ikasle[1]}, Nota: {ikasle[2]}')
        

    except Exception as e:
    # Revertir los cambios si ocurre un error
        konexioa.rollback()
        print("Ocurrió un error: ", e)
    
    try:
        ikaslea=input('Ze ikasleren nota aldatu nahi duzu?')
        ikasgai= input('Ze ikasgaietakoa')
        nota=int(input('Zein da nota berria?'))

        kurtsorea.execute("""
            UPDATE notak 
            SET nota = %s 
            WHERE ikasle_id = (SELECT ikasle_id FROM ikasleak WHERE izena = %s) 
            AND ikasgai_id = (SELECT ikasgai_id FROM ikasgaiak WHERE izena = %s)
        """, (nota, ikaslea, ikasgai))

        konexioa.commit()
        print('Nota aldatu egin da')


        
    except Exception as e:
    # Revertir los cambios si ocurre un error
        konexioa.rollback()
        print("Ocurrió un error: ", e)



def ezabatu_ikaslea (kurtsorea,konexioa):
    try:
        kurtsorea.execute("Select* From ikasleak")
        ikasle_guztiak=kurtsorea.fetchall()
        print(ikasle_guztiak)

        print('Hauek dira gure ikasle guztiak')
        for ikasle in ikasle_guztiak:
            print(f'Iznea: {ikasle[1]}, Abizena: {ikasle[2]}')
        
        izena=input('Sart ezabatunahi duzun ikaslearen izena')

         # Primero, eliminar las notas asociadas al alumno
        kurtsorea.execute("DELETE FROM notak WHERE ikasle_id = (SELECT ikasle_id FROM ikasleak WHERE izena = %s)", (izena,))
        

        #ikaslea ezabatu
        kurtsorea.execute("DELETE FROM ikasleak WHERE izena = %s", (izena,))

        konexioa.commit()


    
    except Exception as e:
    # Revertir los cambios si ocurre un error
        konexioa.rollback()
        print("Ocurrió un error: ", e)

    

