import mysql.connector
from tkinter import messagebox


cnx = mysql.connector.connect(
    user="root", password="", host="127.0.0.1", database="brothers_gym"
)
def search():
    cursor = cnx.cursor()

    try:
        cursor.execute("select * from users")
        # fetching the rows from the cursor object
        result = cursor.fetchall()
        return result      

    except:
        cnx.rollback()


def login(username, password):
    import application

    cursor = cnx.cursor()

    try:
        # Reading the admins data
        cursor.execute("select * from admins")

        # fetching the rows from the cursor object
        result = cursor.fetchall()

        valueUsername = result[0][1]
        valuePassword = result[0][2]
        print
        if username == valueUsername and password == valuePassword:
            print("Connected ")

            return True
        else:
            game_over = messagebox.showinfo(
                "Erreur", "Vérifiez votre mail ou mot de passe"
            )

    except:
        cnx.rollback()
def deleteUser(id):
    import application

    cursor = cnx.cursor()

    try:
        cursor.execute("delete from users WHERE id='{}'".format(id))
        cnx.commit()
        application.deleteUsers()
        
    except:
        cnx.rollback()

def modifyUser(id,info):
    import application

    cursor = cnx.cursor()

    try:
        print(info[1])
        print(info[2])
        cursor.execute("UPDATE users SET nom = '{}', prenom = '{}', email = '{}', telephone = '{}',adresse = '{}', paiement = '{}' WHERE id = '{}'".format(info[1],info[2],info[3],info[4],info[5],info[0]))
        cnx.commit()
        application.modifyUsers()
        
    except:
        cnx.rollback()        