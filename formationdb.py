import mysql.connector
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    port=3306,
    database="cseiniit"
)
# db_cursor=cnx.cursor()
# formation= """INSERT INTO FORMATION(designation,
#          description)
#          VALUES ('Développement web Python/Django','Formation sur le développement web')"""
# try:
#     db_cursor.execute(formation)
#     cnx.commit()
# except Exception as e:
#     print(db_cursor.rowcount,e)



""" update table formation"""

# def update_form():
#     db_cursor=cnx.cursor()
#     formation = "update FORMATION SET designation='Développement web Python/php' where id='1'"
#     db_cursor.execute(formation)
#     cnx.commit()
#     print(" formation updated avec  succes")
# update_form()
   

"""suppression d'une formation"""
def delete_form():
    cursor=cnx.cursor()
    formation="delete from FORMATION where id='2'"
    cursor.execute(formation)
    cnx.commit()
    print("formation supprimer avec success")
delete_form()    





