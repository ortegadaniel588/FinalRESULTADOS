from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorPartido import ControladorPartido
from Controladores.ControladorResultado import ControladorResultado

app = Flask(__name__)
cors = CORS(app)

## Ejecutando controlador Candidato
miControladorMesa = ControladorMesa()
miControladorCandidato = ControladorCandidato()
miControladorPartido = ControladorPartido()
miControladorResultado = ControladorResultado()
"""
Servicio que el servidor ofrecerá, y este consiste en retornar un JSON el cual
tiene un mensaje que dice que el servidor está corriendo.
"""


@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)


#########################################
##peticiones del servidor respecto a Mesa
@app.route("/mesas", methods=['GET'])
def getMesas():
    json = miControladorMesa.index()
    return jsonify(json)


@app.route("/mesas", methods=['POST'])
def crearMesa():
    data = request.get_json()
    json = miControladorMesa.create(data)
    return jsonify(json)


@app.route("/mesas/<string:id>", methods=['GET'])
def getMesa(id):
    json = miControladorMesa.show(id)
    return jsonify(json)


@app.route("/mesas/<string:id>", methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()
    json = miControladorMesa.update(id, data)
    return jsonify(json)


@app.route("/mesas/<string:id>", methods=['DELETE'])
def eliminarMesa(id):
    json = miControladorMesa.delete(id)
    return jsonify(json)


## fin peticion Mesa


###############################################
##peticiones del servidor respecto a Candidato
@app.route("/candidatos", methods=['GET'])
def getCandidatos():
    json = miControladorCandidato.index()
    return jsonify(json)


@app.route("/candidatos", methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json = miControladorCandidato.create(data)
    return jsonify(json)


@app.route("/candidatos/<string:id>", methods=['GET'])
def getCandidato(id):
    json = miControladorCandidato.show(id)
    return jsonify(json)


@app.route("/candidatos/<string:id>", methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    json = miControladorCandidato.update(id, data)
    return jsonify(json)


@app.route("/candidatos/<string:id>", methods=['DELETE'])
def eliminarCandidato(id):
    json = miControladorCandidato.delete(id)
    return jsonify(json)


@app.route("/candidatos/<string:id>/partido/<string:id_partido>", methods=['PUT'])
def asignarPartidoACandidato(id, id_partido):
    json = miControladorCandidato.asignarPartido(id, id_partido)
    return jsonify(json)


## fin peticion candidato


##peticiones del servidor respecto a Partido

@app.route("/partidos", methods=['GET'])
def getPartidos():
    json = miControladorPartido.index()
    return jsonify(json)


@app.route("/partidos", methods=['POST'])
def crearPartido():
    data = request.get_json()
    json = miControladorPartido.create(data)
    return jsonify(json)


@app.route("/partidos/<string:id>", methods=['GET'])
def getPartido(id):
    json = miControladorPartido.show(id)
    return jsonify(json)


@app.route("/partidos/<string:id>", methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json = miControladorPartido.update(id, data)
    return jsonify(json)


@app.route("/partidos/<string:id>", methods=['DELETE'])
def eliminarPartido(id):
    json = miControladorPartido.delete(id)
    return jsonify(json)


## fin peticion Partido

###############################################
##peticiones del servidor respecto a Resultado
# ---------------modificado por DANIEL-----------------------------

@app.route("/resultados", methods=['GET'])
def getResultados():
    json = miControladorResultado.index()
    return jsonify(json)


@app.route("/resultados/<string:id>", methods=['GET'])
def getResultado(id):
    json = miControladorResultado.show(id)
    return jsonify(json)


@app.route("/resultados/candidato/<string:id_candidato>/mesa/<string:id_mesa>", methods=['POST'])
def crearResultado(id_candidato, id_mesa):
    data = request.get_json()
    json = miControladorResultado.create(data, id_candidato, id_mesa)
    return jsonify(json)


@app.route("/resultados/<string:id_resultado>/candidato/<string:id_candidato>/mesa/<string:id_mesa>", methods=['PUT'])
def modificarResultado(id_resultado, id_candidato, id_mesa):
    data = request.get_json()
    json = miControladorResultado.update(id_resultado, data, id_candidato, id_mesa)
    return jsonify(json)


@app.route("/resultados/<string:id_resultado>", methods=['DELETE'])
def eliminarResultado(id_resultado):
    json = miControladorResultado.delete(id_resultado)
    return jsonify(json)


@app.route("/resultados/mesa/<string:id_mesa>", methods=['GET'])
def inscritosEnMesa(id_mesa):
    json = miControladorResultado.listarResultadosEnMesa(id_mesa)
    return jsonify(json)


@app.route("/resultados/resultados_mayores", methods=['GET'])
def getResultadosMayores():
    json = miControladorResultado.resultadosMasAltasPorCurso()
    return jsonify(json)


@app.route("/resultados/promedio_resultados/mesa/<string:id_mesa>", methods=['GET'])
def getPromedioResultadosEnMesa(id_mesa):
    json = miControladorResultado.promedioResultadosEnMesa(id_mesa)
    return jsonify(json)


# ---------------end modificado por DANIEL-----------------------------

## fin peticion Resultado


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
