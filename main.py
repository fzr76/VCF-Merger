# This is a program that will take exported contacts from iPhone and merge them into one vcf file for easy importing
import tkinter as tk
from tkinter import filedialog, Text
import os

# Window
window = tk.Tk()

# List of VCF Files
vcf_dir = []

# Functions
def selectVCF():
    filenames= filedialog.askdirectory(initialdir="/", title="Select folder with VCF Files")
    vcf_dir.append(filenames)
    print(filenames)
    return filenames
def merge():
    os.system('cmd /c "cd selectVCF"')
    os.system('cmd /c "copy *.vcf all.vcf"')
# GUI
canvas = tk.Canvas(window, height=700, width=700, bg="#391282")
canvas.pack()
greeting = tk.Label(text="Hello welcome to fzr76' VCF Merger")
greeting.pack()
frame = tk.Frame(window, bg="#391282")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
openVCF = tk.Button(frame, text="Open VCF Files", padx=10, pady=5, fg="black", bg="#9b42f5", command=selectVCF )
openVCF.pack()
save_new_VCF = tk.Button(frame, text="Save VCF File", padx=10, pady=5, fg="black", bg="#9b42f5", command=merge )
save_new_VCF.pack()

window.mainloop()

multiple_vcf = 0