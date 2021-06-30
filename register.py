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

def register():
    userEnt.get()
    confirmEnt.get()

    if userEnt.get() == '' or passwordEnt.get() == '' or confirmEnt.get() == '':
        messagebox.showerror("Error", "Please Fill Out All Everything")
    elif passwordEnt.get() != confirmEnt.get():
        messagebox.showerror("Error!!", "Passwords Do Not Match")
        passwordEnt.delete(0, END)
        confirmEnt.delete(0, END)

    else:
        mycursor = mydb.cursor()
        insert = (
            "INSERT INTO login (username, password) VALUES (%s, %s)"
        )
        val = (userEnt.get(), confirmEnt.get())
        try:
            mycursor.execute(insert, val)

            mydb.commit()
        except:
            mycursor.execute('Select * from login')
            messagebox.showinfo("Registered", "Information Stored")
            root.destroy()
            import mysql_tkinter_exercise

def showPass():
    passwordEnt.config(show = "")
    confirmEnt.config(show = "")

registerBtn = Button(root, text = "Register", command = register)
registerBtn.place(x=200, y=250)

showPasswordBtn = Button(root, text = "Show Password", command = showPass)
showPasswordBtn.place(x=300, y=250)

root.mainloop()
