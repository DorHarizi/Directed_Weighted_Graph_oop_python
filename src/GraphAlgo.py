from abc import ABC
from typing import List

from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface
from src.DiGraph import DiGraph
from src.NodeData import NodeData as n


class GraphAlgo(GraphAlgoInterface, ABC):

    def __init__(self, graph: DiGraph = None):
        if graph is not None:
            self.graph = graph
        else:
            self.graph = DiGraph()

    """
    Return the directed graph on which the algorithm works on.
    """
    def get_graph(self) -> DiGraph:
        return self.graph

    """
    Loads a graph from a json file.
    """
    def load_from_json(self, file_name: str) -> bool:
        pass

    """
    Saves the graph in JSON format to a file
    """
    def save_to_json(self, file_name: str) -> bool:
        pass

    """
    Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
    Example:
    g_algo = GraphAlgo()
    g_algo.addNode(0)
    g_algo.addNode(1)
    g_algo.addNode(2)
    g_algo.addEdge(0,1,1)
    g_algo.addEdge(1,2,4)
    g_algo.shortestPath(0,1)
    (1, [0, 1])
    g_algo.shortestPath(0,2)
    (5, [0, 1, 2])
    Notes:
    If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])
    """
    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    """
    Finds the shortest path that visits all the nodes in the list
    Return list of the nodes id's in the path, and the overall distance
    """
    def TSP(self, node_lst: List[int]) -> (List[int], float):
        super().TSP(node_lst)

    """
    Finds the node that has the shortest distance to it's farthest node.
    Return The nodes id, min-maximum distance
    """
    def centerPoint(self) -> (int, float):
        super().centerPoint()

    """
    Plots the graph.
    If the nodes have a position, the nodes will be placed there.
    Otherwise, they will be placed in a random but elegant manner.
    Return None
    """
    def plot_graph(self) -> None:
        pass
