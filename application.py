from tkinter import *


def app():

    window2 = Tk()
    frame_name = Frame(window2)

    frame_name.place(relx=0.5, rely=0.6, anchor="center")
    frame_password = Frame(window2)
    frame_password.place(relx=0.5, rely=0.7, anchor="center")
    backgrounf_color_home = "red"
    window2.title("BrothersGym")
    window2.geometry("700x450")
    window2.minsize(500, 350)
    window2.config(bg=backgrounf_color_home)

    submit = Button(window2, text="Connect").place(relx=0.52, rely=0.8, anchor="center")
