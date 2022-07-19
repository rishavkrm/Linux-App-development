from tkinter import *
import customtkinter
from customtkinter import *
from sample_data import sample
import tkinter as tk


class Scan(customtkinter.CTk):

    # constructor
    def __init__(self):
        optionMenuIsClicked = False
        super().__init__()
        # root_tk = customtkinter.CTk()
        self.configure(background='#050514')

        self.geometry(f"{1280}x{800}")
        self.title("Medical Slide Scanner")
        

        # Top LABEL
        text_var = customtkinter.StringVar(value="Please select scan type")
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

        # Select from here label
        labelVar = customtkinter.StringVar(value="Select from here")
        scanTypeLabel = customtkinter.CTkLabel(master=self,
                                               textvariable=labelVar,
                                               width=400,
                                               height=25,
                                               text_color='#8CE6BB',
                                               text_font='"Roboto Slab" 25',
                                               # fg_color=("white", "gray75"),
                                               justify="left",
                                               corner_radius=8)
        scanTypeLabel.place(relx=0.285, rely=0.2, anchor="n")

        optionmenu_var = customtkinter.StringVar(value="------select------")  # set initial value

        self.mainframe = Frame(self)
        self.mainframe.place(x=315, y = 300)

        self.file_choice = tk.StringVar()
        self.contents_list = list()
        self.folder_contents_frame = ScrollFrame(self.mainframe)
        self.folder_contents_frame.pack(side = BOTTOM)

        scan_button = customtkinter.CTkButton(master=self,
                                              text_font='"Roboto Slab" 18',
                                              width=120,
                                              height=32,
                                              border_width=0,
                                              corner_radius=8,
                                              text="Scan",
                                              fg_color="#8CE6BB",
                                              text_color="#050514",
                                              command=self.scan_button_event)
        scan_button.place(relx=0.9, rely=0.9, anchor=CENTER)



        back_button = customtkinter.CTkButton(master=self,
                                              text_font='"Roboto Slab" 18',
                                              width=120,
                                              height=32,
                                              border_width=0,
                                              corner_radius=8,
                                              text="Back",
                                              fg_color="#8CE6BB",
                                              text_color="#050514",
                                              command=self.collapseScanAndEnterHome)
        back_button.place(relx=0.1, rely=0.9, anchor=CENTER)

        def btn_change():
            print(self.file_choice.get())
            labelOption.configure(text = self.file_choice.get())

        for (text, value) in sample.items():
                CTkRadioButton(self.folder_contents_frame.viewPort, text = text, variable = self.file_choice, value = value,bg_color = "#050517", command=btn_change, border_color='#8CE6BB').grid(padx=2, pady=5,column = 0, columnspan = 2, sticky = tk.W)

        labelOption = CTkLabel(self,text="XXX",width=10, text_color='#8CE6BB', text_font='"Roboto Slab" 9')
        labelOption.place(relx=0.7, rely=0.7)
    
        entry = customtkinter.CTkEntry(master=self,
                                       placeholder_text="Enter sample id",
                                       width=120,
                                       height=25,
                                       border_width=2,
                                       corner_radius=10)
        entry.place(relx=0.775, rely=0.717, anchor=CENTER)
    # Back button
    def collapseScanAndEnterHome(self):
        from home import Home
        self.destroy()
        home = Home()
        home.mainloop()
    
    # Scan Button
    def scan_button_event(self):
        from progress import Progress
        self.destroy()
        progress = Progress()
        progress.mainloop()
    

class ScrollFrame(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent) # create a frame (self)

        self.canvas = tk.Canvas(self, borderwidth=0, background="#050517")      # Canvas to scroll
        self.viewPort = tk.Frame(self.canvas, borderwidth=0, background="#050517")     # This frame will hold the child widgets
        self.vsb = CTkScrollbar(self, orientation="vertical", command=self.canvas.yview) 
        self.canvas.configure(yscrollcommand=self.vsb.set)      # Attach scrollbar action to scroll of canvas

        self.vsb.pack(side="right", fill="y")       # Pack scrollbar to right - change as needed
        self.canvas.pack(side="left", fill="both", expand=True)     # Pack canvas to left and expand to fill - change as needed
        self.canvas_window = self.canvas.create_window(
            (0,0), 
            window=self.viewPort, 
            anchor="nw",            
            tags="self.viewPort",
            )       # Add view port frame to canvas

        self.viewPort.bind("<Configure>", self.onFrameConfigure)
        self.canvas.bind("<Configure>", self.onCanvasConfigure)
        self.first = True
        self.onFrameConfigure(None) # Initial stretch on render

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def onCanvasConfigure(self, event):
        '''Reset the canvas window to encompass inner frame when required'''
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_window, width = canvas_width)

    def on_mousewheel(self, event):
        '''Allows the mousewheel to control the scrollbar'''
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def bnd_mousewheel(self):
        '''Binds the mousewheel to the scrollbar'''
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)

    def unbnd_mousewheel(self):
        '''Unbinds the mousewheel from the scrollbar'''
        self.canvas.unbind_all("<MouseWheel>")

    def delete_all(self):
        '''Removes all widgets from the viewPort, only works if grid was used'''
        children = self.viewPort.winfo_children()
        for child in children:
            child.grid_remove()