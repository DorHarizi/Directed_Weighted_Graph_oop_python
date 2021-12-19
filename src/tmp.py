from abc import ABC
from src.NodeData import NodeData
from src.GraphInterface import GraphInterface


class DiGraph(GraphInterface, ABC):

    def __init__(self):
        self.list_Of_Nodes = dict()
        self.list_of_Edge_Dest = dict()
        self.list_of_Edge_Src = dict()
        self.size_Of_Edges = 0
        self.mC = 0

    def __repr__(self):
        return 'Nodes(x=%s)' % self.list_Of_Nodes.keys()

    """
     Returns the number of vertices in this graph.
     """

    def v_size(self) -> int:
        return len(self.list_Of_Nodes)

    """
    Returns the number of edges in this graph.
    """

    def e_size(self) -> int:
        return self.size_Of_Edges

    """
    Returns the current version of this graph.
    """

    def get_mc(self) -> int:
        return self.mC

    """
    Adds an edge to the graph.
    """

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        pass

    """
    Adds a node to the graph.
    """

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        pass

    """
    Removes a node from the graph.
    """

    def remove_node(self, node_id: int) -> bool:
        pass

    """
    Removes an edge from the graph.
    """

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        pass