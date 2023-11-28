from Modelos.Partido import Partido
from Repositorios.RepositorioPartido import RepositorioPartido


class ControladorPartido():
    def __init__(self):
        # Se crea una instancia del RepositorioEstudiante para interactuar con la base de datos
        self.repositorioPartido = RepositorioPartido()

    def index(self):
        # Retorna todos los estudiantes existentes en la base de datos
        return self.repositorioPartido.findAll()

    def create(self, infoPartido):
        # Crea un nuevo objeto Estudiante a partir de la información recibida
        nuevoPartido = Partido(infoPartido)

        # Guarda el nuevo estudiante en la base de datos utilizando el repositorio
        return self.repositorioPartido.save(nuevoPartido)

    def show(self, id):
        # Obtiene un estudiante por su ID desde la base de datos utilizando el repositorio
        elPartido = Partido(self.repositorioPartido.findById(id))

        # Retorna los atributos del estudiante como un diccionario
        return elPartido.__dict__

    def update(self, id, infoPartido):
        # Obtiene el estudiante actual por su ID desde la base de datos utilizando el repositorio
        partidoActual = Partido(self.repositorioPartido.findById(id))

        # Actualiza los atributos del estudiante con la información recibida
        partidoActual.id = infoPartido["id"]
        partidoActual.nombre = infoPartido["nombre"]
        partidoActual.lema = infoPartido["lema"]

        # Guarda los cambios del estudiante actualizado en la base de datos utilizando el repositorio
        return self.repositorioPartido.save(partidoActual)

    def delete(self, id):
        # Elimina un estudiante por su ID desde la base de datos utilizando el repositorio
        return self.repositorioPartido.delete(id)
