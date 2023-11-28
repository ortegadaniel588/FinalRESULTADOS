from Modelos.Candidato import Candidato
from Modelos.Partido import Partido
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioPartido import RepositorioPartido


class ControladorCandidato():
    def __init__(self):
        # Se crea una instancia del RepositoroCandidato para interactuar con la base de datos
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioPartido = RepositorioPartido()

    def index(self):
        # Retorna todos los candidatos existentes en la base de datos
        return self.repositorioCandidato.findAll()

    def create(self, infoCandidato):
        # Crea un nuevo objeto Candidato a partir de la información recibida
        nuevoCandidato = Candidato(infoCandidato)

        # Guarda el nuevo candidato en la base de datos utilizando el repositorio
        return self.repositorioCandidato.save(nuevoCandidato)

    def show(self, id):
        # Obtiene un candidato por su ID desde la base de datos utilizando el repositorio
        elCandidato = Candidato(self.repositorioCandidato.findById(id))

        # Retorna los atributos del candidato como un diccionario
        return elCandidato.__dict__

    def update(self, id, infoCandidato):
        # Obtiene el candidato actual por su ID desde la base de datos utilizando el repositorio
        candidatoActual = Candidato(self.repositorioCandidato.findById(id))

        # Actualiza los atributos del candidato con la información recibida
        candidatoActual.cedula = infoCandidato["cedula"]
        candidatoActual.numero_resolucion = infoCandidato["numero_resolucion"]
        candidatoActual.nombre = infoCandidato["nombre"]
        candidatoActual.apellido = infoCandidato["apellido"]

        # Guarda los cambios del candidato actualizado en la base de datos utilizando el repositorio
        return self.repositorioCandidato.save(candidatoActual)

    def delete(self, id):
        # Elimina un candidato por su ID desde la base de datos utilizando el repositorio
        return self.repositorioCandidato.delete(id)

    """
    Relación Candidato y partido
    """

    def asignarPartido(self, id, id_partido):
        candidatoActual = Candidato(self.repositorioCandidato.findById(id))
        partidoActual = Partido(self.repositorioPartido.findById(id_partido))
        candidatoActual.partido = partidoActual
        return self.repositorioCandidato.save(candidatoActual)
