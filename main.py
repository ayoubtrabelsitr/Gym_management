from admin import Admin
from tkinter import *
import mysql.connector



window=Tk()
frame_name = Frame(window)
frame_name.place(relx=0.5, rely=0.6, anchor="center")
frame_password=Frame(window)
frame_password.place(relx=0.5, rely=0.7, anchor="center")
backgrounf_color_home='red'
window.title("BrothersGym")
window.geometry("700x450")
window.minsize(500,350)
window.config(bg=backgrounf_color_home)
#image
width=height=180
image_home = PhotoImage(file="jeu.png").subsample(3)
canvas = Canvas(window,width=width, height=height,bg=backgrounf_color_home, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image_home)
canvas.place(relx=0.5, rely=0.3, anchor="center")

name = Label(frame_name,text = "Username",background=backgrounf_color_home).pack(side=LEFT) 
e1 = Entry(frame_name).pack(side=RIGHT) 
password = Label(frame_password,text = "Password",background=backgrounf_color_home).pack(side=LEFT)   
e2 = Entry(frame_password).pack(side=RIGHT)
submit = Button(window, text = "Connect").place(relx=0.52, rely=0.8, anchor="center")
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