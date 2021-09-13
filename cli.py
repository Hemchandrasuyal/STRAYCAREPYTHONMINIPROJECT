
from tkinter import*

import mysql.connector


def getvalue():
    print(uservalue.get())
    print(pass1value.get())
    mycursor = mydb.cursor()
    sql = "select * from signup where NAME=%s and PASSWORD=%s"
    val = (uservalue.get(), pass1value.get())
    mycursor.execute(sql, val)
    res = mycursor.fetchall()
    if res:
        for i in res:
            print("sUCCESFULL")
            Label(text="SUCCESFULLY SIGNED IN", bg="GREEN", font="40").place(x=520, y=390)
    else:
        print("FAILED")
        Label(text="FAILED", bg="red", font="40").place(x=520, y=390)
    mydb.commit()


def setvalue():
    print(namevalue.get())
    print(passvalue.get())
    print(mobilevalue.get())
    print(addressvalue.get())
    print(emailvalue.get())
    mycursor = mydb.cursor()
    sql = "insert into signup(NAME,PASSWORD,MOBILE,ADDRESS,EMAIL)values(%s,%s,%s,%s,%s)"
    val = (namevalue.get(), passvalue.get(), mobilevalue.get(), addressvalue.get(), emailvalue.get())
    mycursor.execute(sql, val)
    Label(text="huraay thanks!!!!!!!", bg="GREEN", font="40").place(x=0, y=390)
    mydb.commit()


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Hem1234@*",
    database="SUYAL"
)


def screen2():
    root = Tk()
    root.title("STRAYCARE")
    root.geometry('500x500')
    head = Label(root, text="LOGIN PAGE", font=100)
    head.place(x=570, y=130)
    headd = Label(root, text="DOCTORS AND NGO", font=60)
    headd.place(x=570, y=150)

    top = Frame(root, bd=2, padx=50, pady=70, relief=SOLID, bg="grey")
    top.place(x=500, y=190)

    user = Label(top, text="USERNAME")
    passw = Label(top, text="PASSWORD")

    user.grid(row=1, column=0)
    passw.grid(row=2, column=0)
    uservalue = StringVar()
    pass1value = StringVar()
    userentry = Entry(top, textvariable=uservalue)
    passentry = Entry(top, textvariable=pass1value)
    userentry.grid(row=1, column=1)
    passentry.grid(row=2, column=1)
    button = Button(top, text="SUBMIT", command=getvalue)
    button.grid()
    top = Frame(root, bd=2, padx=50, pady=70, relief=SOLID, bg="grey")
    top.place(x=500, y=190)
    head = Label(root, text="SIGN PAGE", font=100)
    head.place(x=0, y=130)
    headd = Label(root, text="DOCTORS AND NGO", font=60)
    headd.place(x=0, y=150)
    topL = Frame(root, bd=2, padx=50, pady=70, relief=SOLID, bg="grey")
    topL.place(x=0, y=190)
    NAME = Label(topL, text="NAME")
    PASSWORD = Label(topL, text="PASSWORD")
    MOBILE = Label(topL, text="MOBILE")
    ADDRESS = Label(topL, text="ADDRESS")
    EMAIL = Label(topL, text="EMAIL")

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
    button = Button(topL, text="SUBMIT", command=setvalue)
    button.grid(row=6, column=1)
    root.mainloop()
