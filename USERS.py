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
            print(j)
    sql = "select EMAIL from signupu where NAME=%s and PASSWORD=%s"
    val = (x, y)
    mycursor.execute(sql,val)
    res = mycursor.fetchall()
    for i in res:
        for j in i:
            d = j
            print(j)

    profile = Frame(root1, bd=2, padx=50, pady=100, relief=SOLID, bg="lightgreen")
    profile.place(x=0, y=80)

    DOCprofileN = Frame(root1, bd=2, padx=10, pady=70, relief=SOLID, bg="lightgreen")
    DOCprofileN.place(x=800, y=100)
    Label(DOCprofileN,text="NAME",font=("Comic Sans MS", 10, "bold"), fg="blue").grid()
    DOCprofileA = Frame(root1, bd=2, padx=10, pady=70, relief=SOLID, bg="lightgreen")
    DOCprofileA.place(x=920, y=100)
    Label(DOCprofileA, text="ADDRESS", font=("Comic Sans MS", 10, "bold"), fg="blue").grid()
    DOCprofileM= Frame(root1, bd=2, padx=10, pady=70, relief=SOLID, bg="lightgreen")
    DOCprofileM.place(x=1020, y=100)
    Label(DOCprofileM, text="MOBILE", font=("Comic Sans MS", 10, "bold"), fg="blue").grid()
    DOCprofileE = Frame(root1, bd=2, padx=10, pady=70, relief=SOLID, bg="lightgreen")
    DOCprofileE.place(x=1120, y=100)
    Label(DOCprofileE, text="EMAIL",font=("Comic Sans MS", 10, "bold"), fg="blue").grid()
    sqlN = "select NAME from signup"
    mycursor.execute(sqlN)
    resN = mycursor.fetchall()
    for i in resN:
        Label(DOCprofileN, text=i, bg="lightgreen",font=("Comic Sans MS", 10, "bold"), fg="blue").grid(column=0)
    sqlA = "select  ADDRESS  from signup"
    mycursor.execute(sqlA)
    resA = mycursor.fetchall()
    for j in resA:
        Label(DOCprofileA, text=j, bg="lightgreen", font=("Comic Sans MS", 10, "bold"), fg="green").grid(column=0)
    sqlM = "select  MOBILE  from signup"
    mycursor.execute(sqlM)
    resM = mycursor.fetchall()
    for j in resM:
        Label(DOCprofileM, text=j, bg="lightgreen", font=("Comic Sans MS", 10, "bold"), fg="green").grid(column=0)
    sqlE = "select  EMAIL  from signup"
    mycursor.execute(sqlE)
    resE = mycursor.fetchall()
    for j in resE:
        Button(DOCprofileE, text=j, bg="lightgreen", font=("Comic Sans MS", 10, "bold"), fg="blue",command=HELP).grid( column=0)

    Label(root1, text="PROFILE FOR USERS", font=("Comic Sans MS", 30, "bold")).place(x=0, y=0)
    Label(root1, text="DOCTORS near youuuu", font=("Comic Sans MS", 30, "bold")).place(x=900,y=0)
    Label(profile, text="NAME-", font=("Comic Sans MS", 15, "bold"), bg="lightgreen").grid(row=0, column=0)
    Label(profile, text=a, font=("Comic Sans MS", 15, "bold"), bg="lightgreen",fg="blue").grid(row=0, column=4)
    Label(profile, text="MOBILE-", font=("Comic Sans MS", 15, "bold"), bg="lightgreen").grid()
    Label(profile, text=b, font=("Comic Sans MS", 15, "bold"), bg="lightgreen",fg="blue").grid(row=1, column=4)
    Label(profile, text="EMAIL-", font=("Comic Sans MS", 15, "bold"), bg="lightgreen").grid()
    Label(profile, text=c, font=("Comic Sans MS", 15, "bold"), bg="lightgreen",fg="blue").grid(row=2, column=4)
    Label(profile, text="ADDRESS-", font=("Comic Sans MS", 15, "bold"), bg="lightgreen").grid()
    Label(profile, text=d, font=("Comic Sans MS", 15, "bold"), bg="lightgreen",fg="blue").grid(row=3, column=4)
    root1.mainloop()





