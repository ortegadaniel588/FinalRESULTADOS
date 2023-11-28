from Modelos.Resultado import Resultado
from Modelos.Candidato import Candidato
from Modelos.Mesa import Mesa
from Repositorios.RepositorioResultado import RepositorioResultado
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioMesa import RepositorioMesa


class ControladorResultado():
    def __init__(self):
        # Se crea una instancia del RepositorioEstudiante para interactuar con la base de datos
        self.repositorioResultado = RepositorioResultado()
        self.repositorioCandidatos = RepositorioCandidato()
        self.repositorioMesas = RepositorioMesa()

    def index(self):
        # Retorna todos los estudiantes existentes en la base de datos
        return self.repositorioResultado.findAll()

    def create(self, infoResultado, id_candidato, id_mesa):
        nuevoResultado = Resultado(infoResultado)
        elCandidato = Candidato(self.repositorioCandidatos.findById(id_candidato))
        laMesa = Mesa(self.repositorioMesas.findById(id_mesa))
        nuevoResultado.candidato = elCandidato
        nuevoResultado.mesa = laMesa
        return self.repositorioResultado.save(nuevoResultado)

    def show(self, id):
        elResultado = Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__

    def update(self, id, infoResultado, id_candidato, id_mesa):
        elResultado = Resultado(self.repositorioResultado.findById(id))
        elResultado.id = infoResultado["id"]
        elResultado.numero_mesa = infoResultado["numero_mesa"]
        elResultado.resultado = infoResultado["resultado"]
        elCandidato = Candidato(self.repositorioCandidatos.findById(id_candidato))
        laMesa = Mesa(self.repositorioMesas.findById(id_mesa))
        elResultado.candidato = elCandidato
        elResultado.mesa = laMesa
        return self.repositorioResultado.save(elResultado)

    def delete(self, id):
        return self.repositorioResultado.delete(id)

    def listarResultadosEnMesa(self, id_mesa):
        return self.repositorioResultado.getListadoResultadosEnMesa(id_mesa)

    def resultadosMasAltasPorCurso(self):
        return self.repositorioResultado.getMayorResultadoPorMesa()

    # obtener el promedio de las notas
    def promedioResultadosEnMesa(self, id_mesa):
        return self.repositorioResultado.promedioResultadosEnMesa(id_mesa)