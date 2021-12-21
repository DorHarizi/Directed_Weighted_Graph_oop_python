import json
from abc import ABC
from typing import List

from src.GraphAlgoInterface import GraphAlgoInterface
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
        hasLoaded = False
        try:
            with open(file_name, "r") as f:
                new_graph = json.load(f)
                if new_graph is not None:
                    new_Vertices = new_graph["Nodes"]
                    new_Edges = new_graph["Edges"]
                    for v in new_Vertices:
                        if v["id"] is not None and v["pos"] is not None:
                            # need to check if this call to function without the less parameters its ok;
                            vertex = n(key=v["id"], pos=v["pos"])
                            self.graph.list_Of_Nodes[vertex.key] = vertex
                            self.graph.mC = self.graph.mC + 1
                    for v in new_Edges:
                        if v["src"] is not None and v["dest"] is not None and v["w"] is not None:
                            self.graph.list_of_Edge_Src[v["src"]]["dest"] = v["w"]
                            self.graph.list_of_Edge_Dest[v["dest"]][v["src"]] = v["w"]
                            self.graph.size_Of_Edge = self.graph.size_Of_Edge + 1
                            self.graph.mC = self.graph.mC + 1
                    hasLoaded = True
        except IOError as e:
            print(e)
            print("\nJson file wasn't found!")
        return hasLoaded

    """
    Saves the graph in JSON format to a file
    """

    def save_to_json(self, file_name: str) -> bool:
        my_json_graph = dict()
        Nodes = []
        Edges = []
        for v in self.graph.list_Of_Nodes:
            node_id = v["key"]
            node_pos = v["pos"]
            node = {"id": node_id, "pos": node_pos}
            Nodes.append(node)
        for src in self.graph.get_all_v().keys():
            for dest, wight in self.graph.all_out_edges_of_node(src).items():
                edge = {"src": src,  "dest": dest, "w": wight}
                Edges.append(edge)
        my_json_graph["Edges"] = Edges
        my_json_graph["Nodes"] = Nodes
        try:
            with open(file_name, "w") as file:
                json.dump(my_json_graph, default=lambda graph: graph.__dict__, indent=4, fp=file)
                hasSaved = True
        except IOError as e:
            print(e)
            hasSaved = False
        return hasSaved

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
