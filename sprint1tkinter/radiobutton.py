import tkinter as tk

def cambiar_color():
    root.config(bg=color_var.get())

root = tk.Tk()
root.title("Color Favorito")
root.geometry("300x150")

color_var = tk.StringVar(value="white")

rb_rojo = tk.Radiobutton(root, text="Rojo", variable=color_var, value="red", command=cambiar_color)
rb_rojo.pack(anchor="w")
rb_verde = tk.Radiobutton(root, text="Verde", variable=color_var, value="green", command=cambiar_color)
rb_verde.pack(anchor="w")
rb_azul = tk.Radiobutton(root, text="Azul", variable=color_var, value="blue", command=cambiar_color)
rb_azul.pack(anchor="w")

root.mainloop()
