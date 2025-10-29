import tkinter as tk

def mostrar_fruta():
    seleccion = lista.curselection()
    if seleccion:
        fruta = lista.get(seleccion)
        etiqueta.config(text=f"Fruta seleccionada: {fruta}")

root = tk.Tk()
root.title("Lista de Frutas")
root.geometry("300x200")

lista = tk.Listbox(root)
lista.insert(1, "Manzana")
lista.insert(2, "Banana")
lista.insert(3, "Naranja")
lista.pack(pady=10)

boton = tk.Button(root, text="Mostrar fruta", command=mostrar_fruta)
boton.pack(pady=5)

etiqueta = tk.Label(root, text="", font=("Arial", 12))
etiqueta.pack(pady=10)

root.mainloop()
