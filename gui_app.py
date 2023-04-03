
from tkinter import Tk, Label, Entry, Button, END, Listbox

from biudzetas import Biudzetas

langas = Tk()

biudzetas = Biudzetas()

def atnaujinti_listbox():
    boksas_listbox.delete(0, END)
    boksas_listbox.insert(END, *biudzetas.zurnalas)

def ivesti():
    suma = float(suma_entry.get())
    if suma > 0:
        biudzetas.prideti_pajamu_irasa(abs(suma), "", "")
    else:
        biudzetas.prideti_islaidu_irasa(abs(suma), "", "")
    suma_entry.delete(0, END)
    atnaujinti_listbox()

langas.geometry("250x200")
suma_label = Label(langas, text="Įrašykite sumą")
suma_entry = Entry(langas)
suma_button = Button(langas, text="Įvesti", command=ivesti)
boksas_listbox = Listbox(langas)
boksas_listbox.insert(END, *biudzetas.zurnalas)

suma_label.grid(row=0, column=0)
suma_entry.grid(row=0, column=1)
suma_button.grid(row=0, column=2)
boksas_listbox.grid(row=1, columnspan=3)
langas.mainloop()