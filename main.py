# This is a program that will take exported contacts from iPhone and merge them into one vcf file for easy importing
import tkinter as tk
from tkinter import filedialog, Text
import tkinter.messagebox
import os
import platform

# Window
window = tk.Tk()

# This will open a file manager as soon as you open the program to select the destination folder
filenames= ''

def filenames_function():
    global filenames
    filenames = filedialog.askdirectory(initialdir="/", title="Select the folder the VCF files are in")

# Functions
def change_dir():
    print(type(filenames))

def merge():
    os.chdir(filenames)
    if platform.system() == "Windows":
        os.system('cmd /c "copy *.vcf 1-merged-contacts.vcf"')
    elif platform.system() == "Darwin":
        os.system('cat *.vcf > 1-merged-contacts.vcf')
    elif platform.system() == "Linux":
        os.system('cat *.vcf > 1-merged-contacts.vcf')
    else:
        print("This operating system is not supported.")

# GUI
window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())  # center the window
tkinter.messagebox.showinfo("READ", 'This program will merge all of the vcf files you have into one that will be named "1-merged-contacts.vcf"... Once merged the file will be in the same folder that you choose.')
canvas = tk.Canvas(window, height=300, width=700, bg="#391282")
canvas.pack()
greeting = tk.Label(text="Hello welcome to fzr76' VCF Merger")
greeting.pack()
frame = tk.Frame(window, bg="#391282")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
openVCF = tk.Button(frame, text="Choose Folder", padx=10, pady=5, fg="black", bg="#9b42f5", command=filenames_function)
openVCF.pack()
save_new_VCF = tk.Button(frame, text="Merge VCF Files", padx=10, pady=5, fg="black", bg="#9b42f5", command=merge)
save_new_VCF.pack()

window.mainloop()