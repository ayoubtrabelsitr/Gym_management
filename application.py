from tkinter import *

def searchUsers():

    import Data
    data = Data.search()     
    # find total number of rows and
    # columns in list
    total_rows = len(data)
    total_columns = len(data[0])
    # create root window
    root = Tk()
    root.title("Liste des membres")
    # code for creating table
    information = ["ID","NOM","PRENOM","EMAIL","TELEPHONE","ADRESSE","PAIEMENT"]
    for i in range (7):            
        button = Button(root, width=16, fg='red',font=('Arial',12,'bold'),text=information[i])
        button.grid(row=0, column=i)

    for i in range(total_rows):
        for j in range(total_columns):  
            button = Button(root, width=16, fg='black',font=('Arial',12,'bold'),text=str(data[i][j]))
            button.grid(row=i+1, column=j)

def deleteUsers():
    
    import Data
    data = Data.search()     
    # find total number of rows and
    # columns in list
    total_rows = len(data)
    total_columns = len(data[0])
    # create root window
    root = Tk()
    root.title("Supprimer des membres")
    # code for creating table
    information = ["ID","NOM","PRENOM","EMAIL","TELEPHONE","ADRESSE","PAIEMENT"]
    for i in range (7):            
        entre = Button(root, width=14, fg='blue',font=('Arial',12,'bold'),text=str(information[i]))
        entre.grid(row=0, column=i+1)
        
    for j in range (total_rows):
        entre = Button(root,width=14, fg='red',font=('Arial',12,'bold'),text="X")
        entre.grid(row=j+1, column=0)  
    for i in range(total_rows):
        for j in range(total_columns):
            entre = Button(root, width=14, fg='black',font=('Arial',12,'bold'),text=str(data[i][j]))
            entre.grid(row=i+1, column=j+1)  
         
def modifyUsers():
    
    import Data
    data = Data.search()     
    # find total number of rows and
    # columns in list
    total_rows = len(data)
    total_columns = len(data[0])
    # create root window
    root = Tk()
    root.title("Liste des membres")
    # code for creating table
    information = ["ID","NOM","PRENOM","EMAIL","TELEPHONE","ADRESSE","PAIEMENT"]
    for i in range (7):            
        entre = Entry(root, width=18, fg='red',font=('Arial',14,'bold'))
        entre.grid(row=0, column=i)
        entre.insert(END, str(information[i]))

    for i in range(total_rows):
        for j in range(total_columns):
                
            entre = Entry(root, width=18, fg='blue',font=('Arial',14,'bold'))
            entre.grid(row=i+1, column=j)
            entre.insert(END, str(data[i][j]))

def addUser():
    return 0

def getWindow():
    from main import getwindow
    return getwindow()

def updateUser():
    return 0 



def app():
   
    window2 = Tk()
    frame_name = Frame(window2)
    frame_name.place(relx=0.5, rely=0.6, anchor="center")
    frame_password = Frame(window2)
    frame_password.place(relx=0.5, rely=0.7, anchor="center")
    backgrounf_color_home = '#17c0eb'
    backgrounf_color_buttons = '#4cdffa'

    window2.title("BrothersGym")
    window2.geometry("700x450")
    window2.minsize(500, 350)
    window2.config(bg=backgrounf_color_home)

    submit = Button(window2, text="Consulter la liste des membres",bg=backgrounf_color_buttons, command=searchUsers).place(x=50, y=80)
    submit2 = Button(window2, text="Supprimer des membres",bg=backgrounf_color_buttons, command=deleteUsers).place(x=50, y=150)
    submit3 = Button(window2, text="Y",bg=backgrounf_color_buttons).place(x=50, y=210)
    submit4 = Button(window2, text="Z",bg=backgrounf_color_buttons).place(x=50, y=280)


    submit5= Button(window2, text="Quitter",bg=backgrounf_color_buttons,command=exit).place(x=350, y=380)