# controller/app_controller.py

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from pathlib import Path
from PIL import Image
from view.main_view import AddUserView, MainView
from model.usuario_model import Usuario, GestorUsuarios


class AppController:
    def __init__(self, master):
        self.master = master

        self.BASE_DIR = Path(__file__).resolve().parent.parent
        self.ASSETS_PATH = self.BASE_DIR / "assets"

        # 🔑 CORRECCIÓN: Eliminar el argumento 'self.ASSETS_PATH' para evitar TypeError.
        self.model = GestorUsuarios()

        self.view = MainView(master)

        self.avatar_images = {}

        self.view.add_user_button.configure(command=self.abrir_ventana_añadir)

        self.refrescar_lista_usuarios()

    # --- Métodos de Listado/Selección ---

    def refrescar_lista_usuarios(self):
        usuarios = self.model.listar()
        self.view.actualizar_lista_usuarios(usuarios, self.seleccionar_usuario)
        self.view.limpiar_detalles()

    def seleccionar_usuario(self, indice: int):
        usuario = self.model.obtener_por_indice(indice)
        if usuario:
            image_obj = self._obtener_imagen_avatar(usuario.avatar)
            self.view.mostrar_detalles_usuario(usuario, image_obj)
        else:
            messagebox.showerror("Error", "Usuario no encontrado.")

    # --- Manejo de Imágenes ---

    def _obtener_imagen_avatar(self, filename: str) -> ctk.CTkImage:
        if filename not in self.avatar_images:
            try:
                # La ruta de assets se usa aquí, que es correcto
                image_path = self.ASSETS_PATH / filename

                pil_img = Image.open(image_path)
                image = ctk.CTkImage(light_image=pil_img, size=(100, 100))
                self.avatar_images[filename] = image

            except Exception:
                placeholder = self._get_placeholder_image()
                self.avatar_images[filename] = placeholder
                return placeholder

        return self.avatar_images[filename]

    def _get_placeholder_image(self) -> ctk.CTkImage:
        if "placeholder" not in self.avatar_images:
            img = Image.new('RGB', (100, 100), color='gray')
            photo = ctk.CTkImage(light_image=img, size=(100, 100))
            self.avatar_images["placeholder"] = photo
        return self.avatar_images["placeholder"]

    # --- Abrir la ventana modal ---
    def abrir_ventana_añadir(self):
        add_view = AddUserView(self.master)
        add_view.guardar_button.configure(
            command=lambda: self.añadir_usuario(add_view)
        )

    # --- Procesar datos y añadir usuario ---
    def añadir_usuario(self, add_view):
        data = add_view.get_data()
        nombre = data["nombre"].strip()
        edad_str = data["edad"].strip()
        genero = data["genero"].strip()
        avatar_file = data["avatar"].strip()

        if not nombre:
            messagebox.showerror("Error", "El nombre no puede estar vacío.")
            return

        try:
            edad = int(edad_str)
            if edad <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "La edad debe ser un número entero positivo.")
            return

        usuario = Usuario(nombre, edad, genero, avatar_file)
        self.model.agregar(usuario)

        self.refrescar_lista_usuarios()

        add_view.window.destroy()