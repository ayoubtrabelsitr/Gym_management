import mysql.connector
from tkinter import messagebox


cnx = mysql.connector.connect(
    user="root", password="", host="127.0.0.1", database="brothers_gym"
)
def search():
    cursor = cnx.cursor()

    try:
        # Reading the admins data
        cursor.execute("select * from users")
        # fetching the rows from the cursor object
        result = cursor.fetchall()
        return result      
        # if username == valueUsername and password == valuePassword:
        #     print("Connected ")

        #     return True
        # else:
        #     game_over = messagebox.showinfo(
        #         "Erreur", "Vérifiez votre mail ou mot de passe"
        #     )

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
        # Reading the admins data
        cursor.execute("delete from users WHERE id='{}'".format(id))
        cnx.commit()
        application.deleteUsers()
        
    except:
        cnx.rollback()