from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text="type", src="English", dest="Hindi"):
    trans = Translator()
    try:
        trans1 = trans.translate(text, src=src, dest=dest)
        return trans1.text
    except Exception as e:
        return "Error: " + str(e)

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    msg = Sor_txt.get(1.0, END)  # Get data from the source text box
    textget = change(text=msg, src=s, dest=d)
    dest_txt.delete(1.0, END)  # Clear previous text
    dest_txt.insert(END, textget)  # Insert the translated text

# Basic GUI setup
root = Tk()
root.title("Translator")
root.geometry("500x600")
root.config(bg='yellow')

# Title Label
lab_txt = Label(root, text="Translator", font=("Times New Roman", 30, "bold"), bg="red")
lab_txt.pack(pady=20)

# Source Text Label
lab_src = Label(root, text="Source Text", font=("Times New Roman", 20, "bold"), bg="yellow")
lab_src.pack()

# Source Text Box
Sor_txt = Text(root, font=("Times New Roman", 16), wrap=WORD, height=5, width=50)
Sor_txt.pack(pady=10)

# Frame for Language Selection
frame = Frame(root, bg="yellow")
frame.pack(pady=10)

# Source Language Combo Box
list_text = list(LANGUAGES.values())
comb_sor = ttk.Combobox(frame, values=list_text, state="readonly", font=("Arial", 12))
comb_sor.grid(row=0, column=0, padx=10, pady=5)
comb_sor.set("english")

# Translate Button
button_change = Button(frame, text="Translate", font=("Arial", 12, "bold"), bg="green", fg="white", command=data)
button_change.grid(row=0, column=1, padx=10)

# Destination Language Combo Box
comb_dest = ttk.Combobox(frame, values=list_text, state="readonly", font=("Arial", 12))
comb_dest.grid(row=0, column=2, padx=10, pady=5)
comb_dest.set("hindi")

# Destination Text Label
lab_dest = Label(root, text="Translated Text", font=("Times New Roman", 20, "bold"), bg="yellow")
lab_dest.pack()

# Destination Text Box
dest_txt = Text(root, font=("Times New Roman", 16), wrap=WORD, height=5, width=50)
dest_txt.pack(pady=10)

# Run the GUI
root.mainloop()
