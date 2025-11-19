class Usuario:
    def __init__(self, nombre, edad, genero, avatar=""):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.avatar = avatar

class GestorUsuarios:
    def __init__(self):
        self._usuarios = []
        self._cargar_datos_de_ejemplo()

    def _cargar_datos_de_ejemplo(self):
        self._usuarios.append(Usuario("Alicia", 25, "F"))
        self._usuarios.append(Usuario("Borja", 30, "M"))
        self._usuarios.append(Usuario("Carlos", 28, "M"))

    def listar(self):
        return self._usuarios

    def obtener(self, indice):
        return self._usuarios[indice]
