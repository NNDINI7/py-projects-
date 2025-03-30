#digital clock 
import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("DIGITAL CLOCK")

def time():
    string = strftime('%H:%M:%S %P \n %D')
    label.config(text = string)
    label.after(1000,time) #time gets updated every time

label = tk.Label(root,font=('calibri', 50, 'bold'),background ='yellow',foreground = 'black')
#arrange elements in window
label.pack(anchor='center')

time()

root.mainloop()

