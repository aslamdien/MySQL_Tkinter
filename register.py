from tkinter import *
from tkinter import messagebox
import mysql.connector

mydb = mysql.connector.connect(user = 'lifechoices', password = '@Lifechoices1234', host = '127.0.0.1', database = 'hospital', auth_plugin='mysql_native_password')

root = Tk()
root.title("Register")
root.geometry("500x300")

userlab = Label(root, text = "PLease Enter Your Name:")
userlab.place(x = 50, y = 50)
userEnt = Entry(root)
userEnt.place(x=220, y=50)

passwordlab = Label(root, text = "Please Enter A Password:")
passwordlab.place(x=50, y=150)
passwordEnt = Entry(root, show = "*")
passwordEnt.place(x=220, y=150)

confirmLab = Label(root, text = "Confirm Your Password:")
confirmLab.place(x=50, y=200)
confirmEnt = Entry(root, show = "*")
confirmEnt.place(x=220, y=200)

root.mainloop()
