from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk

def login():
    if usernameEntry.get()==" " or passwordEntry.get()==" ":
        messagebox.showerror("Error","Fields cannot be empty")
    elif usernameEntry.get()=="Hari" and passwordEntry.get()=="1234":
        messagebox.showinfo("success","welcome")
        window.destroy()
        import sms1
    else:
        messagebox.showerror("Error","please Enter correct credentials")


window=Tk()
window.geometry('1520x780+0+0')
window.title('Login System of Student Management System')
window.resizable(False,False)

backgroundImage=ImageTk.PhotoImage(file='bgpic.jpg')
bgLabel=Label(window,image=backgroundImage)
bgLabel.place(x=0,y=0)

loginFrame = Frame(window,bg='grey99')
loginFrame.place(x=450, y=200)

logoImage = PhotoImage(file='logo.png')

logoLabel = Label(loginFrame, image=logoImage,bg='grey99')
logoLabel.grid(row=0, column=0, columnspan=2, pady=10)

usernameImage = PhotoImage(file='user.png')

usernameLabel = Label(loginFrame, image=usernameImage, text='username', compound=LEFT,
                      font=('times new roman', 20, 'bold'), bg='grey99')
usernameLabel.grid(row=1, column=0, padx=10, pady=10)

usernameEntry = Entry(loginFrame, font=('times new roman', 20, 'bold'), bd=5, fg='royal blue')
usernameEntry.grid(row=1, column=1, padx=10, pady=10)

passwordImage = PhotoImage(file='password.png')

passwordLabel = Label(loginFrame, image=passwordImage, text='password', compound=LEFT,
                      font=('times new roman', 20, 'bold'), bg='grey99')
passwordLabel.grid(row=2, column=0, padx=20, pady=10)

passwordEntry = Entry(loginFrame, font=('times new roman', 20, 'bold'), bd=5, fg='royal blue')
passwordEntry.grid(row=2, column=1, padx=20, pady=10)

loginButton = Button(loginFrame, text='login', font=('times new roman', 14, 'bold'), width=15, fg='white',
                     bg='cornflowerblue',command=login)
loginButton.grid(row=3, column=1, pady=10)

window.mainloop()

