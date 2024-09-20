def taulak_sortu(kurtsorea):
  mysql_ikasleak= "CREATE TABLE IF NOT EXISTS ikasleak( ikasle_id int NOT NULL,  izena text NOT NULL,  abizena text NOT NULL, PRIMARY KEY(ikasle_id))"
  kurtsorea.execute(mysql_ikasleak)

  mysql_ikasgaiak= "CREATE TABLE IF NOT EXISTS ikasgaiak( ikasgai_id int NOT NULL,  izena text NOT NULL,  maila text NOT NULL, hizkuntza text NOT NULL,  PRIMARY KEY(ikasgai_id))"
  kurtsorea.execute(mysql_ikasgaiak)

  mysql_notak= "CREATE TABLE IF NOT EXISTS notak( nota int NOT NULL,  oharra text NOT NULL,  maila text NOT NULL, ikasle_id int NOT NULL, ikasgai_id int NOT NULL, FOREIGN KEY (ikasgai_id) REFERENCES ikasgaiak(ikasgai_id), FOREIGN KEY (ikasle_id) REFERENCES ikasleak(ikasle_id)) "
  kurtsorea.execute(mysql_notak)


def datuak_hasieratu(kurtsorea):
  ikaslea_datuak = [
    (1,"Jon","Alberdi")
  ]
  