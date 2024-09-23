def taulak_sortu(kurtsorea,konexioa):
    try:

        mysql_cliente= "CREATE TABLE IF NOT EXISTS cliente( cliente_id int NOT NULL AUTO_INCREMENT,  nombre text NOT NULL,  apellidos text NOT NULL,empresa text NOT NULL, puesto text NOT NULL, CP text DEFAULT '20600', provincia text DEFAULT 'Guipuzkoa',fechaNacimiento DATE, PRIMARY KEY(cliente_id))"
        kurtsorea.execute(mysql_cliente)

        mysql_articulo= "CREATE TABLE IF NOT EXISTS articulo( articulo_id int NOT NULL AUTO_INCREMENT,  izena text NOT NULL,  descripcion text NOT NULL, precio_unidad DECIMAL(10,2) NOT NULL, unidad_stock INT NOTT NULL, stock_seguridad INT NOT NULL, img text,  PRIMARY KEY(articulo_id))"
        kurtsorea.execute(mysql_articulo)

        mysql_compras= "CREATE TABLE IF NOT EXISTS notak( cliente_id int NOT NULL,  articulo_id int NOT NULL, fecha DATE DEFAULT CURDATE(),unidades INT NOT NULL, FOREIGN KEY (cliente_id) REFERENCES cliente(cliente_id), FOREIGN KEY (articulo_id) REFERENCES articulo(articulo_id)) "
        kurtsorea.execute(mysql_compras)

        #comfirmar los cabios
        konexioa.commit()
    except Exception as e:
         # Revertir los cambios si ocurre un error
        konexioa.rollback()
        print("Ocurrió un error: ", e)
