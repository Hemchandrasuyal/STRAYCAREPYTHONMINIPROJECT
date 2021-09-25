from functools import partial
from tkinter import *
from Email import *

import mysql.connector
def users(x,y):

    root1 = Tk()
    root1.geometry("1500x1500")
    root1.title("USERS")
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Hem1234@*",
        database="SUYAL"
    )

    mycursor = mydb.cursor()
    sql = "select NAME from signupu where NAME=%s and PASSWORD=%s"
    val=(x,y)
    mycursor.execute(sql,val)
    res = mycursor.fetchall()
    for i in res:
        for j in i:
            a = j

    sql = "select MOBILE from signupu where NAME=%s and PASSWORD=%s"
    val = (x, y)
    mycursor.execute(sql,val)
    res = mycursor.fetchall()
    for i in res:
        for j in i:
            b = j

    sql = "select ADDRESS from signupu where NAME=%s and PASSWORD=%s"
    val = (x, y)
    mycursor.execute(sql,val)
    res = mycursor.fetchall()
    for i in res:
        for j in i:
            c = j

    sql = "select EMAIL from signupu where NAME=%s and PASSWORD=%s"
    val = (x, y)
    mycursor.execute(sql,val)
    res = mycursor.fetchall()
    for i in res:
        for j in i:
            d = j


    profile = Frame(root1, bd=2, padx=50, pady=100, relief=SOLID, bg="lightgreen")
    profile.place(x=0, y=80)
    mainDOCT=Frame(root1, bd=2, relief=SOLID, padx=80,  bg="lightgreen")
    mainDOCT.place(x=750, y=80)
    sqlN = "select NAME from signup"
    mycursor.execute(sqlN)
    resN = mycursor.fetchall()
    Label(mainDOCT, text="NAME", bg="lightgreen", font=("Comic Sans MS", 16, "bold"), fg="red").grid(column=0)
    for i in resN:
        Label(mainDOCT, text=i, bg="lightgreen", font=("Comic Sans MS", 11, "bold"), fg="blue").grid(column=0)
    sqlA = "select  ADDRESS  from signup"
    mycursor.execute(sqlA)
    resA = mycursor.fetchall()
    Label(mainDOCT, text="ADDRESS", bg="lightgreen", font=("Comic Sans MS", 16, "bold"), fg="red").grid(row=0,column=3)
    r=1
    for j in resA:

        Label(mainDOCT, text=j, bg="lightgreen", font=("Comic Sans MS", 11, "bold"), fg="green").grid(row=r,column=3)
        r=r+1
    sqlM = "select  MOBILE  from signup"
    mycursor.execute(sqlM)
    resM = mycursor.fetchall()
    r=1
    Label(mainDOCT, text="MOBILE", bg="lightgreen", font=("Comic Sans MS", 16, "bold"), fg="red").grid(row=0,column=6)
    for j in resM:
        Label(mainDOCT, text=j, bg="lightgreen", font=("Comic Sans MS", 12, "bold"), fg="green").grid(row=r,column=6)
        r=r+1
    sqlE = "select  EMAIL  from signup"
    mycursor.execute(sqlE)
    resE = mycursor.fetchall()
    Label(mainDOCT, text="EMAIL", bg="lightgreen", font=("Comic Sans MS", 16, "bold"), fg="red").grid(row=0, column=9)
    r = 1

    def HELP1(j,a,b,d):
        print(j)

        HELP(j,a,b,d)


    for j in resE:

        Button(mainDOCT, text=j, bg="lightgreen", font=("Comic Sans MS", 8, "bold"), fg="blue",command=partial(HELP1,j,a,b,d)).grid(row=r,column=9)
        r = r+1


    Label(root1, text="PROFILE FOR USERS", font=("Comic Sans MS", 30, "bold")).place(x=0, y=0)
    Label(root1, text="DOCTORS near youuuu", font=("Comic Sans MS", 30, "bold")).place(x=750,y=0)
    Label(profile, text="NAME-", font=("Comic Sans MS", 15, "bold"), bg="lightgreen").grid(row=0, column=0)
    Label(profile, text=a, font=("Comic Sans MS", 15, "bold"), bg="lightgreen",fg="blue").grid(row=0, column=4)
    Label(profile, text="MOBILE-", font=("Comic Sans MS", 15, "bold"), bg="lightgreen").grid()
    Label(profile, text=b, font=("Comic Sans MS", 15, "bold"), bg="lightgreen",fg="blue").grid(row=1, column=4)
    Label(profile, text="EMAIL-", font=("Comic Sans MS", 15, "bold"), bg="lightgreen").grid()
    Label(profile, text=c, font=("Comic Sans MS", 15, "bold"), bg="lightgreen",fg="blue").grid(row=2, column=4)
    Label(profile, text="ADDRESS-", font=("Comic Sans MS", 15, "bold"), bg="lightgreen").grid()
    Label(profile, text=d, font=("Comic Sans MS", 15, "bold"), bg="lightgreen",fg="blue").grid(row=3, column=4)
    root1.mainloop()





