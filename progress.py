from tkinter import *
import customtkinter
import time

def calltime(time1):
    
    currTime = time.time()
    if((time.time()) - time1 < 3):
        return False
    return True

class Progress(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.configure(background='#050514')

        self.geometry(f"{1280}x{800}")
        self.title("Medical Slide Scanner")

        text_var = StringVar(value="Please close the lid")

        warnLabel = customtkinter.CTkLabel(master=self,
                                    textvariable=text_var,
                                    width=120,
                                    height=25,
                                    fg_color=("white", "gray75"),
                                    corner_radius=8)
        warnLabel.place(relx=0.5, rely=0.5, anchor=CENTER)

        # def calltime():
        #     time1 = (time.time())
        #     print(type(time.time()))
        #     while((time.time()) - time1 < 3):
        #         print((time.time()))
        #         continue
        time1 = (time.time())
        while(True):
            if(calltime(time1) == False):
                warnLabel.destroy()


        text2_var = StringVar(value="OK!")

        okLabel = customtkinter.CTkLabel(master=self,
                                    textvariable=text2_var,
                                    width=120,
                                    height=25,
                                    fg_color=("white", "gray75"),
                                    corner_radius=8)
        okLabel.place(relx=0.5, rely=0.5, anchor=CENTER)