import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.brands = DAO.get_all_brands()
        self.graph = None

    def build_graph(self, brand, year):
        self.graph = nx.Graph()
        nodes = DAO.get_nodes(brand)
        self.graph.add_nodes_from(nodes)
        for u in self.graph.nodes:
            for v in self.graph.nodes:
                if u != v:
                    peso = DAO.get_peso(u.Product_number, v.Product_number, year)
                    if peso > 0:
                        self.graph.add_edge(u, v, weight=peso)
        return self.graph

    def get_archi_pesanti(self):
        sorted_edges = list(self.graph.edges)
        sorted_edges.sort(key=lambda e: self.graph[e[0]][e[1]]['weight'], reverse=True)
        duplicati = self.get_duplicati(sorted_edges[:3])
        return sorted_edges[:3], duplicati

    def get_duplicati(self, edge_list):
        duplicati = set()
        for edge in edge_list:
            for node in edge:
                c = 0
                for e in edge_list:
                    if e[0] == node or e[1] == node:
                        c += 1
                if c > 1:
                    duplicati.add(node)
        return list(duplicati)
