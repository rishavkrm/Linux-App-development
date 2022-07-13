from tkinter import *
import customtkinter
# from home import Home
from sample_data import sample


class Scan(customtkinter.CTk):

    # constructor
    def __init__(self):
        optionMenuIsClicked = False
        super().__init__()
        # root_tk = customtkinter.CTk()
        self.configure(background='#1B2430')

        self.geometry(f"{1180}x{820}")
        self.title("Medical Slide Scanner")

        # Top LABEL
        text_var = customtkinter.StringVar(value="Please select scan type")
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

        # Select from here label
        labelVar = customtkinter.StringVar(value="Select from here")
        scanTypeLabel = customtkinter.CTkLabel(master=self,
                                               textvariable=labelVar,
                                               width=400,
                                               height=25,
                                               text_color='#D6D5A8',
                                               text_font='Courier 25',
                                               # fg_color=("white", "gray75"),
                                               justify="left",
                                               corner_radius=8)
        scanTypeLabel.place(relx=0.285, rely=0.2, anchor="n")

        optionmenu_var = customtkinter.StringVar(value="------select------")  # set initial value

        # Dropdown menu

        # callback

        def optionmenu_callback(choice):
            id = sample[choice]
            # global id_label
            id_label.destroy()

            # Label
            label = customtkinter.CTkLabel(master=self,
                                           text=id,
                                           width=0,
                                           height=25,
                                           corner_radius=8)
            label.place(relx=0.6, rely=0.5, anchor=N)

        combobox = customtkinter.CTkComboBox(master=self,
                                             values=list(sample.keys()),
                                             command=optionmenu_callback,
                                             width=250,
                                             variable=optionmenu_var)
        combobox.place(relx=0.185, rely=0.26)

        id_label = customtkinter.CTkLabel(master=self, width=0, text="XXX")
        id_label.place(relx=0.6, rely=0.5, anchor=N)
        # Input Box
        entry = customtkinter.CTkEntry(master=self,
                                       placeholder_text="Enter sample id",
                                       width=120,
                                       height=25,
                                       border_width=2,
                                       corner_radius=10)
        entry.place(relx=0.675, rely=0.515, anchor=CENTER)

        # Scan button
        def scan_button_event():
            print("button pressed")

        scan_button = customtkinter.CTkButton(master=self,
                                              width=120,
                                              height=32,
                                              border_width=0,
                                              corner_radius=8,
                                              text="Scan",
                                              command=scan_button_event)
        scan_button.place(relx=0.9, rely=0.9, anchor=CENTER)



        scan_button = customtkinter.CTkButton(master=self,
                                              width=120,
                                              height=32,
                                              border_width=0,
                                              corner_radius=8,
                                              text="Back",
                                              command=self.collapseScanAndEnterHome)
        scan_button.place(relx=0.1, rely=0.9, anchor=CENTER)

    # Back button
    def collapseScanAndEnterHome(self):
        from home import Home
        self.destroy()
        home = Home()
        home.mainloop()