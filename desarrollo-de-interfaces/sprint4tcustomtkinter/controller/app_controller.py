import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from pathlib import Path
from PIL import Image
from view.main_view import AddUserView, MainView
from model.usuario_model import Usuario, GestorUsuarios
from typing import List, Dict


class AppController:
    def __init__(self, master):
        self.master = master

        self.BASE_DIR = Path(__file__).resolve().parent.parent
        self.ASSETS_PATH = self.BASE_DIR / "assets"
        self.CSV_PATH = self.BASE_DIR / "usuarios.csv"

        self.model = GestorUsuarios()
        self.view = MainView(master)

        self.avatar_images = {}

        self.view.add_user_button.configure(command=self.abrir_ventana_añadir)

        self._conectar_menu()

        self.cargar_usuarios(feedback=False)
        self.refrescar_lista_usuarios()
        self.view.set_estado("Aplicación iniciada. Lista de usuarios cargada.")

    def _conectar_menu(self):
        self.view.menu_archivo.add_command(label="Guardar", command=self.guardar_usuarios)
        self.view.menu_archivo.add_command(label="Cargar", command=lambda: self.cargar_usuarios(feedback=True))
        self.view.menu_archivo.add_separator()
        self.view.menu_archivo.add_command(label="Salir", command=self.master.quit)

        self.view.menu_ayuda.add_command(label="Acerca de...", command=self.mostrar_info_app)

    def mostrar_info_app(self):
        messagebox.showinfo("Acerca de", "Registro de Usuarios (CTk + MVC)\nPersistencia CSV implementada.")

    # --- Manejadores de Persistencia (Fase 3) ---

    def guardar_usuarios(self):
        self.model.guardar_csv(self.CSV_PATH)
        self.view.set_estado(f"Datos guardados exitosamente en: {self.CSV_PATH.name}")
        messagebox.showinfo("Guardado", "Datos guardados correctamente.")

    def cargar_usuarios(self, feedback: bool = True):
        cargados = self.model.cargar_csv(self.CSV_PATH)

        if cargados > 0:
            self.refrescar_lista_usuarios()
            msg = f"{cargados} usuarios cargados desde {self.CSV_PATH.name}."
            self.view.set_estado(msg)
            if feedback:
                messagebox.showinfo("Carga Exitosa", msg)
        else:
            if feedback:
                messagebox.showwarning("Carga Fallida",
                                       f"No se pudo cargar el archivo '{self.CSV_PATH.name}' o estaba vacío.")

            # Si no hay datos persistentes, cargamos los de ejemplo por defecto
            if not self.model.listar():
                self.model._cargar_datos_de_ejemplo()

            self.refrescar_lista_usuarios()
            self.view.set_estado("Cargando datos de ejemplo (CSV no encontrado o vacío).")

    # --- Lógica de la Aplicación ---

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

    def _obtener_imagen_avatar(self, filename: str) -> ctk.CTkImage:
        if filename not in self.avatar_images:
            try:
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

    def abrir_ventana_añadir(self):
        add_view = AddUserView(self.master)
        add_view.guardar_button.configure(
            command=lambda: self.añadir_usuario(add_view)
        )

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