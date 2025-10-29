import tkinter as tk

def saludar():
    nombre = entrada.get()
    etiqueta.config(text=f"¡Hola, {nombre}!")

root = tk.Tk()
root.title("Saludo Personalizado")
root.geometry("300x150")

entrada = tk.Entry(root, font=("Arial", 12))
entrada.pack(pady=10)

boton = tk.Button(root, text="Saludar", command=saludar)
boton.pack(pady=5)

etiqueta = tk.Label(root, text="", font=("Arial", 12))
etiqueta.pack(pady=10)

root.mainloop()
