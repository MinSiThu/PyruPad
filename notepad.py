from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import messagebox
import os

class Notepad():

    __name = "TK Notepad"
    __window = Tk()
    __height = 750
    __width = 750

    __textArea = scrolledtext.ScrolledText(__window)
    __menuBar = Menu(__window,tearoff=0)

    __fileMenu = Menu(__menuBar,tearoff=0)
    __editMenu = Menu(__menuBar,tearoff=0)
    __aboutMenu = Menu(__menuBar,tearoff=0)
    __file = None 

    def __init__(self):
        self.__window.title(self.__name)
        # resizeable frame
        self.__window.grid_rowconfigure(0, weight=1)
        self.__window.grid_columnconfigure(0, weight=1)

        self.__textArea.grid(sticky = N + E + S + W)

        # File Menu
        self.__fileMenu.add_command(label="New",command=self.__newFile)
        self.__fileMenu.add_command(label="Open",command=self.__openFile)
        self.__fileMenu.add_command(label="Save",command=self.__saveFile)
        self.__fileMenu.add_command(label="Exit",command=self.__quitApp)

        self.__menuBar.add_cascade(label="File",menu=self.__fileMenu)

        # Edit Menu
        self.__editMenu.add_command(label="Copy",command=self.__copy)
        self.__editMenu.add_command(label="Cut",command=self.__cut)
        self.__editMenu.add_command(label="Paste",command=self.__paste)
        
        self.__menuBar.add_cascade(label="Edit",menu=self.__editMenu)

        # About Menu
        self.__aboutMenu.add_command(label="About Us",command=self.__openAboutUs)
        self.__menuBar.add_cascade(label="About",menu=self.__aboutMenu)

        # Add menu bar
        self.__window.config(menu=self.__menuBar)

    def run(self):
        self.__window.mainloop()

    # Functions in Menu
    def __openAboutUs(self):
        messagebox.showinfo("About Us","This note is for Free & Open Source")

    def __quitApp(self):
        self.__window.destroy() #quit app

    def __openFile(self):
        self.__file = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if self.__file == "":
            self.__file = None
        else:
            self.__window.title(os.path.basename(self.__file))
            file = open(self.__file,"r")
            self.__textArea.delete(1.0,END)
            self.__textArea.insert(1.0, file.read())
            file.close()

    def __newFile(self):
        self.__window.title(self.__name)
        self.__file = None
        self.__textArea.delete(1.0,END)

    def __saveFile(self):
        self.__file = filedialog.asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])
        if self.__file == "":
            self.__file = None
        else:
            file = open(self.__file,"w")
            file.write(self.__textArea.get(1.0,END))
            file.close()
            self.__window.title(os.path.basename(self.__file))

    def __cut(self):
        self.__textArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__textArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__textArea.event_generate("<<Paste>>")

notepad = Notepad()
notepad.run()