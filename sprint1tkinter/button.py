import tkinter as tk

def mostrar_mensaje():
    etiqueta.config(text="¡Has presionado el botón!")

root = tk.Tk()
root.title("Ejercicio de botones")
root.geometry("300x150")

etiqueta = tk.Label(root, text="Presiona un botón", font=("Arial", 12))
etiqueta.pack(pady=20)

boton_mensaje = tk.Button(root, text="Mostrar mensaje", command=mostrar_mensaje)
boton_mensaje.pack(pady=5)

boton_salir = tk.Button(root, text="Salir", command=root.quit)
boton_salir.pack(pady=5)

root.mainloop()
