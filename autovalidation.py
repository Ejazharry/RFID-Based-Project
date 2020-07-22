from tkinter import *
from tkinter import messagebox as ms
import sqlite3
import time
time.sleep(5)
window = Tk()
window.geometry("266x208")
window.title("Info")
def DESTROY():
      window.destroy();
Label(window, text='Scan your ID', font=('', 20), pady=5, padx=5).grid(row=6, column=2)
Button(window, text='OK', bd=2, font=('', 8), padx=3, pady=3, bg="light blue",
               command=DESTROY).place(x=100, y=50)
 
window.mainloop() 
#from New import *
from CardRead import text
root = Tk()
root.title("VALIDATION")
width = 400
height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="white")

with sqlite3.connect('trail.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (IDNUMBER INTEGER PRIMARY KEY , USN VARCHAR , NAME VARCHAR NOT NULL, '
          'BRANCH VARCHAR NOT NULL, SCHOLAR_TYPE VARCHAR NOT NULL, MOBILE_NO LONG UNIQUE NOT NULL,EMAIL VARCHAR NOT '
          'NULL);')
db.commit()
db.close()


class main:
    
    def __init__(self, master):
        # Window
        self.master = master
        self.IdNumber = StringVar()
        self.IDNUMBER = StringVar()
        self.USN = StringVar()
        self.NAME = StringVar()
        self.BRANCH = StringVar()
        self.SCHOLAR_TYPE = StringVar()
        self.MOBILE_NO = StringVar()
        self.EMAIL = StringVar()
        # Create Widgets
        self.widgets()
        

    #def login(self):
        # Establish Connection
    
        self.IdNumber.set(text)
        if self.IdNumber.get() == '':
            ms.showerror('Error!', 'please enter the IdNumber.')
        else:
            with sqlite3.connect('trail.db') as db:
                c = db.cursor()
                # Find user If there is any take proper action
                find_user = 'SELECT * FROM user WHERE IDNUMBER = ?'
                c.execute(find_user, [(self.IdNumber.get())])
                result = c.fetchall()
            if result:
                self.logf.pack_forget()
                self.head['text'] = 'WELCOME!!!'
                self.head['pady'] = 20

            else:
                ms.showerror('Oops!', 'ID Not Found!! SingUp if new user.')

            
     
    def new_user(self):
        # Establish Connection
        if (self.IDNUMBER.get() == '' or self.USN.get() == '' or self.NAME.get() == '' or self.BRANCH.get() == '' or self.SCHOLAR_TYPE.get() == '' or self.MOBILE_NO.get() == '' or self.EMAIL.get() == ''):
            ms.showerror('Error!', 'Please fill all the details .')
        else:
            with sqlite3.connect('trail.db') as db:
                c = db.cursor()
                # Find Existing username if any take proper action
                find_user = 'SELECT * FROM user WHERE IDNUMBER = ?'
                c.execute(find_user, [(self.IDNUMBER.get())])
            if c.fetchall():
                ms.showerror('Error!', 'ALREADY REGISTERED.')
            else:
                ms.showinfo('Success!', 'Account Created!')
                self.log()
                # Create New Account
                insert = 'INSERT INTO user(IDNUMBER, USN, NAME, BRANCH, SCHOLAR_TYPE, MOBILE_NO, EMAIL) VALUES(?,?,' \
                         '?,?,?,?,?) '
                c.execute(insert, [(self.IDNUMBER.get()), (self.USN.get()), (self.NAME.get()), (self.BRANCH.get()),
                                   (self.SCHOLAR_TYPE.get()), (self.MOBILE_NO.get()), (self.EMAIL.get())])
                db.commit()
    
    
    def login(self):
        # Establish Connection
        #self.IdNumber.set(text)
        if self.IdNumber.get() == '':
            ms.showerror('Error!', 'please enter the IdNumber.')
        else:
            with sqlite3.connect('trail.db') as db:
                c = db.cursor()
                # Find user If there is any take proper action
                find_user = 'SELECT * FROM user WHERE IDNUMBER = ?'
                c.execute(find_user, [(self.IdNumber.get())])
                result = c.fetchall()
            if result:
                self.logf.pack_forget()
                self.head['text'] = 'WELCOME!!!'
                self.head['pady'] = 20

            else:
                ms.showerror('Oops!', 'ID Not Found.')


    
    def log(self):
        self.IdNumber.set(text)
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()

    def cr(self):
        self.IDNUMBER.set('')
        self.USN.set('')
        self.NAME.set('')
        self.BRANCH.set('')
        self.SCHOLAR_TYPE.set('')
        self.MOBILE_NO.set('')
        self.EMAIL.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()

    def widgets(self):
        self.head = Label(self.master, text='LOGIN', font=('', 10), pady=5, bg="white")
        self.head.pack()
        self.logf = Frame(self.master, padx=10, pady=10)
        Label(self.logf, text='ID NUMBER', font=('', 10), pady=5, padx=5).grid(row=1, column=0)
        Entry(self.logf, textvariable=self.IdNumber, bd=5, font=('', 10)).grid(row=1, column=1)
        Button(self.logf, text=' Login ', bd=3, font=('', 10), padx=1, pady=1, bg="light green",command=self.login).grid(row=2, column=1)
        Button(self.logf, text=' Sign Up', bd=3, font=('', 10), padx=1, pady=1, bg="light yellow",
               command=self.cr).grid(row=2, column=0)
        Label(self.logf, text='If new user!! ', font=('', 7), pady=5, padx=5).grid(row=3, column=1)
        Label(self.logf, text='If user!! ', font=('', 7), pady=5, padx=5).grid(row=3, column=0)
        self.logf.pack()

        self.crf = Frame(self.master, padx=10, pady=10)
        Label(self.crf, text='IDNUMBER ', font=('', 10), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.IDNUMBER, bd=5, font=('', 8)).grid(row=0, column=1)
        Label(self.crf, text='USN: ', font=('', 10), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.USN, bd=5, font=('', 8)).grid(row=1, column=1)
        Label(self.crf, text='NAME: ', font=('', 10), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.NAME, bd=5, font=('', 8)).grid(row=2, column=1)
        Label(self.crf, text='BRANCH: ', font=('', 10), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.BRANCH, bd=5, font=('', 8)).grid(row=3, column=1)
        Label(self.crf, text='SCHOLAR_TYPE: ', font=('', 10), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.SCHOLAR_TYPE, bd=5, font=('', 8)).grid(row=4, column=1)
        Label(self.crf, text='MOBILE_NO: ', font=('', 10), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.MOBILE_NO, bd=5, font=('', 8)).grid(row=5, column=1)
        Label(self.crf, text='EMAIL: ', font=('', 10), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.EMAIL, bd=3, font=('', 8)).grid(row=6, column=1)
        Button(self.crf, text='Sigh Up', bd=2, font=('', 8), padx=3, pady=3, bg="yellow",
               command=self.new_user).grid()
        Button(self.crf, text='Back to Login', bd=2, font=('', 8), padx=3, pady=3, bg="light blue",
               command=self.log).grid(row=7,column=1)
 
    

main(root)
root.mainloop()