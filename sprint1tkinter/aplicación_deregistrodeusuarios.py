import tkinter as tk
from tkinter import messagebox

def añadir_usuario():
    nombre = entry_nombre.get().strip()
    edad = scale_edad.get()
    genero = genero_var.get()
    if nombre and genero:
        usuario = f"{nombre} - {edad} años - {genero}"
        lista_usuarios.insert(tk.END, usuario)
        entry_nombre.delete(0, tk.END)
    else:
        messagebox.showwarning("Datos incompletos", "Introduce nombre y género.")

def eliminar_usuario():
    seleccion = lista_usuarios.curselection()
    if seleccion:
        lista_usuarios.delete(seleccion)
    else:
        messagebox.showwarning("Selecciona usuario", "Debes seleccionar un usuario para eliminar.")

def guardar_lista():
    messagebox.showinfo("Guardar Lista", "Función de guardar lista no implementada.")

def cargar_lista():
    messagebox.showinfo("Cargar Lista", "Función de cargar lista no implementada.")

root = tk.Tk()
root.title("Registro de Usuarios")
root.geometry("500x400")

# Frame superior
frame_superior = tk.Frame(root)
frame_superior.pack(pady=10)

tk.Label(frame_superior, text="Nombre:").grid(row=0, column=0, padx=5)
entry_nombre = tk.Entry(frame_superior)
entry_nombre.grid(row=0, column=1, padx=5)

tk.Label(frame_superior, text="Edad:").grid(row=1, column=0, padx=5, pady=5)
scale_edad = tk.Scale(frame_superior, from_=0, to=100, orient="horizontal")
scale_edad.grid(row=1, column=1, padx=5, pady=5)

genero_var = tk.StringVar(value="")
tk.Label(frame_superior, text="Género:").grid(row=2, column=0, padx=5, pady=5)
tk.Radiobutton(frame_superior, text="Masculino", variable=genero_var, value="Masculino").grid(row=2, column=1, sticky="w")
tk.Radiobutton(frame_superior, text="Femenino", variable=genero_var, value="Femenino").grid(row=3, column=1, sticky="w")
tk.Radiobutton(frame_superior, text="Otro", variable=genero_var, value="Otro").grid(row=4, column=1, sticky="w")

# Frame inferior
frame_inferior = tk.Frame(root)
frame_inferior.pack(pady=10, fill="both", expand=True)

scroll = tk.Scrollbar(frame_inferior)
scroll.pack(side="right", fill="y")

lista_usuarios = tk.Listbox(frame_inferior, yscrollcommand=scroll.set)
lista_usuarios.pack(side="left", fill="both", expand=True)
scroll.config(command=lista_usuarios.yview)

# Botones
botones_frame = tk.Frame(root)
botones_frame.pack(pady=10)

tk.Button(botones_frame, text="Añadir", width=10, command=añadir_usuario).grid(row=0, column=0, padx=5)
tk.Button(botones_frame, text="Eliminar", width=10, command=eliminar_usuario).grid(row=0, column=1, padx=5)
tk.Button(botones_frame, text="Salir", width=10, command=root.quit).grid(row=0, column=2, padx=5)

# Menú
menubar = tk.Menu(root)
archivo_menu = tk.Menu(menubar, tearoff=0)
archivo_menu.add_command(label="Guardar Lista", command=guardar_lista)
archivo_menu.add_command(label="Cargar Lista", command=cargar_lista)
menubar.add_cascade(label="Archivo", menu=archivo_menu)
root.config(menu=menubar)

root.mainloop()
