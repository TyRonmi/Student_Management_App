# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 21:24:10 2023

@author: Ronmi
"""

from tkinter import *
#from PIL import ImageTk
from tkinter import messagebox
from tkinter import PhotoImage


def login():
    if usernameEntry.get() == '' or passwordEntry.get() =='':
        messagebox.showerror('Error', 'Username and Password Cannot Be Blank')
        
    elif usernameEntry.get() == 'user' and passwordEntry.get() == '1234':
        messagebox.showinfo('Login Successful', 'Welcome Admin...')
        window.destroy()
        import mainPage
         
    
   
    else:
        messagebox.showerror('Ooops!', 'Username or Password Incorrect')

window = Tk()


window.geometry('800x400+275+100')
window.title('Student Management System - Login Page')
window.resizable(False, False)
windowLogo = PhotoImage(file = 'applogo.png')
window.iconphoto(False, windowLogo)

backgroundImage = PhotoImage(file= 'bg.png')
backgroundLabel = Label(window, image=backgroundImage)
backgroundLabel.place(x=250, y=0)


loginFrame = Frame(window)
loginFrame.place(x=15, y=60)

loginImage = PhotoImage(file='applogoo.png')

loginLabel = Label(loginFrame, image=loginImage)
loginLabel.grid(columnspan=2, pady=10)

usernameImage = PhotoImage(file='usernameimage.png')
usernameLabel = Label(loginFrame, image=usernameImage, text='Username  ', compound=LEFT)
usernameLabel.grid(row=1, column=0, pady=10)

passwordImage = PhotoImage(file='passwordimage.png')
passwordLabel = Label(loginFrame, image=passwordImage, text='Password  ', compound=LEFT)
passwordLabel.grid(row=2, column=0, pady=10)

usernameEntry = Entry(loginFrame, bd=1)
usernameEntry.grid(row=1, column=1, pady=10)
passwordEntry = Entry(loginFrame, show="*", bd=1)
passwordEntry.grid(row=2, column=1, pady=10)


loginButton = Button(loginFrame, text='Login', font=('times new roman', 10, 'bold'), width=12
                     ,fg= 'white', bg='cornflowerblue', activebackground='cornflowerblue', activeforeground='white', cursor='hand2', command=login)
loginButton.grid(row=3, columnspan=2, pady=20)




window.mainloop()


        