from DOCTORS import *
from USERS import *
from tkinter import*
from tkinter import messagebox
import mysql.connector

root = Tk()
root.title("STRAYCARE")

photo=PhotoImage(file="pro.png")
imagel=Label(image=photo)
imagel.pack()

HEADING=Label(text="STRAY CARE",font=("Comic Sans MS",20,"bold"), bg="green")
HEADING.pack()

def screen1():
    def getvalue():
        if(uservalue.get()==""):
            messagebox.showinfo("ALERT","COMPUSORY TO FILL username")

        if (pass1value.get() == ""):
            messagebox.showinfo("ALERT", "COMPUSORY TO FILL password")
        print(uservalue.get())
        print(pass1value.get())
        mycursor = mydb.cursor()
        sql = "select * from signup where NAME=%s and PASSWORD=%s"
        val = (uservalue.get(), pass1value.get())

        mycursor.execute(sql, val)
        res = mycursor.fetchall()
        if res:
            print("sUCCESFULL")
            messagebox.showinfo("MESSAGE", "SUCCESFULLY LOGGED IN")
            doctors(uservalue.get(), pass1value.get())

        else:
            print("FAILED")

        mydb.commit()

    def setvalue():
        print(namevalue.get())
        print(passvalue.get())
        print(mobilevalue.get())
        print(addressvalue.get())
        print(emailvalue.get())
        if (namevalue.get() == ""):
            messagebox.showinfo("ALERT", "COMPUSORY TO FILL username")

        if (passvalue.get() == ""):
            messagebox.showinfo("ALERT", "COMPUSORY TO FILL password")
        if (addressvalue.get() == ""):
            messagebox.showinfo("ALERT", "COMPUSORY TO FILL address")
        if (mobilevalue.get() == ""):
            messagebox.showinfo("ALERT", "COMPUSORY TO FILL mobile")
        if (emailvalue.get() == ""):
                messagebox.showinfo("ALERT", "COMPUSORY TO FILL email")
        mycursor = mydb.cursor()
        sql = "insert into signup(NAME,PASSWORD,MOBILE,ADDRESS,EMAIL)values(%s,%s,%s,%s,%s)"
        val = (namevalue.get(), passvalue.get(), mobilevalue.get(), addressvalue.get(), emailvalue.get())
        mycursor.execute(sql, val)
        messagebox.showinfo("MESSAGE", "!!HURRAYYY WELCOME!!")
        mydb.commit()

    mydb = mysql.connector.connect(
        host="localhost"
             "",
        user="root",
        passwd="Hem1234@*",
        database="SUYAL"
    )


    root.title("STRAYCARE")
    top = Frame(root, bd=2, padx=100, pady=100, relief=SOLID, bg="green")
    top.place(x=900, y=390)
    photo = PhotoImage(file="pro.png")
    imagel = Label(image=photo)
    imagel.pack()

    head = Label(root, text="LOGIN PAGE", font=("Comic Sans MS", 15, "bold"), bg="green")
    head.place(x=0, y=350)

    user = Label(top, text="USERNAME", font=("Comic Sans MS", 10, "bold"), bg="green")
    passw = Label(top, text="PASSWORD", font=("Comic Sans MS", 10, "bold"), bg="green")

    user.grid(row=1, column=0)
    passw.grid(row=2, column=0)
    uservalue = StringVar()
    pass1value = StringVar()
    userentry = Entry(top, textvariable=uservalue)
    passentry = Entry(top, textvariable=pass1value)
    userentry.grid(row=1, column=1)
    passentry.grid(row=2, column=1)
    button = Button(top, text="SUBMIT", command=getvalue, font=("Comic Sans MS", 15, "bold"), bg="green")
    button.grid()

    head = Label(root, text="SIGNUP PAGE",font=("Comic Sans MS",15,"bold"), bg="green")
    head.place(x=900, y=350)
    topL = Frame(root, bd=2, padx=100, pady=100, relief=SOLID,bg="green")
    topL.place(x=0, y=390)
    d=Label(topL,text="DOCTOR NGO", bg="green")
    d.grid()
    NAME = Label(topL, text="NAME", font=("Comic Sans MS", 10, "bold"), bg="green")
    PASSWORD = Label(topL, text="PASSWORD", font=("Comic Sans MS", 10, "bold"), bg="green")
    MOBILE = Label(topL, text="MOBILE", font=("Comic Sans MS", 10, "bold"), bg="green")
    ADDRESS = Label(topL, text="ADDRESS", font=("Comic Sans MS", 10, "bold"), bg="green")
    EMAIL = Label(topL, text="EMAIL", font=("Comic Sans MS", 10, "bold"), bg="green")

    NAME.grid(row=1, column=0)
    PASSWORD.grid(row=2, column=0)
    MOBILE.grid(row=3, column=0)
    ADDRESS.grid(row=4, column=0)
    EMAIL.grid(row=5, column=0)
    namevalue = StringVar()
    passvalue = StringVar()
    mobilevalue = StringVar()
    addressvalue = StringVar()
    emailvalue = StringVar()
    mobileentry = Entry(topL, textvariable=mobilevalue)
    passentry = Entry(topL, textvariable=passvalue)
    nameentry = Entry(topL, textvariable=namevalue)
    addressentry = Entry(topL, textvariable=addressvalue)
    emailentry = Entry(topL, textvariable=emailvalue)
    nameentry.grid(row=1, column=1)
    passentry.grid(row=2, column=1)
    mobileentry.grid(row=3, column=1)
    addressentry.grid(row=4, column=1)
    emailentry.grid(row=5, column=1)
    button = Button(topL, text="SUBMIT", command=setvalue, font=("Comic Sans MS", 15, "bold"), bg="green")
    button.grid(row=6, column=1)
def screen2():

    def getvalue():
        if (uservalue.get() == ""):
            messagebox.showinfo("ALERT", "COMPUSORY TO FILL username")

        if (pass1value.get() == ""):
            messagebox.showinfo("ALERT", "COMPUSORY TO FILL password")
        print(uservalue.get())
        print(pass1value.get())
        mycursor = mydb.cursor()
        sql = "select * from signupu where NAME=%s and PASSWORD=%s"
        val = (uservalue.get(), pass1value.get())
        mycursor.execute(sql, val)
        res = mycursor.fetchall()
        if res:
            print("sUCCESFULL")
            messagebox.showinfo("MESSAGE","SUCCESFULLY SIGNED UP")

            users(uservalue.get(),pass1value.get())

        else:
            messagebox.showinfo("MESSAGE", "FAILED")
            print("FAILED")

        mydb.commit()

    def setvalue():
        print(namevalue.get())
        print(passvalue.get())
        print(mobilevalue.get())
        print(addressvalue.get())
        print(emailvalue.get())
        if (namevalue.get() == ""):
            messagebox.showinfo("ALERT", "COMPUSORY TO FILL username")

        if (passvalue.get() == ""):
            messagebox.showinfo("ALERT", "COMPUSORY TO FILL password")
        if (addressvalue.get() == ""):
            messagebox.showinfo("ALERT", "COMPUSORY TO FILL address")
        if (mobilevalue.get() == ""):
            messagebox.showinfo("ALERT", "COMPUSORY TO FILL mobile")
        if (emailvalue.get() == ""):
            messagebox.showinfo("ALERT", "COMPUSORY TO FILL email")
        mycursor = mydb.cursor()
        sql = "insert into signupu(NAME,PASSWORD,MOBILE,ADDRESS,EMAIL)values(%s,%s,%s,%s,%s)"
        val = (namevalue.get(), passvalue.get(), mobilevalue.get(), addressvalue.get(), emailvalue.get())
        mycursor.execute(sql, val)
        messagebox.showinfo("MESSAGE", "!!!HURRAY WELCOME!!!")
        mydb.commit()

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Hem1234@*",
        database="SUYAL"
    )


    root.title("STRAYCARE")



    top = Frame(root, bd=2, padx=100, pady=100, relief=SOLID,bg="green")
    top.place(x=900, y=390)
    head = Label(root, text="LOGIN PAGE", bg="green", font=("Comic Sans MS", 15, "bold"))
    head.place(x=0, y=350)

    user = Label(top, text="USERNAME", font=("Comic Sans MS", 10, "bold"), bg="green")
    passw = Label(top, text="PASSWORD", font=("Comic Sans MS", 10, "bold"), bg="green")

    user.grid(row=1, column=0)
    passw.grid(row=2, column=0)
    uservalue = StringVar()
    pass1value = StringVar()
    userentry = Entry(top, textvariable=uservalue)
    passentry = Entry(top, textvariable=pass1value)
    userentry.grid(row=1, column=1)
    passentry.grid(row=2, column=1)
    button = Button(top, text="SUBMIT", command=getvalue, font=("Comic Sans MS", 15, "bold"), bg="green")
    button.grid()
    top = Frame(root, bd=2, padx=100, pady=100, relief=SOLID)
    top.place(x=500, y=190)
    head = Label(root, text="SIGNUP PAGE", font=("Comic Sans MS", 15, "bold"), bg="green")
    head.place(x=900, y=350)
    topL = Frame(root, bd=2, padx=100, pady=100, relief=SOLID,bg="green")
    topL.place(x=0, y=390)
    d = Label(topL, text="USERS", bg="green")
    d.grid(row=0,column=0)
    NAME = Label(topL, text="NAME", font=("Comic Sans MS", 10, "bold"), bg="green")
    PASSWORD = Label(topL, text="PASSWORD", font=("Comic Sans MS", 10, "bold"), bg="green")
    MOBILE = Label(topL, text="MOBILE", font=("Comic Sans MS", 10, "bold"), bg="green")
    ADDRESS = Label(topL, text="ADDRESS", font=("Comic Sans MS", 10, "bold"), bg="green")
    EMAIL = Label(topL, text="EMAIL", font=("Comic Sans MS", 10, "bold"), bg="green")

    NAME.grid(row=1, column=0)
    PASSWORD.grid(row=2, column=0)
    MOBILE.grid(row=3, column=0)
    ADDRESS.grid(row=4, column=0)
    EMAIL.grid(row=5, column=0)
    namevalue = StringVar()

    passvalue = StringVar()
    mobilevalue = StringVar()
    addressvalue = StringVar()
    emailvalue = StringVar()
    mobileentry = Entry(topL, textvariable=mobilevalue)
    passentry = Entry(topL, textvariable=passvalue)
    nameentry = Entry(topL, textvariable=namevalue)
    addressentry = Entry(topL, textvariable=addressvalue)
    emailentry = Entry(topL, textvariable=emailvalue)
    nameentry.grid(row=1, column=1)
    passentry.grid(row=2, column=1)
    mobileentry.grid(row=3, column=1)
    addressentry.grid(row=4, column=1)
    emailentry.grid(row=5, column=1)
    button = Button(topL, text="SUBMIT", command=setvalue, font=("Comic Sans MS", 15, "bold"), bg="green")
    button.grid(row=6, column=1)
by=Button(text="DOCTORS",command=screen1,width="10",height="2",bg="green",font=("Comic Sans MS",20,"bold"))
by.place(x=400,y=100)
by=Button(text="USER",command=screen2,width="10",height="2",bg="green",font=("Comic Sans MS",20,"bold"))
by.place(x=800,y=100)

root.mainloop()