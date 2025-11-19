import customtkinter as ctk

class MainView:
    def __init__(self, master):
        self.master = master
        self.frame_left = ctk.CTkFrame(master)
        self.frame_left.grid(row=0, column=0, sticky="nswe", padx=(10,5), pady=10)

        self.frame_right = ctk.CTkFrame(master)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=(5,10), pady=10)

        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=2)
        master.grid_rowconfigure(0, weight=1)

        self.lista_usuarios_scrollable = ctk.CTkScrollableFrame(self.frame_left)
        self.lista_usuarios_scrollable.pack(fill="both", expand=True, padx=5, pady=5)

        self.label_nombre = ctk.CTkLabel(self.frame_right, text="Nombre:")
        self.label_nombre.pack(anchor="w", pady=2)

        self.label_edad = ctk.CTkLabel(self.frame_right, text="Edad:")
        self.label_edad.pack(anchor="w", pady=2)

        self.label_genero = ctk.CTkLabel(self.frame_right, text="Género:")
        self.label_genero.pack(anchor="w", pady=2)

    def actualizar_lista_usuarios(self, usuarios, on_seleccionar_callback):
        for w in self.lista_usuarios_scrollable.winfo_children():
            w.destroy()
        for i, u in enumerate(usuarios):
            btn = ctk.CTkButton(
                self.lista_usuarios_scrollable,
                text=u.nombre,
                command=lambda idx=i: on_seleccionar_callback(idx)
            )
            btn.pack(fill="x", padx=5, pady=2)

    def mostrar_detalles_usuario(self, usuario):
        self.label_nombre.configure(text=f"Nombre: {usuario.nombre}")
        self.label_edad.configure(text=f"Edad: {usuario.edad}")
        self.label_genero.configure(text=f"Género: {usuario.genero}")
