def datuak_ezabatu (kurtsorea,konexioa):
    try:
        kurtsorea.execute("DELETE FROM ikasleak")
        kurtsorea.execute("DELETE FROM ikasgaiak")
        kurtsorea.execute("DELETE FROM notak")
        
        konexioa.commit() #confrimar los datos
    except Exception as e:
    # Revertir los cambios si ocurre un error
        konexioa.rollback()
        print("Ocurrió un error: ", e)

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
