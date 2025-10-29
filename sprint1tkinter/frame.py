import tkinter as tk

def mostrar_texto():
    etiqueta_resultado.config(text=entry.get())

def borrar_texto():
    entry.delete(0, tk.END)
    etiqueta_resultado.config(text="")

root = tk.Tk()
root.title("Ejercicio Frame")
root.geometry("400x200")

frame_superior = tk.Frame(root)
frame_superior.pack(pady=10)

tk.Label(frame_superior, text="Etiqueta 1").grid(row=0, column=0, padx=5, pady=5)
tk.Label(frame_superior, text="Etiqueta 2").grid(row=0, column=1, padx=5, pady=5)
entry = tk.Entry(frame_superior)
entry.grid(row=1, column=0, columnspan=2, pady=5)

frame_inferior = tk.Frame(root)
frame_inferior.pack(pady=10)

boton_mostrar = tk.Button(frame_inferior, text="Mostrar", command=mostrar_texto)
boton_mostrar.grid(row=0, column=0, padx=5)
boton_borrar = tk.Button(frame_inferior, text="Borrar", command=borrar_texto)
boton_borrar.grid(row=0, column=1, padx=5)

etiqueta_resultado = tk.Label(root, text="", font=("Arial", 12))
etiqueta_resultado.pack(pady=10)

root.mainloop()
