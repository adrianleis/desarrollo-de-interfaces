import tkinter as tk

root = tk.Tk()
root.title("Text con Scrollbar")
root.geometry("400x300")

frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

scroll = tk.Scrollbar(frame)
scroll.pack(side="right", fill="y")

texto = tk.Text(frame, wrap="word", yscrollcommand=scroll.set)
texto.pack(side="left", fill="both", expand=True)

scroll.config(command=texto.yview)

texto.insert("end", "Este es un texto largo de ejemplo.\n" * 50)

root.mainloop()
