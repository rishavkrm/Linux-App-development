from importlib.abc import TraversableResources
from tkinter import *
import bcrypt
from home import Home
import customtkinter
from PIL import ImageTk, Image

# def get_database():
#         from pymongo import MongoClient
#         import pymongo

#         # Provide the mongodb atlas url to connect python to mongodb using pymongo
#         CONNECTION_STRING = "mongodb+srv://rishavkrm:GXWlRjUXwRloTvoc@cluster0.qtcanpa.mongodb.net/csquare"

#         # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
#         from pymongo import MongoClient
#         client = MongoClient(CONNECTION_STRING)

#         # Create the database for our example (we will use the same database throughout the tutorial
#         return client['csquare']

class NewLogin:
    def __init__(self, window):
        super().__init__()
        self.parent_window = window
        self.main_window = Frame(window)
        self.head = Label (self.main_window, text="New Login")
        self.idLabel = Label(self.main_window, text="Enter your Id below")
        self.userId = Entry(self.main_window)
        self.passLabel = Label(self.main_window, text="Enter Password")
        self.password = Entry(self.main_window)
        self.submit = Button(self.main_window, text="Submit", command=self.cloudAuth)
        self.status = Label(self.main_window, text="")
        self.backbtn = Button(self.main_window, text="Back", command=self.back)

        self.main_window.pack()
        self.head.pack()
        self.idLabel.pack()
        self.userId.pack()
        self.passLabel.pack()
        self.password.pack()
        self.submit.pack()
        self.status.pack()
        self.backbtn.pack()

    def checkLocalTextPassword(self):
        passFile = open("localPassword/password.txt", "r")
        currId = self.userId.get()
        currPass = self.password.get().encode("utf8")
        currHashedPass = bcrypt.hashpw(currPass, bcrypt.gensalt(12))
        stdId = passFile.readline()[0:-1]
        stdPass = passFile.readline().encode("utf8")

        if(currId == stdId and bcrypt.checkpw(currPass, stdPass)):
            self.status.configure(text="Correct Password")
        else:
            self.status.configure(text="Wrong Password")

        passFile.close()

    def cloudAuth(self):
        print("cloudAuth")
        # dbname = get_database()
        # collection_name = dbname["users"]

        # item_details = collection_name.find()
        # for item in item_details:
        # # This does not give a very readable output
        #     print(item)

    def back(self):
        self.main_window.destroy()
        self = Auth(self.parent_window)

    def destroy(self):
        self.main_window.destroy()

class Auth:
    def __init__(self, window):
        super().__init__()
        self.parent_window = window
        self.main_window = Frame(window)
        self.head = Label (self.main_window, text="Login")
        self.idLabel = Label(self.main_window, text="")
        self.passLabel = Label(self.main_window, text="Enter Password")
        self.password = Entry(self.main_window)
        self.submit = Button(self.main_window, text="Submit", command=self.checkLocalTextPassword)
        self.status = Label(self.main_window, text="")
        self.newLoginBtn = Button(self.main_window, text="New Login", command=self.newLogin)

        self.main_window.pack()
        self.head.pack()
        self.idLabel.pack()
        self.passLabel.pack()
        self.password.pack()
        self.submit.pack()
        self.status.pack()
        self.newLoginBtn.pack()

        self.checkAndUpdateUserId()

    def checkLocalTextPassword(self):
        passFile = open("localPassword/password.txt", "r")
        currId = self.idLabel.cget("text")
        currPass = self.password.get().encode("utf8")
        stdId = passFile.readline()[0:-1]
        stdPass = passFile.readline().encode("utf8")

        passFile.close()

        if(currId == stdId and bcrypt.checkpw(currPass, stdPass)):
            self.status.configure(text="Correct Password")
            self.login()
            return True

        else:
            self.status.configure(text="Wrong Password")
            return False

    def checkAndUpdateUserId(self):
        passFile = open("localPassword/password.txt", "r")
        stdId = passFile.readline()[0:-1]
        passFile.close()
        if(stdId != ""):
            self.idLabel.configure(text=stdId)
            return True
        else:
            return False

    def newLogin(self):
        self.destroy()
        self = NewLogin(self.parent_window)

    def login(self):
        self.parent_window.destroy()
        home = Home(self.parent_window)
        home.mainloop()

    def destroy(self):
        self.main_window.destroy()


# window = Tk()

# auth = Auth(window)

# if(auth.checkAndUpdateUserId() == False):
#     auth.destroy()
#     auth = NewLogin(window)
# # auth.destroy()
# # auth = NewLogin(window)

# window.mainloop() 