from tkinter import *
from tkinter import messagebox, simpledialog
import mysql.connector
import tkinter as tk
from datetime import *

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', database='Lifechoices_Online',
                               host='127.0.0.1',
                               auth_plugin='mysql_native_password')
mycursor = mydb.cursor()
mycursor1 = mydb.cursor()


def verify():
    newwindow = Tk()
    newwindow.title("LOGIN")
    root.withdraw()
    newwindow.geometry("400x250")

    # date and time
    date = datetime.now()
    date_label = Label(newwindow)
    date_label.pack()
    date_label.config(text="Date" + date.strftime("%d/%m/%y %H:%M"))

    lbluser = tk.Label(newwindow, text="Enter username", bg="grey")
    lbluser.pack()
    username = tk.Entry(newwindow, width=35)
    username.pack(pady=5)
    lblpassword = tk.Label(newwindow, text="Please enter password", bg="grey")
    lblpassword.pack()
    password = tk.Entry(newwindow, width=35)
    password.pack(pady=5)

    def check2():

        user_verification = username.get()
        pass_verification = password.get()
        sql = "select * from users where user_name = %s and password = %s"
        mycursor.execute(sql, [user_verification, pass_verification])

        results = mycursor.fetchall()
        if results:

            for i in results:
                logged()
                break
        else:
            failed()

    Loginbtn = tk.Button(newwindow, text="SUBMIT", bg="skyblue", command=check2)

    Loginbtn.pack()



def logged():
    x = datetime.now()
    y = x.strftime("%H:%M")
    myuser = simpledialog.askstring("Login", "Please enter your username ", parent=root)
    exe = "INSERT INTO logged VALUES (%s, curtime(), NULL)"
    mycursor.execute(exe, [myuser])
    mydb.commit()
    messagebox.showinfo("Successful", "You have successfully logged in")
    window3 = Tk()
    window3.title("Lifechoices Online")
    window3.geometry("400x200")
    signIn = datetime.now()
    x = signIn.strftime("%H:%M:%S")

    # date and time
    date = datetime.now()
    date_label = Label(window3)
    date_label.pack()
    date_label.config(text="Date" + date.strftime("%d/%m/%y %H:%M"))

    def time():
        messagebox.showinfo("logged out", "You have successfully logged out")

        x = datetime.now()
        y = x.strftime("%H:%M")
        myuser = simpledialog.askstring("Log Out", "Please enter your username ", parent=root)
        exe = "UPDATE logged SET signout = curtime()where user_name= %s"
        mycursor.execute(exe, [myuser])
        mydb.commit()

        window3.withdraw()

    Loginbtn1 = tk.Button(window3, text="LOGOUT", command=time)
    Loginbtn1.pack()


def failed():
    messagebox.showinfo("Unsuccessful", "Please try again !")


def register():
    window2 = Tk()
    root.withdraw()
    window2.configure(bg='skyblue')

    window2.title("REGISTER-NEW USER")
    window2.geometry("400x200")

    # date and time
    date = datetime.now()
    date_label = Label(window2)
    date_label.pack()
    date_label.config(text="Date" + date.strftime("%d/%m/%y %H:%M"))

    lbluser = tk.Label(window2, text="Enter username", bg="grey")
    lbluser.pack()
    username = tk.Entry(window2, width=35)
    username.pack()
    lbluser1 = tk.Label(window2, text="Enter fullname", bg="grey")
    lbluser1.pack()
    firstname = tk.Entry(window2, width=35)
    firstname.pack()
    lblpassword = tk.Label(window2, text="Please enter password", bg="grey")
    lblpassword.pack()
    password = tk.Entry(window2, width=35)
    password.pack()

    def create():
        if len(firstname.get()) == 0:
            messagebox.showinfo("Error", "Please enter your fullname")
            quit()
        if len(username.get()) == 0:
            messagebox.showinfo("Error", "PLease enter a username")
            quit()
        if len(password.get()) == 0:
            messagebox.showinfo("Error", "Please enter a Password")
            quit()
        user = (firstname.get(), username.get(), password.get())
        exe = "INSERT INTO users(full_name,user_name, password) VALUES(%s,%s, %s)"
        mycursor.execute(exe, user)
        mydb.commit()
        messagebox.showinfo("Lifechoices online management", "You have successfully registered")
        window2.withdraw()
        verify()


    Loginbtn = tk.Button(window2, text="REGISTER", bg="skyblue", command=create)
    Loginbtn.pack()

    window2.mainloop()


def admin():
    window4 = Tk()
    window4.title("ADMINISTRATION")
    window4.geometry("400x200")
    root.withdraw()

    # date and time
    date = datetime.now()
    date_label = Label(window4)
    date_label.pack()
    date_label.config(text="Date" + date.strftime("%d/%m/%y %H:%M"))

    lbluser = tk.Label(window4, text="Enter username", bg="grey")
    lbluser.pack()
    username = tk.Entry(window4, width=35)
    username.pack(pady=5)
    lblpassword = tk.Label(window4, text="Please enter password", bg="grey")
    lblpassword.pack()
    password = tk.Entry(window4, width=35)
    password.pack(pady=5)

    def adminy():
        if len(username.get()) == 0:
            messagebox.showinfo("Error", "PLease enter a username")
            quit()
        if len(password.get()) == 0:
            messagebox.showinfo("Error", "Please enter a Password")
            quit()
        user = (username.get(), password.get())
        exe = "INSERT INTO admin(user_name, password) VALUES(%s,%s)"
        messagebox.showinfo("Lifechoices online management", "Details successfully verified")

        window4.destroy()

        windownew = Tk()
        windownew.geometry("700x600")
        windownew.resizable(False, False)
        windownew.title("Admin Page")
        liLb = Label(windownew, text="ID:")
        liName = Listbox(windownew, width=20)
        li2Lb = Label(windownew, text="Username:")
        liD = Listbox(windownew, width=20)
        liTL = Label(windownew, text="Password")
        liT = Listbox(windownew, width=20)
        #######################################
        lbU = Label(windownew, text="Username:")
        Liu = Listbox(windownew, width=20)
        lbD = Label(windownew, text="SignIn Time:")
        Lid = Listbox(windownew, width=20)
        LiTiL = Label(windownew, text="SignOut Time:")
        LiTi = Listbox(windownew, width=20)


        def s():
            mycursor.execute("SELECT ID FROM users")

            ID = mycursor.fetchall()

            for x in ID:
                liName.insert(END, x)

            liName.insert(END, str(mycursor.rowcount) + " rows")

            mycursor.execute("SELECT user_name FROM users")

            name = mycursor.fetchall()

            for x in name:
                liD.insert(END, x)

            liD.insert(END, str(mycursor.rowcount) + " rows")

            mycursor.execute("SELECT password FROM users")

            uName = mycursor.fetchall()
            for x in uName:
                liT.insert(END, x)
            liT.insert(END, str(mycursor.rowcount) + " rows")

            mycursor.execute("SELECT user_name FROM logged")

            tUn = mycursor.fetchall()
            for x in tUn:
                Liu.insert(END, x)
            Liu.insert(END, str(mycursor.rowcount) + " rows")

            mycursor.execute("SELECT signintime FROM logged")

            d = mycursor.fetchall()
            for x in d:
                Lid.insert(END, x)
            Lid.insert(END, str(mycursor.rowcount) + " rows")

            mycursor.execute("SELECT signout FROM logged")

            timeIn = mycursor.fetchall()
            for x in timeIn:
                LiTi.insert(END, x)
            LiTi.insert(END, str(mycursor.rowcount) + " rows")

            mycursor.execute("SELECT signout FROM logged")

            timeIn = mycursor.fetchall()
            for x in timeIn:
                LiT0.insert(END, x)
            LiT0.insert(END, str(mycursor.rowcount) + " rows")
        showbtn = Button(windownew, text="show database content", command=s)

        def building():
            sql = "SELECT * FROM logged"
            mycursor.execute(sql)
            results1 = mycursor.fetchall()
            messagebox.showinfo("In builidng","Currently"+str(mycursor.rowcount))




        showbtn2 = Button(windownew, text="how many people are in the building?",command=building)



        liLb.place(x=0, y=0)
        liName.place(x=0, y=50)
        li2Lb.place(x=50, y=0)
        liD.place(x=50, y=50)
        liTL.place(x=150, y=0)
        liT.place(x=150, y=50)
        lbU.place(x=0, y=250)
        Liu.place(x=0, y=300)
        lbD.place(x=150, y=250)
        Lid.place(x=150, y=300)
        LiTiL.place(x=300, y=250)
        LiTi.place(x=300, y=300)
        showbtn.place(x=0, y=500)
        showbtn2.place(x=200,y=500)



        adBtn = Button(windownew, text="Login as Admin", command=adminIn)
        windownew.mainloop()

    Loginbtn = tk.Button(window4, text="LOGIN", bg="skyblue", command=adminy)
    Loginbtn.pack()


####################################################################################################
# first page
root = tk.Tk()
root.configure(bg='black')
root.geometry("800x550")
root.title("Lifechoices Online Management")

# picture

photo = PhotoImage(file="chel.ppm")
w = Label(root, image=photo)
w.pack()

label1 = tk.Label(root, text="Welcome to Lifechoices Online portal", bg="grey", width=50)
label1.pack()
label2 = tk.Label(root, text="SELECT 1 of the options below !", bg="grey", width=50)
label2.pack()

# date and time
date = datetime.now()
date_label = Label(root)
date_label.pack()
date_label.config(text="Date" + date.strftime("%d/%m/%y %H:%M"))

Loginbtn = tk.Button(root, text="Login", bg="skyblue", command=verify, width=25)
Loginbtn.pack(pady=5)
Registerbtn = tk.Button(root, text="Register new user", bg="skyblue", width=25, command=register)
Registerbtn.pack(pady=5)
Adminbtn = tk.Button(root, text="Admin login", bg="skyblue", width=25, command=admin)
Adminbtn.pack(pady=5)

root.mainloop()
