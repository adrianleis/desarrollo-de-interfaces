from typing import List

class Usuario:
    def __init__(self, nombre: str, edad: int, genero: str, avatar: str):
        self.nombre = nombre
        self.edad = int(edad)
        self.genero = genero
        self.avatar = avatar


class GestorUsuarios:
    def __init__(self):
        self._usuarios: List[Usuario] = []
        self._cargar_datos_de_ejemplo()

    def _cargar_datos_de_ejemplo(self):
        self._usuarios.append(Usuario("Ana López", 28, "Femenino", "avatar1.jpg"))
        self._usuarios.append(Usuario("Javi Pérez", 35, "Masculino", "avatar2.jpg"))
        self._usuarios.append(Usuario("Raul Dominguez", 40, "Masculino", "avatar3.jpg"))
    def listar(self) -> List[Usuario]:
        return self._usuarios

    def obtener_por_indice(self, indice: int) -> Usuario:
        if 0 <= indice < len(self._usuarios):
            return self._usuarios[indice]
        return None

    def agregar(self, usuario: Usuario):
        self._usuarios.append(usuario)