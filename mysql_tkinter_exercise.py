import mysql.connector
from tkinter import *
from tkinter import messagebox

mydb = mysql.connector.connect(user = 'lifechoices', password = '@Lifechoices1234', host = '127.0.0.1', database = 'hospital', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

xy = mycursor.execute('Select * from login')

root = Tk()
root.title("Login Page")
root.geometry("500x300")

usernamelab = Label(root, text = "Please Enter Username:")
usernamelab.place(x=50, y=50)
usernameEnt = Entry(root)
usernameEnt.place(x=220, y=50)

passwordlab = Label(root, text = "Please Enter Password:")
passwordlab.place(x=50, y=100)
passwordEnt = Entry(root, show = "*")
passwordEnt.place(x=220, y=100)

def login():
    for i in mycursor:
        if usernameEnt.get() == i[0] and passwordEnt.get() == i[1]:
            messagebox.showinfo("Loged In", "Access Granted")
            break

        elif usernameEnt.get() != i[0] and passwordEnt.get() != i[1]:
            messagebox.showerror("Access Denied", "Please Enter Correct Username or Password")
            usernameEnt.delete(0, END)
            passwordEnt.delete(0, END)
            break


loginbtn = Button(root, text = "Login", command = login)
loginbtn.place(x=150, y=150)

registerbtn = Button(root, text = "Register New User")
registerbtn.place(x=250, y=150)

root.mainloop()
