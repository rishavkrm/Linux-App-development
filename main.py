from tkinter import *
from authUI import NewLogin, Auth

window = Tk()

auth = Auth(window)

if(auth.checkAndUpdateUserId() == False):
    auth.destroy()
    auth = NewLogin(window)
# auth.destroy()
# auth = NewLogin(window)
# print(auth.log)
# if(auth.log == True):
#     print("c")
#     auth.destroy()
#     window = Home()


window.mainloop()





# home = Home()
# home.resizable(False ,False)
# home.mainloop()
# root_tk.mainloop()
