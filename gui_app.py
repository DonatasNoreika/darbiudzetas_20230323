
from tkinter import Tk, Label, Entry, Button, END

from biudzetas import Biudzetas

langas = Tk()

biudzetas = Biudzetas()

def ivesti():
    suma = float(suma_entry.get())
    if suma > 0:
        biudzetas.prideti_pajamu_irasa(abs(suma), "", "")
    else:
        biudzetas.prideti_islaidu_irasa(abs(suma), "", "")
    suma_entry.delete(0, END)

langas.geometry("250x200")
suma_label = Label(langas, text="Įrašykite sumą")
suma_entry = Entry(langas)
suma_button = Button(langas, text="Įvesti", command=ivesti)


suma_label.grid(row=0, column=0)
suma_entry.grid(row=0, column=1)
suma_button.grid(row=0, column=2)
langas.mainloop()