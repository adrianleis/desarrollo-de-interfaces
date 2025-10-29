import tkinter as tk

def actualizar(valor):
    etiqueta.config(text=f"Valor seleccionado: {valor}")

root = tk.Tk()
root.title("Ejercicio Scale")
root.geometry("300x150")

scale = tk.Scale(root, from_=0, to=100, orient="horizontal", command=actualizar)
scale.pack(pady=20)

etiqueta = tk.Label(root, text="Valor seleccionado: 0", font=("Arial", 12))
etiqueta.pack()

root.mainloop()
