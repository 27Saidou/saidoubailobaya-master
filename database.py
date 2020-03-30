import mysql.connector
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    port=3306,
    database="cseiniit"
)
"""creation  de la bdb"""
db_cursor = cnx.cursor()
db_cursor.execute("CREATE DATABASE cseiniit")
db_cursor.execute("SHOW DATABASES")
for db in db_cursor:
    print(db)
    db_cursor.close()
    cnx.close()

""" creation table formation"""
db_cursor = cnx.cursor()
# creation de la table formations
db_cursor.execute(
	"CREATE TABLE formation (id INT AUTO_INCREMENT PRIMARY KEY, designation varchar(255)NOT NULL,description varchar(255)NOT NULL)")
# afficher la liste des tables
db_cursor.execute("SHOW TABLES")
for table in db_cursor:
	print(table)
        db_cursor.close()
        cnx.close()
