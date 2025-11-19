from model.usuario_model import GestorUsuarios
from view.main_view import MainView

class AppController:
    def __init__(self, master):
        self.model = GestorUsuarios()
        self.view = MainView(master)
        self.refrescar_lista_usuarios()

    def refrescar_lista_usuarios(self):
        self.view.actualizar_lista_usuarios(self.model.listar(), self.seleccionar_usuario)

    def seleccionar_usuario(self, indice):
        usuario = self.model.obtener(indice)
        self.view.mostrar_detalles_usuario(usuario)
