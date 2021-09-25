from tkinter import *
import mysql.connector


def doctors(x,y):
    root1 = Tk()
    root1.geometry("1500x1500")
    root1.title("DOCTORS")


    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Hem1234@*",
        database="SUYAL"
    )

    mycursor = mydb.cursor()
    sql = "select NAME from signup where NAME=%s and PASSWORD=%s"
    val=(x,y)
    mycursor.execute(sql,val)
    res = mycursor.fetchall()
    for i in res:
        for j in i:
            a = j
    sql = "select MOBILE from signup where NAME=%s and PASSWORD=%s"
    val = (x, y)
    mycursor.execute(sql,val)
    res = mycursor.fetchall()
    for i in res:
        for j in i:
            b = j
            print(j)
    sql = "select EMAIL from signup where NAME=%s and PASSWORD=%s"
    val = (x, y)
    mycursor.execute(sql,val)
    res = mycursor.fetchall()
    for i in res:
        for j in i:
            c = j

    sql = "select ADDRESS from signup where NAME=%s and PASSWORD=%s"
    val = (x, y)
    mycursor.execute(sql,val)
    res = mycursor.fetchall()
    for i in res:
        for j in i:
            d = j
            print(j)

    profile = Frame(root1, bd=2, padx=30, pady=100, relief=SOLID, bg="lightgreen")
    profile.place(x=0, y=80)
    Label(root1, text="PROFILE FOR DOCTORS AND NGO", font=("Comic Sans MS", 30, "bold")).place(x=0, y=0)
    Label(root1, text="HELP THEM", font=("Comic Sans MS", 30, "bold"),fg="red").place(x=800, y=0)
    sql="select * from usermsg1 where EMAIL=%s"
    val=(c,)
    mycursor.execute(sql,val)
    resmsg=mycursor.fetchall()
    ya=100

    for i in resmsg:
        for j in i:

            Label(root1, text=j, font=("Comic Sans MS", 15, "bold"), fg="brown").place(x=800, y=ya)
            ya=ya+40




    Label(profile, text="NAME-", font=("Comic Sans MS", 15, "bold"), bg="lightgreen").grid(row=0, column=0)
    Label(profile, text=a, font=("Comic Sans MS", 15, "bold"), bg="lightgreen").grid(row=0, column=4)
    Label(profile, text="MOBILE-", font=("Comic Sans MS", 15, "bold"), bg="lightgreen").grid()
    Label(profile, text=b, font=("Comic Sans MS", 15, "bold"), bg="lightgreen").grid(row=1, column=4)
    Label(profile, text="EMAIL-", font=("Comic Sans MS", 15, "bold"), bg="lightgreen").grid()
    Label(profile, text=c, font=("Comic Sans MS", 15, "bold"), bg="lightgreen").grid(row=2, column=4)
    Label(profile, text="ADDRESS-", font=("Comic Sans MS", 15, "bold"), bg="lightgreen").grid()
    Label(profile, text=d, font=("Comic Sans MS", 15, "bold"), bg="lightgreen").grid(row=3, column=4)


    root1.mainloop()






