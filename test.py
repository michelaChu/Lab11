from model.model import Model
from database.DAO import DAO

myModel = Model()

myModel.creaGrafo("White", 2018)
print(len(myModel._grafo.nodes))
print(len(myModel._grafo.edges))

