# Librerias
from tkinter import Tk, Label, Entry, Button
from pytube import YouTube

# Declaración funciones
def buscar(link):
    print()


# Declaración ventana
ventana = Tk()
ventana.title("Si")
ventana.config(bg="Black", width=800, height=400)

# Declaración interfaz
titulo = Label(ventana, text="Introduce el enlace del video de YouTube", fg="White", bg="Black", font="Calibri 14")
titulo.place(x=10, y=10)
entradaLink = Entry(ventana, font="Calibri 14")
entradaLink.place(x=10, y=40)
botonBuscar = Button(ventana, text="Buscar", fg="White", bg="Grey", font="Calibri 14", command=buscar(entradaLink.get()))
botonBuscar.place(x=300, y=40)


# Bucle ventana
ventana.mainloop()