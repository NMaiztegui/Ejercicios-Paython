def datuak_ezabatu (kurtsorea,konexioa):
    try:
        kurtsorea.execute("TRUNCATE TABLE ikasleak")
        kurtsorea.execute("TRUNCATE TABLE ikasgaiak")
        kurtsorea.execute("TRUNCATE TABLE notak")
        
        konexioa.commit() #confrimar los datos
    except Exception as e:
    # Revertir los cambios si ocurre un error
        konexioa.rollback()
        print("Ocurrió un error: ", e)

    print('Datuak ezabatu dira')

def tablak_ezabatu (kurtsorea,konexioa):
    try:
        kurtsorea.execute("DROP TABLE ikasleak")
        kurtsorea.execute("DROP TABLE ikasgaiak")
        kurtsorea.execute("DROP TABLE notak")

        konexioa.commit()
    except Exception as e:
    # Revertir los cambios si ocurre un error
        konexioa.rollback()
        print("Ocurrió un error: ", e)
    
    print('Taulak ezabatu dira')
