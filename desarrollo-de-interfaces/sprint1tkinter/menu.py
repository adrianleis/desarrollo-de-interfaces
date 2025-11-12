import tkinter as tk
from tkinter import messagebox

def abrir():
    etiqueta.config(text="Has seleccionado Abrir")

def salir():
    root.quit()

def acerca_de():
    messagebox.showinfo("Acerca de", "Esta es una aplicación de ejemplo con Menú")

root = tk.Tk()
root.title("Ejercicio Menú")
root.geometry("300x150")

menubar = tk.Menu(root)

archivo_menu = tk.Menu(menubar, tearoff=0)
archivo_menu.add_command(label="Abrir", command=abrir)
archivo_menu.add_command(label="Salir", command=salir)
menubar.add_cascade(label="Archivo", menu=archivo_menu)

ayuda_menu = tk.Menu(menubar, tearoff=0)
ayuda_menu.add_command(label="Acerca de", command=acerca_de)
menubar.add_cascade(label="Ayuda", menu=ayuda_menu)

root.config(menu=menubar)

etiqueta = tk.Label(root, text="", font=("Arial", 12))
etiqueta.pack(pady=50)

root.mainloop()
