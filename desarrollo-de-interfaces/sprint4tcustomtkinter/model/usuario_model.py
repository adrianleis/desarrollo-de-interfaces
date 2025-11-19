from typing import List
import csv
from pathlib import Path

class Usuario:
    def __init__(self, nombre: str, edad: int, genero: str, avatar: str):
        self.nombre = nombre
        self.edad = int(edad)
        self.genero = genero
        self.avatar = avatar


class GestorUsuarios:
    def __init__(self):
        self._usuarios: List[Usuario] = []
        # La carga de ejemplo se llama solo si cargar_csv falla al inicio
        pass

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

    def guardar_csv(self, ruta_archivo: Path):
        with open(ruta_archivo, 'w', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f)
            escritor.writerow(['nombre', 'edad', 'genero', 'avatar'])
            for u in self._usuarios:
                escritor.writerow([u.nombre, u.edad, u.genero, u.avatar])

    def cargar_csv(self, ruta_archivo: Path) -> int:
        try:
            with open(ruta_archivo, 'r', newline='', encoding='utf-8') as f:
                lector = csv.reader(f)
                next(lector)
                self._usuarios.clear()
                cargados = 0
                for fila in lector:
                    try:
                        nombre, edad_str, genero, avatar = fila
                        edad = int(edad_str)
                        if edad <= 0:
                            raise ValueError
                        usuario = Usuario(nombre, edad, genero, avatar)
                        self._usuarios.append(usuario)
                        cargados += 1
                    except Exception:
                        pass # Ignorar filas corruptas

            return cargados

        except FileNotFoundError:
            return 0