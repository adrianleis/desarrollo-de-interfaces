import tkinter as tk
def cambiar_texto():
    etiqueta3.config(text="¡El texto ha cambiado!")


ventana = tk.Tk()
ventana.title("Ventana con etiquetas")
ventana.geometry("300x200")

etiqueta1 = tk.Label(ventana, text="¡Bienvenido a la aplicación!", font=("Arial", 12))
etiqueta1.pack(pady=10)


etiqueta2 = tk.Label(ventana, text="Tu Nombre Completo", font=("Arial", 12))
etiqueta2.pack(pady=10)


etiqueta3 = tk.Label(ventana, text="Texto original", font=("Arial", 12))
etiqueta3.pack(pady=10)


boton = tk.Button(ventana, text="Cambiar texto", command=cambiar_texto)
boton.pack(pady=10)


ventana.mainloop()

