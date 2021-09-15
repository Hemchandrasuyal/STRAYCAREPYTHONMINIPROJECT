import smtplib as s
def HELP():
    ob = s.SMTP("smtp.gmail.com", 587)
    ob.starttls()
    ob.login("harshitsuyal4@gmail.com", "Hem1234@*")
    subject = "hello from python                  goood day help"
    body = "STRAYCARE is a project made by me helllloo"
    message = "Subject:{}\n\n{}".format(subject, body)
    listofAddress = ["harshitsuyal56@gmail.com"]
    ob.sendmail("harshitsuyal4@gmail.com", listofAddress, message)
    print("Successfully sent email")


