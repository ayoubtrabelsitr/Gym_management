from tkinter import *

def searchUsers():

    import Data
    data = Data.search()     
    total_rows = len(data)
    total_columns = len(data[0])
    root = Tk()
    root.title("Liste des membres")
    information = ["ID","NOM","PRENOM","EMAIL","TELEPHONE","ADRESSE","PAIEMENT"]
    for i in range (7):  
        if i==3:
            button = Button(root, width=24, fg='red',font=('Arial',11,'bold'),text=information[i])
            button.grid(row=0, column=i)
        else : 
            button = Button(root, width=13, fg='red',font=('Arial',11,'bold'),text=information[i])
            button.grid(row=0, column=i)

    for i in range(total_rows):
        for j in range(total_columns):  
            if j==3:
                button = Button(root, width=24, fg='black',font=('Arial',11,'bold'),text=str(data[i][j]),anchor="w")
                button.grid(row=i+1, column=j)
            else :    
                button = Button(root, width=13, fg='black',font=('Arial',11,'bold'),text=str(data[i][j]))
                button.grid(row=i+1, column=j)

def deleteUsers():
    import Data
    data = Data.search()     
    def check_window_state(window):
        state = window.state()
        if state == 'normal':
            window.destroy()

    total_rows = len(data)
    total_columns = len(data[0])
    root = Tk()
    root.title("Supprimer des membres")
    information = ["ID","NOM","PRENOM","EMAIL","TELEPHONE","ADRESSE","PAIEMENT"]
    for i in range (7):            
        entre = Button(root, width=14, fg='blue',font=('Arial',12,'bold'),text=str(information[i]))
        entre.grid(row=0, column=i+1)
        

    for i in range(total_rows):
        for j in range(total_columns):
            entre = Button(root, width=14, fg='black',font=('Arial',12,'bold'),text=str(data[i][j]))
            entre.grid(row=i+1, column=j+1)  
    for j in range (total_rows):
        entre = Button(root, width=14, fg='red', font=('Arial',12,'bold'), text="X", command=lambda j=j: (Data.deleteUser(data[j][0]), check_window_state(root))) 
        entre.grid(row=j+1, column=0)  

 
def modifyUsers():
    def check_window_state(window):
        state = window.state()
        if state == 'normal':
            window.destroy()

    import Data
    data = Data.search()

    total_rows = len(data)
    total_columns = len(data[0])

    # Liste pour stocker les références des Entry
    entry_list = []

    # Créer la fenêtre root
    root = Tk()
    root.title("Modifier des membres")
    
    # Créer les en-têtes des colonnes
    information = ["ID", "NOM", "PRENOM", "EMAIL", "TELEPHONE", "ADRESSE", "PAIEMENT"]
    for i in range(7):
        entre = Button(root, width=14, fg='red', font=('Arial', 12, 'bold'), text=str(information[i]))
        entre.grid(row=0, column=i+1)

    # Créer les Entry et stocker les références dans la liste entry_list
    for i in range(total_rows):
        row_entries = []
        for j in range(total_columns):
            entry = Entry(root, width=14, fg='black', font=('Arial', 12, 'bold'))
            entry.grid(row=i+1, column=j+1)
            entry.insert(END, str(data[i][j]))  # Insérer la valeur existante
            row_entries.append(entry)  # Ajouter chaque Entry à la liste de la ligne
        entry_list.append(row_entries)  # Ajouter chaque ligne d'Entries dans la liste principale

    # Fonction pour récupérer et envoyer les valeurs modifiées
    def submit_modifications(index):
        # Récupérer les nouvelles valeurs des Entry pour la ligne donnée
        modified_values = [entry.get() for entry in entry_list[index]]
        Data.modifyUser(data[index][0], modified_values)  # Envoi à la fonction de modification
        check_window_state(root)

    # Créer les boutons "Modifier" et associer à la fonction submit_modifications
    for j in range(total_rows):
        entre = Button(root, width=16, fg='red', font=('Arial', 12, 'bold'), text="Modifier",
                       command=lambda j=j: submit_modifications(j))
        entre.grid(row=j+1, column=0)



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
    submit3 = Button(window2, text="Ajouter des membres",bg=backgrounf_color_buttons).place(x=50, y=210)
    submit4 = Button(window2, text="Modifier des membres",bg=backgrounf_color_buttons,command=modifyUsers).place(x=50, y=280)


    submit5= Button(window2, text="Quitter",bg='red',command=exit).place(x=350, y=380)