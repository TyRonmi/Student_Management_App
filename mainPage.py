# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 20:10:56 2023

@author: Ronmi
"""

from tkinter import *
import time
import ttkthemes
from tkinter import ttk, messagebox, filedialog
import pymysql
import pandas


def topLevelFeatures(title, title_logo, button_text, command):
    global sessionEntry, idEntry, nameEntry, classEntry, dobEntry, genderEntry, addressEntry, mobileEntry, commentEntry, firstTermPositionEntry, secondTermPositionEntry, thirdTermPositionEntry, screen
    screen = Toplevel()
    screen.grab_set()
    screen.title(title)
    screen.resizable(False, False) 
    
    TitleLogo = PhotoImage(file = title_logo)
    screen.iconphoto(False, TitleLogo)
    
    
    sessionLabel = Label(screen, text='Session', font=('Bodoni MT', 10))
    sessionLabel.grid(row=0, column=0, padx=10, pady=10, sticky=W)
    sessionEntry = Entry(screen, font=('calibri', 10, 'bold'))
    sessionEntry.grid(row=0, column=1, padx=10, pady=10, sticky=W)
    
    idLabel = Label(screen, text='Student ID', font=('Bodoni MT', 10))
    idLabel.grid(row=1, column=0, padx=10, pady=10, sticky=W)
    idEntry = Entry(screen, font=('calibri', 10, 'bold'))
    idEntry.grid(row=1, column=1, padx=10, pady=10, sticky=W)
    
    nameLabel = Label(screen, text='Student Name', font=('Bodoni MT', 10))
    nameLabel.grid(row=2, column=0, padx=10, pady=10, sticky=W)
    nameEntry = Entry(screen, font=('calibri', 10, 'bold'))
    nameEntry.grid(row=2, column=1, padx=10, pady=10, sticky=W)
    
    
    classLabel = Label(screen, text='Class', font=('Bodoni MT', 10))
    classLabel.grid(row=3, column=0, padx=10, pady=10, sticky=W)
    classEntry = Entry(screen, font=('calibri', 10, 'bold'))
    classEntry.grid(row=3, column=1, padx=10, pady=10, sticky=W)
    
    dobLabel = Label(screen, text='D.O.B', font=('Bodoni MT', 10))
    dobLabel.grid(row=4, column=0, padx=10, pady=10, sticky=W)
    dobEntry = Entry(screen, font=('calibri', 10, 'bold'))
    dobEntry.grid(row=4, column=1, padx=10, pady=10, sticky=W)
    
    genderLabel = Label(screen, text='Gender', font=('Bodoni MT', 10))
    genderLabel.grid(row=5, column=0, padx=10, pady=10, sticky=W)
    genderEntry = Entry(screen, font=('calibri', 10, 'bold'))
    genderEntry.grid(row=5, column=1, padx=10, pady=10, sticky=W)
    
    addressLabel = Label(screen, text='Address', font=('Bodoni MT', 10))
    addressLabel.grid(row=6, column=0, padx=10, pady=10, sticky=W)
    addressEntry = Entry(screen, font=('calibri', 10, 'bold'))
    addressEntry.grid(row=6, column=1, padx=10, pady=10, sticky=W)
    
    mobileLabel = Label(screen, text='Mobile No.', font=('Bodoni MT', 10))
    mobileLabel.grid(row=7, column=0, padx=10, pady=10, sticky=W)
    mobileEntry = Entry(screen, font=('calibri', 10, 'bold'))
    mobileEntry.grid(row=7, column=1, padx=10, pady=10, sticky=W)
    
    firstTermPositionLabel = Label(screen, text='First Term Position', font=('Bodoni MT', 10))
    firstTermPositionLabel.grid(row=8, column=0, padx=10, pady=10, sticky=W)
    firstTermPositionEntry = Entry(screen,  width=10, font=('calibri', 10, 'bold'))
    firstTermPositionEntry.grid(row=8, column=1, padx=10, pady=10, sticky=W)
    
    secondTermPositionLabel = Label(screen, text='Second Term Position', font=('Bodoni MT', 10))
    secondTermPositionLabel.grid(row=9, column=0, padx=10, pady=10, sticky=W)
    secondTermPositionEntry = Entry(screen,  width=10, font=('calibri', 10, 'bold'))
    secondTermPositionEntry.grid(row=9, column=1, padx=10, pady=10, sticky=W)
    
    thirdTermPositionLabel = Label(screen, text='Third Term Position', font=('Bodoni MT', 10))
    thirdTermPositionLabel.grid(row=10, column=0, padx=10, pady=10, sticky=W)
    thirdTermPositionEntry = Entry(screen,  width=10, font=('calibri', 10, 'bold'))
    thirdTermPositionEntry.grid(row=10, column=1, padx=10, pady=10, sticky=W)
    
    commentLabel = Label(screen, text='Comment', font=('Bodoni MT', 10))
    commentLabel.grid(row=11, column=0, padx=10, pady=10, sticky=W)
    commentEntry = Entry(screen, font=('cambria', 10, 'italic'))
    commentEntry.grid(row=11, column=1, padx=10, pady=10, sticky=W)
    
     
    
    screenButton = ttk.Button(screen, text=button_text, command=command)
    screenButton.grid(row=13, columnspan=2, pady=10)
    

    if title=='Update Student':
# for the update screen, we need to select row data to update
        indexing = studentTable.focus()
        content = studentTable.item(indexing)
        listdata = content['values']
       
# for the update screen, we need to make selected row data appear in corresponding entries
        sessionEntry.insert(0, listdata[0])
        idEntry.insert(0, listdata[1])  
        nameEntry.insert(0, listdata[2]) 
        classEntry.insert(0, listdata[3]) 
        dobEntry.insert(0, listdata[4])
        genderEntry.insert(0, listdata[5])
        addressEntry.insert(0, listdata[6]) 
        mobileEntry.insert(0, listdata[7]) 
        firstTermPositionEntry.insert(0, listdata[8])
        secondTermPositionEntry.insert(0, listdata[9])
        thirdTermPositionEntry.insert(0, listdata[10])
        commentEntry.insert(0, listdata[11]) 



def currentdate():
    global date
    date=time.strftime('%d/%m/%Y')
    datelabel.config(text=f' {date}     ')


def currenttime():
    global nowtime
    nowtime=time.strftime('%H:%M:%S')
    timelabel.config(text=f'{nowtime}')
    timelabel.after(1000, currenttime)
    
    
def exitButtonCommand():
    yes_exit = messagebox.askyesno('Comfirm', 'Do You Want to Exit?') 
    if yes_exit:
        window.destroy()
    else:
        pass
    
    
    
def exportButtonCommand():
    url = filedialog.asksaveasfile(defaultextension='.csv')
    if url is not None:
        indexing = studentTable.get_children()
        newlist = []
        
        for index in indexing:
            content = studentTable.item(index)
            datalist = content['values']
            
            if all(value == "" for value in datalist):
                continue
            
            newlist.append(datalist)
            
        table = pandas.DataFrame(newlist, columns=['Session', 'ID Number', 'Name', 'Class', 'DOB', 'Gender', 'Address', 'Mobile', '1st Term Position', '2nd Term Position', '3rd Term Position', 'Comment', 'Added Time', 'Added Date'])
        table.to_csv(url, index=False)
        messagebox.showinfo('Successful', 'Data Saved Successfully')

    
def updateButtonCommand():
    query = 'update student set session=%s, name=%s, class=%s, dob=%s, gender=%s, address=%s, mobile=%s, firsttermposition=%s, secondtermposition=%s, thirdtermposition=%s, comment=%s, time=%s , date=%s where id=%s;' 
    myCursor.execute(query,(sessionEntry.get(), nameEntry.get(), classEntry.get(), dobEntry.get(), genderEntry.get(), 
                            addressEntry.get(), mobileEntry.get(), firstTermPositionEntry.get(), secondTermPositionEntry.get(), thirdTermPositionEntry.get(), commentEntry.get(), nowtime, date, idEntry.get()))
    connectCommand.commit()
    messagebox.showinfo('Successful', f'{nameEntry.get()}, with ID Number {idEntry.get()} Updated Successfully', parent=screen)
    screen.destroy()
    
# update the updata data on treeview
    showButtonCommand()
    

def showButtonCommand():
    query = 'select * from student;'
    myCursor.execute(query)
    display_data = myCursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in display_data:
        studentTable.insert('', END, values=data)


def deleteButtonCommand():
    indexing = studentTable.focus()
    content = studentTable.item(indexing)
    content_id = content['values'][1]
    name_id = content['values'][2]
    
    sure_delete = messagebox.askyesno('Confirm', f'Delete {name_id}, with ID Number {content_id} From Records?')
    if sure_delete:
        query = 'delete from student where id=%s;'
        myCursor.execute(query, content_id)
        connectCommand.commit()
        messagebox.showinfo('Deleted', f'{name_id}, with ID Number {content_id} deleted successfully. Click OK to refresh records')
        query = 'select * from student;'
        myCursor.execute(query)
        display_data = myCursor.fetchall()
        studentTable.delete(*studentTable.get_children())
       
        for data in display_data:
            studentTable.insert('', END, values=data)
            
        else:
            pass


def searchButtonCommand():
    query = 'select * from student where session = %s or id=%s or name = %s or class=%s or dob=%s or gender=%s or address=%s or mobile=%s or firsttermposition=%s or secondtermposition=%s or thirdtermposition=%s or comment=%s;'
    myCursor.execute(query, (sessionEntry.get(), idEntry.get(), nameEntry.get(), classEntry.get(), dobEntry.get(), genderEntry.get(), addressEntry.get(), mobileEntry.get(), firstTermPositionEntry.get(), secondTermPositionEntry.get(), thirdTermPositionEntry.get(), commentEntry.get()))
    studentTable.delete(*studentTable.get_children())
    display_data = myCursor.fetchall()
    for data in display_data:
        studentTable.insert('', END, values=data)


def addButtonCommand():
    if sessionEntry.get()=='' or idEntry.get()=='' or nameEntry.get()=='' or classEntry.get()=='' or dobEntry.get()=='' or genderEntry.get()=='' or addressEntry.get()=='' or mobileEntry.get()=='' or firstTermPositionEntry.get()=='' or secondTermPositionEntry.get()=='' or thirdTermPositionEntry.get()=='' or commentEntry.get()=='':
        messagebox.showerror('Error', 'Entry into All Fields Are Required', parent=screen)
    else:
        try:
            query = 'insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            myCursor.execute(query, (sessionEntry.get(), idEntry.get(), nameEntry.get(), classEntry.get(), dobEntry.get(), genderEntry.get(), addressEntry.get(), 
                                     mobileEntry.get(), firstTermPositionEntry.get(), secondTermPositionEntry.get(), thirdTermPositionEntry.get(), commentEntry.get(), nowtime, date))
            connectCommand.commit()
            result = messagebox.askyesno('Successful ', 'Data Added Successfully. Do You Want To Clear Form?', parent=screen)
            if result:
                sessionEntry.delete(0, END)
                idEntry.delete(0, END)
                nameEntry.delete(0, END)
                classEntry.delete(0, END)
                dobEntry.delete(0, END)
                genderEntry.delete(0, END)
                addressEntry.delete(0, END)
                mobileEntry.delete(0, END)
                firstTermPositionEntry.delete(0, END)
                secondTermPositionEntry.delete(0, END)
                thirdTermPositionEntry.delete(0, END)
                commentEntry.delete(0, END)
        except:
            messagebox.showerror('Error', 'Student ID Already Exist', parent=screen)
            return    
# displaying data on right frame tree view
        query = 'select *from student;'
        myCursor.execute(query)
        display_data = myCursor.fetchall()
        
        studentTable.delete(*studentTable.get_children())
        for data in display_data:
            datalist=list(data)
            studentTable.insert('', END, values=datalist)


def connect_DB():
    def connect():
        global myCursor, connectCommand
        try:
            connectCommand = pymysql.Connect(host=hostnameEntry.get(), user=usernameEntry.get(), password='123')
            myCursor = connectCommand.cursor()             
        except:
            messagebox.showerror('Error !', 'Invalid Hostname or Username', parent=connectDBWindow)
            return 
# Creating the database
        try:
            query = 'create database studentmanagementsystem;'
            myCursor.execute(query)
            query = 'use studentmanagementsystem;'
            myCursor.execute(query)
            query = 'create table student(session Varchar(15), id Varchar(15) not null primary key, name Varchar(50), class Varchar(20), dob Varchar(20), gender Varchar(10), address Varchar(100), mobile Varchar(33), firsttermposition varchar(10), secondtermposition varchar(10), thirdtermposition varchar(10), comment Varchar(1000), time Varchar(20), date Varchar(20))'
            myCursor.execute(query)
        except:
            query = 'use studentmanagementsystem;'
            myCursor.execute(query)
        messagebox.showinfo('Successful', 'You Are Now Connected To Database', parent=connectDBWindow)
        
        connectDBWindow.destroy()
        addStudentButton.config(state=NORMAL)
        searchStudentButton.config(state=NORMAL)
        deleteStudentButton.config(state=NORMAL)
        updateStudentButton.config(state=NORMAL)
        showStudentButton.config(state=NORMAL)
        exportDataButton.config(state=NORMAL)
        
        
    connectDBWindow = Toplevel()
    connectDBWindow.grab_set()
    connectDBWindow.geometry('300x130+950+180')
    connectDBWindow.title('Connect to Database')
    connectDBWindow.resizable(False, False)
    connectDBLogo = PhotoImage(file = 'connect.png')
    connectDBWindow.iconphoto(False, connectDBLogo)
    
    hostnameLabel = Label(connectDBWindow, text='Host Name ', font=('Calibri', 10, 'bold'))
    hostnameLabel.grid(row=0, column=0, padx=20, pady=10)
    
    hostnameEntry = Entry(connectDBWindow)
    hostnameEntry.grid(row=0, column=1, padx=20)

    usernameLabel = Label(connectDBWindow, text='User Name ', font=('Calibri', 10, 'bold'))
    usernameLabel.grid(row=1, column=0, padx=20, pady=10)

    usernameEntry = Entry(connectDBWindow)
    usernameEntry.grid(row=1, column=1, padx=20)

    #passwordLabel = Label(connectDBWindow, text='Password    ', font=('Calibri', 10, 'bold'))
    #passwordLabel.grid(row=2, column=0, padx=20, pady=10)
    
    #passwordEntry = Entry(connectDBWindow, show="*")
    #passwordEntry.grid(row=2, column=1, padx=20)

    connectDBButton = ttk.Button(connectDBWindow, text='  Connect  ', command=connect)
    connectDBButton.grid(row=2, column=1, padx= 20, pady=10)

window = ttkthemes.ThemedTk()

window.get_themes()

window.set_theme('aquativo')


window.geometry('1250x600+50+50')
window.title('Student Management System - Mainpage')
window.resizable(False, False)
windowLogo = PhotoImage(file = 'applogo.png')
window.iconphoto(False, windowLogo)


datetimeframe = Frame(window)
datetimeframe.place(x=20, y=5)


dateImage = PhotoImage(file= 'dateimage.png')
datelabel = Label(datetimeframe, image = dateImage, text=' ', compound=LEFT)
datelabel.grid(row=0, column=0)
currentdate()

timeImage = PhotoImage(file= 'clock3.png')
timelabel = Label(datetimeframe, image = timeImage, text=' ', compound=LEFT)
timelabel.grid(row=0, column=5)
currenttime()


titleLabel = Label(text='Student Management System', font=('garamond', 11, 'bold'), width=30)
titleLabel.place(x=500, y=5)


connectButton = ttk.Button(window, text='Connect to Database', command=connect_DB)
connectButton.place(x=1108, y=10)


leftFrame = Frame(window, bd=3, relief=RIDGE)
leftFrame.place(x=23, y=60, width=250, height=520)


studentLogo = PhotoImage(file = 'studentlogo.png')
studentLogoLabel = Label(leftFrame, image=studentLogo)
studentLogoLabel.place(x=70, y=0)

#functional buttons
showStudentButton = ttk.Button(leftFrame, text='  Show Students', width=15, state=DISABLED, command=showButtonCommand)
showStudentButton.place(x=68, y=120)

addStudentButton = ttk.Button(leftFrame, text='    Add Student', width=15, state=DISABLED, command=lambda :topLevelFeatures('Add Student', 'addstudentlogo.png', '    Add    ', addButtonCommand))
addStudentButton.place(x=68, y=160)

searchStudentButton = ttk.Button(leftFrame, text='  Search Student', width=15, state=DISABLED, command=lambda :topLevelFeatures('Search Student', 'search.png', '  Search  ', searchButtonCommand))
searchStudentButton.place(x=68, y=200)

deleteStudentButton = ttk.Button(leftFrame, text='  Delete Student', width=15, state=DISABLED, command=deleteButtonCommand)
deleteStudentButton.place(x=68, y=240)

updateStudentButton = ttk.Button(leftFrame, text=' Update Student', width=15, state=DISABLED, command=lambda :topLevelFeatures('Update Student', 'update.png', '  Update  ', updateButtonCommand))
updateStudentButton.place(x=68, y=280)

exportDataButton = ttk.Button(leftFrame, text='     Export Data', width=15, state=DISABLED, command=exportButtonCommand)
exportDataButton.place(x=68, y=320)

exitButton = ttk.Button(leftFrame, text='            Exit', width=15, command=exitButtonCommand)
exitButton.place(x=68, y=420)


rightFrame = Frame(window, bd=3, relief=RIDGE)
rightFrame.place(x=295, y=60, width=932, height=520)


#creating horizontal and vertical scroll bars to be able to view full table
scrollBarX = Scrollbar(rightFrame, orient=HORIZONTAL)
scrollBarY = Scrollbar(rightFrame, orient=VERTICAL)


# creating table interface in right frame
studentTable = ttk.Treeview(rightFrame, columns=('session', 'id', 'name', 'class', 'dob', 'gender','address', 
                                  'mobile', 'firsttermposition', 'secondtermposition', 'thirdtermposition', 'comment', 'time', 'date'),
                            xscrollcommand=scrollBarX.set, yscrollcommand=scrollBarY.set)

scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)
#placing scrollbars in right frame
scrollBarX.pack(side=BOTTOM, fill=X)
scrollBarY.pack(side=RIGHT, fill=Y)

studentTable.pack(fill=BOTH, expand=1)


# adding headings to the student table

studentTable.heading('session', text='Session')
studentTable.heading('id', text='Student ID')
studentTable.heading('name', text='Student Name')
studentTable.heading('class', text='Class')
studentTable.heading('dob', text='D.O.B')
studentTable.heading('gender', text='Gender')
studentTable.heading('address', text='Address')
studentTable.heading('mobile', text='Mobile No.')
studentTable.heading('firsttermposition', text='1st Term Position')
studentTable.heading('secondtermposition', text=' 2nd Term Position')
studentTable.heading('thirdtermposition', text='3rd Term Position')
studentTable.heading('comment', text='Comment')
studentTable.heading('time', text='Added Time')
studentTable.heading('date', text='Added Date')


studentTable.column('session', width=70, anchor=CENTER)
studentTable.column('id', width=70, anchor=CENTER)
studentTable.column('name', anchor=CENTER)
studentTable.column('class', width=90, anchor=CENTER)
studentTable.column('dob', width=150, anchor=CENTER)
studentTable.column('gender', width=50, anchor=CENTER)
studentTable.column('address', anchor=CENTER)
studentTable.column('mobile', width=90, anchor=CENTER)
studentTable.column('firsttermposition', width=120, anchor=CENTER)
studentTable.column('secondtermposition', width=120, anchor=CENTER)
studentTable.column('thirdtermposition', width=120, anchor=CENTER)
studentTable.column('comment', anchor=CENTER)
studentTable.column('time', width=80, anchor=CENTER)
studentTable.column('date', width=80, anchor=CENTER)





style = ttk.Style()
style.configure('Treeview', rowheight=25, font=('garamond', 9, 'bold'))

style.configure('Treeview.Heading', font=('garamond', 10, 'bold'), foreground='green')


studentTable.config(show='headings')


window.mainloop()
