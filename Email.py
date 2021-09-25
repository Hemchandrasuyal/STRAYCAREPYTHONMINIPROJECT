import smtplib as s
import mysql.connector
def HELP(j,a,b,d):

    ob = s.SMTP("smtp.gmail.com", 587)
    ob.starttls()
    ob.login("harshitsuyal4@gmail.com", "Hem1234@*")
    subject = "hello "
    body = "STRAYCARE "
    message = "Subject:{}\n\n{}".format(subject, body)
    listofAddress = [j]
    ob.sendmail("harshitsuyal4@gmail.com", listofAddress, message)
    print("Successfully sent email")
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Hem1234@*",
        database="SUYAL"
    )
    mycursor = mydb.cursor()
    print(j[0])
    sql = "insert into usermsg1 (MESSAGE,EMAIL,NAME,MOBILE,EMAILSEND) values(%s,%s,%s,%s,%s)"
    var = (body, j[0],a,b,d)
    mycursor.execute(sql, var)
    mydb.commit()




