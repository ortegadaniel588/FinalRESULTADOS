from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultado import Resultado
from bson import ObjectId


class RepositorioResultado(InterfaceRepositorio[Resultado]):
    def getListadoResultadosEnMesa(self, id_mesa):
        theQuery = {"mesa.$id":ObjectId(id_mesa)}
        return self.query(theQuery)

    def getMayorResultadoPorMesa(self):
        query1 = {
            "$group": {
                "_id": "$mesa",
                "max": {
                    "$max": "$resultado"
                },
                "doc": {
                    "$first": "$$ROOT"
                }
            }
        }

        pipeline = [query1]
        return self.queryAggregation(pipeline)

    def promedioResultadosEnMesa(self, id_mesa):
        query1 = {
            "$match": {"mesa.$id": ObjectId(id_mesa)}
        }

        query2 = {
            "$group": {
                "_id": "$mesa",
                "promedio": {
                   "$avg": "$resultado"
                }
            }
        }

        pipeline = [query1, query2]

        return self.queryAggregation(pipeline)