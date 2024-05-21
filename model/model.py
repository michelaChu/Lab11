import networkx as nx

from database.DAO import DAO
class Model:
    def __init__(self):
        self._allColors = DAO.getALlColors()
        self._grafo = nx.Graph()


    def creaGrafo(self, colore, anno):

        nodi = DAO.getALlNodes(colore)
        idMap = {}
        for n in nodi:
            idMap[n.Product_number] = n
        self._grafo.add_nodes_from(nodi)
        archi = DAO.getALlEdges(anno, colore)
        for a in archi:
            v0 = idMap[a[0]]
            v1 = idMap[a[1]]
            self._grafo.add_edge(v0, v1, weight=a[2])

    def getTop3(self):
        return sorted(self._grafo.edges(data=True), key=lambda x: x[2]['weight'], reverse=True)[:3]

    def getNumNodes(self):
        return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)