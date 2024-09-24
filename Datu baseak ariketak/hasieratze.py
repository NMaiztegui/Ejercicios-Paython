def taulak_sortu(kurtsorea,konexioa):
  try:
    mysql_ikasleak= "CREATE TABLE IF NOT EXISTS ikasleak( ikasle_id int NOT NULL AUTO_INCREMENT,  izena text NOT NULL,  abizena text NOT NULL, PRIMARY KEY(ikasle_id))"
    kurtsorea.execute(mysql_ikasleak)

    mysql_ikasgaiak= "CREATE TABLE IF NOT EXISTS ikasgaiak( ikasgai_id int NOT NULL AUTO_INCREMENT,  izena text NOT NULL,  maila text NOT NULL, hizkuntza text NOT NULL,  PRIMARY KEY(ikasgai_id))"
    kurtsorea.execute(mysql_ikasgaiak)

    mysql_notak= "CREATE TABLE IF NOT EXISTS notak( nota int NOT NULL,  oharra text NOT NULL, ikasle_id int NOT NULL, ikasgai_id int NOT NULL, FOREIGN KEY (ikasgai_id) REFERENCES ikasgaiak(ikasgai_id), FOREIGN KEY (ikasle_id) REFERENCES ikasleak(ikasle_id)) "
    kurtsorea.execute(mysql_notak)

    #comfirmar los cabios
    konexioa.commit()
  except Exception as e:
    # Revertir los cambios si ocurre un error
    konexioa.rollback()
    print("Ocurrió un error: ", e)

  print('Taulak sortta daude')

def datuak_hasieratu(kurtsorea,konexioa):
  try:
     
    #preparar las los datos que se van a insertar
    insert_ikasleak= "INSERT INTO ikasleak (  izena  , abizena) VALUES (%s, %s)"
    insert_ikasgiak= "INSERT INTO ikasgaiak (  izena, maila, hizkuntza ) VALUES (%s, %s, %s)"
    insert_notak ="INSERT INTO notak ( nota ,  oharra , ikasle_id , ikasgai_id ) VALUES (%s, %s, %s, %s)"
    #datuak
    ikaslea_datuak = [ ("Jon","Alberdi"), ("Naroa","Muriilo"), ("Maddi","Beraza"), ("Jone","Monedero"), ("Malen","Esparza")]
    ikasgaiak_datuak=[('Matematikak', 'Hasiberriak', 'Euskara'), ('Historia', 'Ertaina', 'Euskara'), ('Fisika', 'Aurreratua', 'Gaztelania'), ( 'Filosofia', 'Hasiberriak', 'Euskara'), ( 'Ingelesa', 'Aurreratua', 'Ingelesa'), ( 'Kimika', 'Ertaina', 'Gaztelania') ]
    notak_datuak= [  (9, 'lan oona', 5, 3),  (5, 'hobetu behar', 4, 4), (4, 'azterketa errepikatuu behar', 3, 2)]

    #comprobar si las tablas tienen contenido

    kurtsorea.execute("SELECT COUNT(*) FROM ikasleak") #e utiliza para contar el número total de filas en la tabla, 
    if kurtsorea.fetchone()[0] == 0: #si la tabla esta vacia el resultado de filas deberia ser 0
        kurtsorea.executemany(insert_ikasleak, ikaslea_datuak) # insertar los datos en la tabla si no hay contenido de antes
        print("Datos insertados en la tabla ikasleak.")
    else:
      print("la tabla ikasleak ya tiene datos")

    kurtsorea.execute("SELECT COUNT(*) FROM ikasgaiak")
    if kurtsorea.fetchone()[0] == 0:
      kurtsorea.executemany(insert_ikasgiak,ikasgaiak_datuak)
      print("Datos insertados en la tabla ikasgaiak.")
    else:
      print("la tabla ikasgaiak ya tiene datos")
    
    kurtsorea.execute("SELECT COUNT(*) FROM notak")
    if kurtsorea.fetchone()[0] == 0:
      kurtsorea.executemany(insert_notak,notak_datuak)
      print("Datos insertados en la tabla notak.")
    else:
      print("la tabla notak ya tiene datos")

    
    
    
    #comfirmar los cabios
    konexioa.commit()
  except Exception as e:
    # Revertir los cambios si ocurre un error
    konexioa.rollback()
    print("Ocurrió un error: ", e)

  