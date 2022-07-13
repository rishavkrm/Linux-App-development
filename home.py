from tkinter import *
import customtkinter



class Home(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        # root_tk = customtkinter.CTk()
        self.configure(background='#1B2430')

        self.geometry(f"{1180}x{820}")
        self.title("Medical Slide Scanner")
        scanner_image = PhotoImage(file='scannerLogo.png')
        scanner_image = scanner_image.subsample(25)

        text_var = customtkinter.StringVar(value="Medical Slide Scanner")

        # LABEL
        label = customtkinter.CTkLabel(master=self,
                                       textvariable=text_var,
                                       width=120,
                                       height=25,
                                       text_color='#D6D5A8',
                                       text_font='Courier 50',
                                       # fg_color=("white", "gray75"),
                                       justify="left",
                                       corner_radius=8)
        label.place(relx=0.5, rely=0.01, anchor="n")

        # SCAN BUTTON
        button1 = customtkinter.CTkButton(self, fg_color="#51557E",
                                          text="Scan    ",
                                          text_font=('Courier', '25'),
                                          width=360,
                                          height=150,
                                          image=scanner_image,
                                          compound='right',
                                          command=self.collapseHomeAndScan
                                          )  # single color name
        # button1.pack(padx=0, pady=0)
        button2 = customtkinter.CTkButton(self, fg_color="#51557E",
                                          width=360,
                                          height=150,
                                          )  # single hex string
        button3 = customtkinter.CTkButton(self, fg_color="#51557E",
                                          width=360,
                                          height=350,
                                          text="Scan    ",
                                          text_font=('Courier', '25'),
                                          image=scanner_image,
                                          compound='right',
                                          )  # tuple color

        # PLACING BUTTONS
        button1.place(relx=0.35, rely=0.3, anchor="n")
        button2.place(relx=0.35, rely=0.55, anchor="n")
        button3.place(relx=0.70, rely=0.3, anchor="n")

    def collapseHomeAndScan(self):
        from scan import Scan
        self.destroy()
        scan = Scan()
        scan.mainloop()
