import mysql.connector
from tkinter import messagebox
from application import app
cnx = mysql.connector.connect(user='root', password='',
                                host='127.0.0.1',
                                database='brothers_gym')

def login(username,password):

    cursor = cnx.cursor()

    try:  
        #Reading the admins data      
        cursor.execute("select * from admins")  
    
        #fetching the rows from the cursor object  
        result = cursor.fetchall()  
  
        valueUsername = result[0][1]
        valuePassword = result[0][2]
        print(valueUsername)
        print(valuePassword)
        print
        if username == valueUsername and password == valuePassword:
            print("Connected ")
            app()
           
        else : 
            game_over = messagebox.showinfo ( "Erreur" , "Vérifiez votre mail ou mot de passe" )
            
               
    except:  
        cnx.rollback()  
    