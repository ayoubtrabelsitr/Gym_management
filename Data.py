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

def modifyUser(id, info):
    import application
    cursor = cnx.cursor()

    try:
        # Requête SQL pour modifier les informations de l'utilisateur
        cursor.execute("UPDATE users SET nom = %s, prenom = %s, email = %s, telephone = %s, adresse = %s, paiement = %s WHERE id = %s",
                       (info[1], info[2], info[3], info[4], info[5], info[6], id))
        cnx.commit()
        application.modifyUsers()
        
    except Exception as e:
        print(f"Erreur lors de la modification : {e}")
        cnx.rollback()