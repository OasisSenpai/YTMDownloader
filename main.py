# Librerias
from tkinter import Tk, Label, Entry, Button, filedialog, LabelFrame, Radiobutton, StringVar
from pytube import YouTube
import re

# Declaración funciones
def directorio(lugar):
    entradaDirectorio.delete(0, "end")
    entradaDirectorio.insert(0, lugar)


def descargar(opcion, link):
    if entradaDirectorio.get()=="":
        directorio(filedialog.askdirectory())
    j = re.split("\s", opcion)
    itag = j[1].split("=")[1].replace('"','')
    print(itag)
    YouTube(link).streams.filter(only_audio=True).get_by_itag(itag).download(entradaDirectorio.get())


def buscar(link):
    opciones_var = StringVar()
    grid_row = 0
    for i in YouTube(link).streams.filter(only_audio=True):
        # create a radio button
        radio = Radiobutton(etiquetaOpciones, text=i, value=i, variable=opciones_var, anchor="w")
        #radio.place(x=0, y=grid_row)
        radio.grid(column=0, row=grid_row, ipady=5)
        grid_row += 1
    botonDescargar = Button(etiquetaOpciones, text="Descargar", fg="White", bg="Grey", font="Calibri 13", command=lambda:descargar(opciones_var.get(), link))
    botonDescargar.grid(column=0, row=grid_row, ipady=5)


# Declaración ventana
ventana = Tk()
ventana.title("Download music from YouTube")
ventana.config(width=865, height=400)

# Declaración interfaz
titulo = Label(ventana, text="Introduce el enlace del video de YouTube", font="Calibri 14", width=40)
titulo.place(x=10, y=10)
etiquetaDirectorio = Label(ventana, text="Introduce el directorio donde guardarlo", font="Calibri 14", width=40)
etiquetaDirectorio.place(x=450, y=10)

entradaLink = Entry(ventana, font="Calibri 14", width=40)
entradaLink.place(x=10, y=40)
entradaDirectorio = Entry(ventana, font="Calibri 14", width=40)
entradaDirectorio.place(x=450, y=40)

botonBuscar = Button(ventana, text="Buscar", fg="White", bg="Grey", font="Calibri 13", width=44, command=lambda:buscar(entradaLink.get()))
botonBuscar.place(x=10, y=70)
botonDirectorio = Button(ventana, text="Explorar", fg="White", bg="Grey", font="Calibri 13", width=44, command=lambda:directorio(filedialog.askdirectory()))
botonDirectorio.place(x=450, y=70)

etiquetaOpciones = LabelFrame(ventana, text="Opciones a elegir:", font="Calibri 14", width=845)
etiquetaOpciones.place(x=10, y=120)



# Bucle ventana
ventana.mainloop()