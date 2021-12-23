import json
import sys
from abc import ABC
from typing import List
from matplotlib import pyplot as pt

from src.Graph_Interface.GraphAlgoInterface import GraphAlgoInterface
from src.My_Graph.DiGraph import DiGraph
from src.My_Graph.NodeData import NodeData as n
from src.My_Graph.EdgeData import EdgeData as e


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
                        if v["id"] is not None:
                            # need to check if this call to function without the less parameters its ok;
                            key = v["id"]
                            pos = v["pos"]
                            self.graph.add_node(key, pos)
                    for v in new_Edges:
                        if v["src"] is not None and v["dest"] is not None and v["w"] is not None:
                            self.graph.add_edge(v["src"], v["dest"], v["w"])
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
        for v in self.graph.get_all_v():
            node_id = n.get_key(v)
            node_pos = n.get_pos(v)
            node = {"id": node_id, "pos": node_pos}
            Nodes.append(node)
        for src in self.graph.get_all_v().keys():
            for dest, wight in self.graph.all_out_edges_of_node(src).items():
                edge = {"src": src, "dest": dest, "w": wight}
                Edges.append(edge)
        my_json_graph["Nodes"] = Nodes
        my_json_graph["Edges"] = Edges
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
        if self.graph is None or self.graph.get_all_v(id1) is None or self.graph.get_all_v(id2) is None:
            return float('inf'), []
        if id1 == id2:
            return float('inf'), []

        nodes = self.graph.get_all_v()

        if id1 not in nodes or id2 not in nodes:
            return float('inf'), []

        for node in nodes:
            n.set_tag(node, False)
            n.set_weight(node, sys.maxsize)  # set  weight

        stack = {}  # create a stack  for the node we pass
        shortest_path = {}  # create a dictionary for path  nodes

        # nodes[id][0]=0
        n.set_weight(nodes.keys(id1), 0)
        stack[id1] = 0
        while len(stack) != 0:
            min_node = -1
            min_weight = sys.maxsize
            for i in stack.keys():
                if n.get_weight(i) < min_weight:
                    # if nodes.get(i)[4]<min_weight:
                    #     min_weight=nodes.get(i)[4]
                    min_weight == n.get_weight(i)
                    min_node = i

            if min_node == nodes.get(id2):
                break

            po = self.graph.get_all_v(min_node)
            stack.pop(min_node)
            neighbors = self.graph.all_out_edges_of_node(min_node)
            for edge in neighbors:
                if n.get_tag(edge) == False and e.get_weight(edge) + n.get_weight(po) < n.get_weight(node):
                    # if nodes.get(i)[3]==False and neighbors.get(i) + po < nodes.get(i)[4]:]
                    n.set_weight(node, (e.get_weight(edge) + e.get_weight(po)))
                    # nodes.get(i)[3]=neighbors.get(i) + po
                    shortest_path[edge] = min_node
                    stack[edge] = neighbors.get(edge)
                n.set_tag(nodes.get(min_node), True)
            # nodes.get(min_node)[3]=True
            if shortest_path.get(id2) is None:  # if we didn't found predecessor to the dest node
                return float("inf"), []

            path = [
                id2]  # create a list that illustrate the shortest path and add the last vertex= the dest of the path
            while id2 != id1:  # while isn't the start of the path
                id2 = shortest_path.get(id2)  # get the previous vertex that we came from it to the current vertex
                path.insert(0, id2)  # add it to the top of list
            return n.get_weight(nodes.get(id2)), path  # return the path

    """
    Finds the shortest path that visits all the nodes in the list
    Return list of the nodes id's in the path, and the overall distance
    """

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        start = node_lst[0]
        mini = sys.maxsize
        citys = []
        citys.append(start)
        weight = 0

        for city in citys:

            n.get_key(neighbors.keys(edge)) != n.get_key(city)

            neighbors = self.graph.all_out_edges_of_node(city)

            for edge in neighbors:
                if e.get_src(edge) in node_lst and n.get_tag(e.get_src(edge)) == False and e.get_src(
                        edge) < mini and e.get_src(edge) != n.get(city):
                    mini = e.get_weight(edge)
                    # mini=neighbors[i][4]
                    n.set_tag(e.get_src(edge), True)
                    # neighbors[i][3] =True
                    # weight=weight+neighbors[i][4]
                    next = e.get_src(edge)

                citys.append(next)
                weight = weight + mini

        if len(city) < len(node_lst):
            return -1
        if len(city) == len(node_lst):
            return city, weight

    """
    Finds the node that has the shortest distance to it's farthest node.
    Return The nodes id, min-maximum distance
    """

    def centerPoint(self) -> (int, float):
        mincenter = sys.maxsize
        lst_graph = self.graph.get_all_v()
        center = -1
        for node in lst_graph:
            biggestDistance = 0
            for i in lst_graph:
                weight = GraphAlgo.shortest_path(node, n.get_key(i))
                if weight > biggestDistance:
                    biggestDistance = weight
                    center = i

            if biggestDistance < mincenter:
                mincenter = biggestDistance
                node_center = center

        return node_center

    """
    Plots the graph.
    If the nodes have a position, the nodes will be placed there.
    Otherwise, they will be placed in a random but elegant manner.
    Return None
    """

    def plot_graph(self) -> None:
        fig, ax = pt.subplots()
        for node in self.graph.get_all_v().values():
            pos_tmp = n.get_pos(node)
            id_tmp = n.get_key(node)
            ax.scatter(pos_tmp[0], pos_tmp[1], color="blue", zorder=10)
            ax.annotate(id_tmp, (pos_tmp[0], pos_tmp[1]))  # draw the Nodes of the graph
        for node_edge in self.graph.get_all_v().values():
            src = n.get_key(node_edge)
            src_pos = n.get_pos(node_edge)
            for dest in self.graph.all_out_edges_of_node(src):
                dest_pos = n.get_pos(self.graph.get_node(dest))
                xSrc = src_pos[0]
                ySrc = src_pos[1]
                xDest = dest_pos[0]
                yDest = dest_pos[1]
                pt.plot([xSrc, xDest], [ySrc, yDest])  # draw the Edges of the graph
        # pt.xlabel("x axis")
        # pt.ylabel("y axis")
        pt.title("Directed Graph")
        pt.show()
