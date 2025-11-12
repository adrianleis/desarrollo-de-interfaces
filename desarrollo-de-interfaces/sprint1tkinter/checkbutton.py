import tkinter as tk

def actualizar():
    aficiones = []
    if leer_var.get():
        aficiones.append("Leer")
    if deporte_var.get():
        aficiones.append("Deporte")
    if musica_var.get():
        aficiones.append("Música")
    etiqueta.config(text="Aficiones seleccionadas: " + ", ".join(aficiones))

root = tk.Tk()
root.title("Aficiones")
root.geometry("300x200")

leer_var = tk.IntVar()
deporte_var = tk.IntVar()
musica_var = tk.IntVar()

check_leer = tk.Checkbutton(root, text="Leer", variable=leer_var, command=actualizar)
check_leer.pack(anchor="w")
check_deporte = tk.Checkbutton(root, text="Deporte", variable=deporte_var, command=actualizar)
check_deporte.pack(anchor="w")
check_musica = tk.Checkbutton(root, text="Música", variable=musica_var, command=actualizar)
check_musica.pack(anchor="w")

etiqueta = tk.Label(root, text="Aficiones seleccionadas: ", font=("Arial", 12))
etiqueta.pack(pady=10)

root.mainloop()
