from admin import Admin
from tkinter import *
import mysql.connector



window=Tk()
backgrounf_color_home='red'
window.title("BrothersGym")
window.geometry("700x450")
window.config(bg=backgrounf_color_home)

name = Label(window,text = "Username",background=backgrounf_color_home).place(x = 180,y = 200)  
e1 = Entry(window).place(x = 240,y = 200) 
password = Label(window,text = "Password",background=backgrounf_color_home).place(x = 180,y = 230)   
e2 = Entry(window).place(x = 240,y = 230) 
submit = Button(window, text = "Submit").place(x = 280,y = 280)   
window.mainloop()


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