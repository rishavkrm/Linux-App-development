from tkinter import *
import customtkinter
from PIL import Image, ImageTk
from yaml import AnchorToken
import os
print(os.getcwd())


class Home(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        # root_tk = customtkinter.CTk()
        self.configure(background="#050514")

        self.geometry(f"{1280}x{800}")
        self.title("Medical Slide Scanner")
        # scanner_image = PhotoImage(file='scannerLogo.png')
        # scanner_image = scanner_image.subsample(25)

        text_var = customtkinter.StringVar(value="MEDICAL SLIDE SCANNER")

        # LABEL
        label = customtkinter.CTkLabel(master=self,
                                       textvariable=text_var,
                                       width=120,
                                       height=25,
                                       text_color='#8CE6BB',
                                       text_font='"Roboto Slab" 45',
                                       # fg_color=("white", "gray75"),
                                       justify="left",
                                       corner_radius=8)
        label.place(relx=0.5, rely=0.01, anchor="n")

        # # SCAN BUTTON
        # button1 = customtkinter.CTkButton(self, fg_color="#51557E",
        #                                   text="Scan    ",
        #                                   text_font=('Monteserrat', '25'),
        #                                   width=360,
        #                                   height=150,
        #                                   image=scanner_image,
        #                                   compound='right',
        #                                   command=self.collapseHomeAndScan
        #                                   )  # single color name
        # # button1.pack(padx=0, pady=0)
        # button2 = customtkinter.CTkButton(self, fg_color="#51557E",
        #                                   width=360,
        #                                   height=150,
        #                                   text="Manual Scan",
        #                                   text_font=('Monteserrat', '25'),
        #                                   image=scanner_image,
        #                                   compound='right'
        #                                   )  # single hex string
        # button3 = customtkinter.CTkButton(self, fg_color="#51557E",
        #                                   width=360,
        #                                   height=350,
        #                                   text="Repository",
        #                                   text_font=('Monteserrat', '25'),
        #                                   image=scanner_image,
        #                                   compound='right'
        #                                   )  # tuple color

        # Scan Button

        scan_image = Image.open(f"{os.getcwd()}/image/img0.png")
        resized_image= scan_image.resize((350,350))
        scan_image = ImageTk.PhotoImage(resized_image)
        button1 = customtkinter.CTkButton(self, 
                                            image=scan_image,
                                            command=self.collapseHomeAndScan,
                                            text="",
                                            border_width=0,
                                            fg_color="#050514",
                                            hover_color="#050514")
                                        
        find_image = Image.open(f"{os.getcwd()}/image/img1.png")
        resized_image= find_image.resize((400,150))
        find_image = ImageTk.PhotoImage(resized_image)
        button2 = customtkinter.CTkButton(self, 
                                            image=find_image,
                                            text="",
                                            border_width=0,
                                            fg_color="#050514",
                                            hover_color="#050514")

        search_image = Image.open(f"{os.getcwd()}//image/img2.png")
        resized_image= search_image.resize((400,200))
        search_image = ImageTk.PhotoImage(resized_image)
        button3 = customtkinter.CTkButton(self, 
                                            image=search_image,
                                            text="",
                                            border_width=0,
                                            fg_color="#050514",
                                            hover_color="#050514")

        demo1_image = Image.open(f"{os.getcwd()}//image/img3.png")
        resized_image= demo1_image.resize((350,150))
        demo1_image = ImageTk.PhotoImage(resized_image)
        button4 = customtkinter.CTkButton(self, 
                                            image=demo1_image,
                                            text="",
                                            border_width=0,
                                            fg_color="#050514",
                                            hover_color="#050514")

        demo2_image = Image.open(f"{os.getcwd()}/image/img4.png")
        resized_image= demo2_image.resize((400,125))
        demo2_image = ImageTk.PhotoImage(resized_image)
        button5 = customtkinter.CTkButton(self, 
                                            image=demo2_image,
                                            text="",
                                            border_width=0,
                                            fg_color="#050514",
                                            hover_color="#050514")

        # PLACING BUTTONS
        button1.place(x=260, y=100)
        button2.place(x=650, y=100)
        button3.place(x=650, y=280)
        button4.place(x=260, y=485)
        button5.place(x=650, y=510)

    def collapseHomeAndScan(self):
        from scan import Scan
        self.destroy()
        scan = Scan()
        scan.mainloop()
