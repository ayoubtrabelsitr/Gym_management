from admin import Admin
import mysql.connector

cnx = mysql.connector.connect(user='root', password='',
                                host='127.0.0.1',
                                database='brothers_gym')

cursor = cnx.cursor()

bouda = Admin(2,"bouda","123456")
query = bouda.ajouterAdmin()

cursor.execute(query,(bouda.getId(),
    bouda.getUsername(),
    bouda.getPassword()))

cnx.commit()