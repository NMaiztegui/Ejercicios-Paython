def taulak_sortu(kurtsorea,konexioa):
    try:

        mysql_cliente= "CREATE TABLE IF NOT EXISTS cliente( cliente_id int NOT NULL AUTO_INCREMENT,  nombre text NOT NULL,  apellidos text NOT NULL,empresa text NOT NULL, puesto text NOT NULL, CP varchar(50) DEFAULT '20600', provincia varchar(50) DEFAULT 'Guipuzkoa',telefono text NOT NULL, fechaNacimiento DATE, PRIMARY KEY(cliente_id))"
        kurtsorea.execute(mysql_cliente)

        mysql_articulo= "CREATE TABLE IF NOT EXISTS articulo( articulo_id int NOT NULL AUTO_INCREMENT,  izena text NOT NULL,  descripcion text NOT NULL, precio_unidad DECIMAL(10, 2)NOT NULL, unidad_stock int NOT NULL, stock_seguridad int NOT NULL, img text,  PRIMARY KEY(articulo_id))"
        kurtsorea.execute(mysql_articulo)

        mysql_compras= "CREATE TABLE IF NOT EXISTS compras( cliente_id int NOT NULL,  articulo_id int NOT NULL, fecha DATE NOT NULL,unidades INT NOT NULL, FOREIGN KEY (cliente_id) REFERENCES cliente(cliente_id), FOREIGN KEY (articulo_id) REFERENCES articulo(articulo_id),PRIMARY KEY(cliente_id,articulo_id)) "
        kurtsorea.execute(mysql_compras)

        #comfirmar los cabios
        konexioa.commit()
    except Exception as e:
         # Revertir los cambios si ocurre un error
        konexioa.rollback()
        print("Ocurrió un error: ", e)

def datuak_sartu (kurtsorea,konexioa):
    try:
        #preparar las tablas para insertar datos
        insert_cliente= "INSERT INTO cliente(nombre,apellidos,empresa,puesto,CP,provincia,telefono,fechaNacimiento) VALUES (%s, %s,%s, %s,%s, %s,%s,%s) "
        insert_articulo="INSERT INTO articulo(izena ,  descripcion , precio_unidad , unidad_stock , stock_seguridad , img ) VALUES (%s, %s,%s, %s,%s, %s)"
        insert_compras= "INSERT INTO compras(cliente_id ,  articulo_id , fecha ,unidades ) VALUES (%s, %s, COALESCE(%s, CURDATE()), %s))" #si el vampo de fecha se queda vacio, se insertara la fecha del dia en el que se ha insertado del dato

        #tablen datuak
        cliente_datuak=[('José', 'Fernández Ruiz','Estudio Cero', 'Gerente', '41400', 'Sevilla', '656789043', 13/6/1968),('Luis', 'Fernández Chacón','Beep', 'Dependiente','41400', 'Sevilla', '675894566','24-05-1982'),('Antonio', 'Ruiz Gómez','Comar', 'Dependiente','41400', 'Sevilla','654345544','06-08-1989'),('Andrea', 'Romero Vázquez','EstudioCero', 'Dependiente','41400', 'Sevilla' ,'646765657','23-11-1974'),('José', 'Pérez Pérez', 'Beep', 'Gerente', '41400', 'Sevilla', '645345543','10-04-1978')]
        articulos_datuak=[('NETGEAR switch prosafe', 'Switch 8 puertos GigabitEthernet',125.0,  3, 2),('Switch SRW224G4-EU de Linksys', 'CISCO switch 24 puertos 10/100', 202.43, 2 ,2),('Switch Dlink','D-Link smartswitch 16 puertos', 149.90 , 7 ,4),('Switch Dlink','D-Link smart switch 48 puertos', 489.00 , 4 ,2)]
        compras_datuak=[(1, 1, '13-10-2010' ,2),(1, 2, 13/10/2010, 1),(2 ,3 ,15/10/2010 ,1),(2, 4 ,15/10/2010 ,1),(3, 1, 15/10/2010, 2),(4, 2, 15/10/2010, 1),(5, 3, 15/10/2010, 3),(1, 4, 16/10/2010, 1),(1, 1, 16/10/2010, 2),(2, 2 ,17/10/2010, 1),(3, 3, 18/10/2010, 4),(4, 4, 19/10/2010 ,2),(5, 1, 19/10/2010, 1)]

        #comprobar si las tablas tienen contenido

        kurtsorea.execute("SELECT COUNT(*) FROM cliente") #e utiliza para contar el número total de filas en la tabla, 
        if kurtsorea.fetchone()[0] == 0: #si la tabla esta vacia el resultado de filas deberia ser 0
            kurtsorea.executemany(insert_cliente, cliente_datuak) # insertar los datos en la tabla si no hay contenido de antes
            print("Datos insertados en la tabla cliente.")
        else:
            print("la tabla cliente ya tiene datos")

        kurtsorea.execute("SELECT COUNT(*) FROM articulo")
        if kurtsorea.fetchone()[0] == 0:
         kurtsorea.executemany(insert_articulo,articulos_datuak)
         print("Datos insertados en la tabla articulo.")
        else:
            print("la tabla articulo ya tiene datos")
        
        kurtsorea.execute("SELECT COUNT(*) FROM compras")
        if kurtsorea.fetchone()[0] == 0:
            kurtsorea.executemany(insert_compras,compras_datuak)
            print("Datos insertados en la tabla compras.")
        else:
         print("la tabla compras ya tiene datos")
        
        konexioa.commit()
    except Exception as e:
         # Revertir los cambios si ocurre un error
        konexioa.rollback()
        print("Ocurrió un error: ", e)                       
