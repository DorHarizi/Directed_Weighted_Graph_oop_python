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
    """
    Finds the shortest path that visits all the nodes in the list
    Return list of the nodes id's in the path, and the overall distance
    """
    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm.
        @param id1: Represents the src node id.
        @param id2: Represents the dest node id.
        @return: The distance of the path and list of the nodes ids that the path goes through.
        If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[]).
        """
        ans = (math.inf, [])
        graph = self.get_graph()
        graph_nodes = graph.get_all_v()
        visited = {}
        distance = {}
        path = {}
        queue = []
        if id1 not in graph_nodes or id2 not in graph_nodes:
            return ans
        if id1 == id2:
            ans = (0, [id1])
            return ans
        for node in graph.get_all_v():
            distance[node] = math.inf
        distance[id1] = 0
        heapq.heappush(queue, (distance[id1], id1))
        while len(queue) != 0:
            current = heapq.heappop(queue)[1]
            if current in visited:
                continue
            else:
                visited[current] = 1
                curr_edges = graph.all_out_edges_of_node(current)
                for tmp_node in curr_edges:
                    edge = curr_edges[tmp_node]
                    if edge + distance[current] < distance[tmp_node]:
                        distance[tmp_node] = edge + distance[current]
                        path[tmp_node] = current
                    if tmp_node not in visited:
                        heapq.heappush(queue, (distance[tmp_node], tmp_node))

        if id2 not in path:
            return ans

        final_distance = 0
        final_list = []
        final_list.append(id2)
        final_distance = distance[id2]
        tmp = path[id2]
        while tmp != id1:
            final_list.append(tmp)
            tmp = path[tmp]
        final_list.append(id1)
        final_list.reverse()
        return (final_distance, final_list)


    def TSP(self, node_lst: List[int]) -> (List[int], float):
        start = node_lst[0]
        visit =[]
        path=[]
        path.append(start)
        citys = []
        citys.append(start)
        weight = 0
        for l in node_lst:
             visit.append(False)

        while True:
            # while len(citys) != 0:

            if False not in visit:
                break

            for city in citys:


                neighbors = self.graph.all_out_edges_of_node(n.get_key(city))
                mini = sys.maxsize

                for edge in neighbors:
                    if visit[edge] is False:
                        # if neighbors.get(edge) < mini and edge != n.get_key(city):
                        if self.shortest_path(n.get_key(city),edge)[0] < mini and edge != n.get_key(city):


                            # mini = neighbors.get(edge)
                            mini = self.shortest_path(n.get_key(city),edge)[0]

                            visit[edge]=True
                            next = node_lst[edge]

                citys.pop(0)
                path.append(next)
                weight = weight + mini
                if False in visit:
                    visit[n.get_key(city)] = True

                    citys.append(next)

        if len(path) < len(node_lst):
                return -1
        if len(path) >= len(node_lst):
             return (path, weight)

        """
        Finds the node that has the shortest distance to it's farthest node.
        Return The nodes id, min-maximum distance
        """

    def centerPoint(self) -> (int, float):
        mincenter = sys.maxsize
        graph = self.graph
        lst_graph = graph.get_all_v()
        center = -1
        for key in lst_graph.keys():

            biggestDistance = 0
            for k in lst_graph.keys():

                id1 = key
                id2 = k

                if id1 == id2:
                    continue

                weight = self.shortest_path(id1, id2)[0]
                if weight > biggestDistance:
                    biggestDistance = weight

            if biggestDistance < mincenter:
                mincenter = biggestDistance
                node_center = key

        return (node_center, mincenter)


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
