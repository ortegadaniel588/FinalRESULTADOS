from Modelos.Mesa import Mesa
from Repositorios.RepositorioMesa import RepositorioMesa


class ControladorMesa():
    def __init__(self):
        # Se crea una instancia del RepositorioEstudiante para interactuar con la base de datos
        self.repositorioMesa = RepositorioMesa()

    def index(self):
        # Retorna todos los estudiantes existentes en la base de datos
        return self.repositorioMesa.findAll()

    def create(self, infoMesa):
        # Crea un nuevo objeto Estudiante a partir de la información recibida
        nuevoMesa = Mesa(infoMesa)

        # Guarda el nuevo estudiante en la base de datos utilizando el repositorio
        return self.repositorioMesa.save(nuevoMesa)

    def show(self, id):
        # Obtiene un estudiante por su ID desde la base de datos utilizando el repositorio
        elMesa = Mesa(self.repositorioMesa.findById(id))

        # Retorna los atributos del estudiante como un diccionario
        return elMesa.__dict__

    def update(self, id, infoMesa):
        # Obtiene el estudiante actual por su ID desde la base de datos utilizando el repositorio
        mesatoActual = Mesa(self.repositorioMesa.findById(id))

        # Actualiza los atributos del estudiante con la información recibida
        mesatoActual.numero = infoMesa["numero"]
        mesatoActual.cantidad_inscritos = infoMesa["cantidad_inscritos"]

        # Guarda los cambios del estudiante actualizado en la base de datos utilizando el repositorio
        return self.repositorioMesa.save(mesatoActual)

    def delete(self, id):
        # Elimina un estudiante por su ID desde la base de datos utilizando el repositorio
        return self.repositorioMesa.delete(id)