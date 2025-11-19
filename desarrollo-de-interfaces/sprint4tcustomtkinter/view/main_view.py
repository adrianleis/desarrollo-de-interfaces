import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from typing import Dict, Any, Optional, List, Callable


class Usuario:
    def __init__(self, nombre: str, edad: int, genero: str, avatar: str):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.avatar = avatar


class AddUserView:
    def __init__(self, master: ctk.CTk):
        self.window = ctk.CTkToplevel(master)
        self.window.title("Añadir Nuevo Usuario")
        self.window.geometry("350x450")
        self.window.resizable(False, False)
        self.window.grab_set()

        self.genero_var = tk.StringVar(value="Otro")
        self.avatar_var = tk.StringVar(value="avatar1.jpg")

        ctk.CTkLabel(self.window, text="Nombre:").pack(pady=(15, 0))
        self.nombre_entry = ctk.CTkEntry(self.window, width=250)
        self.nombre_entry.pack(pady=5)

        ctk.CTkLabel(self.window, text="Edad:").pack(pady=(10, 0))
        self.edad_entry = ctk.CTkEntry(self.window, width=250)
        self.edad_entry.pack(pady=5)

        ctk.CTkLabel(self.window, text="Género:").pack(pady=(10, 5))
        ctk.CTkRadioButton(self.window, text="Masculino", variable=self.genero_var, value="Masculino").pack(anchor="w",
                                                                                                            padx=50)
        ctk.CTkRadioButton(self.window, text="Femenino", variable=self.genero_var, value="Femenino").pack(anchor="w",
                                                                                                          padx=50)
        ctk.CTkRadioButton(self.window, text="Otro", variable=self.genero_var, value="Otro").pack(anchor="w", padx=50)

        ctk.CTkLabel(self.window, text="Avatar:").pack(pady=(15, 5))
        ctk.CTkRadioButton(self.window, text="Avatar 1", variable=self.avatar_var, value="avatar1.jpg").pack(anchor="w",
                                                                                                             padx=50)
        ctk.CTkRadioButton(self.window, text="Avatar 2", variable=self.avatar_var, value="avatar2.jpg").pack(anchor="w",
                                                                                                             padx=50)
        ctk.CTkRadioButton(self.window, text="Avatar 3", variable=self.avatar_var, value="avatar3.jpg").pack(anchor="w",
                                                                                                             padx=50)

        btn_frame = ctk.CTkFrame(self.window, fg_color="transparent")
        btn_frame.pack(pady=20)

        self.guardar_button = ctk.CTkButton(btn_frame, text="Guardar")
        self.guardar_button.pack(side="left", padx=10)

        self.cancelar_button = ctk.CTkButton(btn_frame, text="Cancelar", command=self.window.destroy)
        self.cancelar_button.pack(side="left", padx=10)

    def get_data(self) -> Dict[str, str]:
        return {
            "nombre": self.nombre_entry.get(),
            "edad": self.edad_entry.get(),
            "genero": self.genero_var.get(),
            "avatar": self.avatar_var.get()
        }


class MainView:
    def __init__(self, master: ctk.CTk):
        self.master = master
        self.avatar_image_ref = None

        self.menubar = tk.Menu(master)
        master.config(menu=self.menubar)

        self.menu_archivo = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Archivo", menu=self.menu_archivo)

        self.menu_ayuda = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Ayuda", menu=self.menu_ayuda)

        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=3)
        master.grid_rowconfigure(0, weight=1)
        master.grid_rowconfigure(1, weight=0)
        master.grid_rowconfigure(2, weight=0)

        self.lista_usuarios_frame = ctk.CTkFrame(master)
        self.lista_usuarios_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")
        self.lista_usuarios_frame.grid_rowconfigure(1, weight=1)

        ctk.CTkLabel(self.lista_usuarios_frame, text="Usuarios", font=ctk.CTkFont(size=16, weight="bold")).pack(
            pady=(10, 5))
        self.lista_usuarios_scrollable = ctk.CTkScrollableFrame(self.lista_usuarios_frame)
        self.lista_usuarios_scrollable.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        self.add_user_button = ctk.CTkButton(self.lista_usuarios_frame, text="Añadir Usuario")
        self.add_user_button.pack(fill="x", padx=10, pady=(0, 10))

        self.detalles_frame = ctk.CTkFrame(master)
        self.detalles_frame.grid(row=0, column=1, padx=(0, 10), pady=(10, 0), sticky="nsew")
        self.detalles_frame.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(self.detalles_frame, text="Detalles del Usuario", font=ctk.CTkFont(size=16, weight="bold")).pack(
            pady=10)

        self.avatar_label = ctk.CTkLabel(self.detalles_frame, text="[Avatar]", font=ctk.CTkFont(size=20), image=None)
        self.avatar_label.pack(pady=20)

        self.nombre_label = ctk.CTkLabel(self.detalles_frame, text="Nombre: -")
        self.nombre_label.pack(pady=5)
        self.edad_label = ctk.CTkLabel(self.detalles_frame, text="Edad: -")
        self.edad_label.pack(pady=5)
        self.genero_label = ctk.CTkLabel(self.detalles_frame, text="Género: -")
        self.genero_label.pack(pady=5)

        self.status_bar = ctk.CTkLabel(master, text="Listo.", anchor="w")
        self.status_bar.grid(row=1, column=0, columnspan=2, padx=10, pady=(0, 5), sticky="ew")

        # Botón Salir en la esquina inferior derecha
        ctk.CTkButton(master, text="Salir", command=master.quit).grid(row=2, column=1, padx=(0, 10), pady=10,
                                                                      sticky="e")

    def actualizar_lista_usuarios(self, usuarios: List[Usuario], on_seleccionar_callback: Callable[[int], None]):
        for widget in self.lista_usuarios_scrollable.winfo_children():
            widget.destroy()

        for i, usuario in enumerate(usuarios):
            btn = ctk.CTkButton(
                self.lista_usuarios_scrollable,
                text=usuario.nombre,
                command=lambda idx=i: on_seleccionar_callback(idx)
            )
            btn.pack(fill="x", padx=5, pady=2)

    def mostrar_detalles_usuario(self, usuario: Usuario, avatar_img: ctk.CTkImage):
        self.avatar_image_ref = avatar_img

        self.nombre_label.configure(text=f"Nombre: {usuario.nombre}")
        self.edad_label.configure(text=f"Edad: {usuario.edad}")
        self.genero_label.configure(text=f"Género: {usuario.genero}")

        self.avatar_label.configure(text="", image=self.avatar_image_ref)

    def limpiar_detalles(self):
        self.nombre_label.configure(text="Nombre: -")
        self.edad_label.configure(text="Edad: -")
        self.genero_label.configure(text="Género: -")
        self.avatar_label.configure(text="[Seleccione un usuario]", image=None)
        self.avatar_image_ref = None

    def set_estado(self, mensaje: str):
        self.status_bar.configure(text=mensaje)