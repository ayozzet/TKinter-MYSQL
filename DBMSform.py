import tkinter as tk
import mysql.connector
from tkinter import *

def submitact():

    #root.bind('<Return>', func)
    user = Username.get()
    passw = password.get()

    print(f"The name entered by you is {user} {passw}")

    logintodb(user, passw)


def logintodb(user, passw):

    # If paswword is enetered by the
    # user
    if passw:
        db = mysql.connector.connect(host ="localhost",
                                     user = user,
                                     password = passw,
                                     db ="flaskapp")
        cursor = db.cursor()

    # If no password is enetered by the
    # user
    else:
        db = mysql.connector.connect(host ="localhost",
                                     user = user,
                                     db ="College")
        cursor = db.cursor()

    # A Table in the database
    savequery = "select * from STUDENT"

    try:
        cursor.execute(savequery)
        myresult = cursor.fetchall()

        # Printing the result of the
        # query
        for x in myresult:
            print(x)
        print("Query Excecuted successfully")

    except:
        db.rollback()
        print("Error occured")


root = tk.Tk()
root.resizable(0,0) #remove maximize button
root.wm_iconbitmap("favicon.ico")
root.geometry("400x250")
root.title("Medical Access Form - Hospital Az-Zahra")

#def func(event):
#    print("You hit return.")
#root.bind('<Return>', func)

#def submitact():
#    print("You clicked the button")


# Definging the first row
lblfrstrow = tk.Label(root, text ="Username :", )
lblfrstrow.place(x = 40, y = 20)

Username = tk.Entry(root, width = 70)
Username.place(x = 120, y = 20, width = 150)

lblsecrow = tk.Label(root, text ="Password :")
lblsecrow.place(x = 40, y = 50)

password = tk.Entry(root, width = 70, show='*')
password.place(x = 120, y = 50, width = 150)

submitbtn = tk.Button(root, text ="Login",
                      bg ='white', fg = 'red',command = submitact)
submitbtn.place(x = 120, y = 80, width = 150)

root.mainloop()
