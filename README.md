# Directed Weighted Graph Algorithms:                                                                
## Dor Harizi
## Bar Nahmias [[GitHub](https://github.com/BarNahmias)]

# Design and implementation of directed and weighted graphs 

![This is an image](https://user-images.githubusercontent.com/92825016/145035678-cd125e45-64d7-4055-91bb-646ddfbf99ba.png)  

## Getting Started
**libraries:** 
1. import heapq
2. import json
3. import math
4. import sys
5. from abc import ABC
6. from typing import List, Dict, Any
7. from matplotlib import pyplot as pt

8. from src.Graph_Interface.GraphAlgoInterface import GraphAlgoInterface
9. from src.My_Graph.DiGraph import DiGraph
10. from src.My_Graph.NodeData import NodeData as n

## class
1. DiGraph - this class create object from type graph.
2. NodeData - this class create object from type node.
3. EdgeData - this class create object from type edge.
4. Main -  this class the linked to class MyGui,my_Algo and create DirectedWeightedGraph  .
5. GeaphAlgo - this class include  function that we use on graph.
7. MyGui - graphic interface.


## uml :
![image](https://user-images.githubusercontent.com/92825016/147459626-3b932f75-a56a-48b7-95c9-e204352a13e3.png)  


## GeaphAlgo - function:
#### **init()**
Inits the graph on which this set of algorithms operates on.


#### **shortestPathDist()**
Computes the length of the shortest path between src to dest
Note: if no such path --> returns -1.
 - this function based on **Diastra** algorithm. 
0. For each vertex, it is marked whether they visited it or not and what is the distance from the vertex of the source, which we will mark in S. At first all the codes are marked as not visited, and distance is defined as infinity.
Algorithm loop:
1. As long as there are codes we did not visit:
2. Mark X (the current vertex. In this first iteration the vertex of the source S) as the vertex visited.
3. For any code that is X and we have not yet visited it:
Y is updated so that its distance is equal to the minimum value between two values: between the current distance, the weight of the arc connecting X and Y and the distance between S and X.
4. Make a new vertex X according to a code that this distance from the source node S is the shortest of all the vertices in the graph that we have not yet visited.
* This site was built using [Wikipedia Pages](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm).
#### **shortestPath()**
Computes the the shortest path between src to dest - as an ordered List of nodes:
src--> n1-->n2-->...dest
Note if no such path --> returns null;

This function is based on the function **shortestPathDist()** and return shorter List of nodes.

#### **center()**
 Finds the NodeData which minimizes the max distance to all the other nodes.
 Assuming the graph isConnected, elese return null. 
 return the Node data to which the max shortest path to all the other nodes is minimized
1. for all node in the graph we find the biggest **shortestPathDist()**.
2. we find the node that the smaller  biggest **shortestPathDist()** .
3. this node is the center node. 
* This site was built using [Wikipedia Pages]( https://en.wikipedia.org/wiki/Graph_center).

#### **tsp()**
Computes a list of consecutive nodes which go over all the nodes in cities.
the sum of the weights of all the consecutive (pairs) of nodes (directed) is the "cost" of the solution -
the lower the better.
  - this function based on **greedy** algorithm. 
1. we choosing start node and we find the next node  with the shorter distans .
2. for the node that we found (1) we found agen the next node  with the shorter distans and repeating .
3. from the last node we found the shorter distans to start node. 
* This site was built using [Wikipedia Pages]( https://en.wikipedia.org/wiki/Travelling_salesman_problem).

#### **save()**
 Saves this weighted (directed) graph to the given
 file name - in JSON format.
#### **load()**
This method loads a graph to this graph algorithm.
param file - file name of JSON file

## Run times :

**Building large graphs:**

- 1,000 Vertices 10,000 Edges: 153 ms
- 10,000 Vertices 100,000 Edges: 511 ms
- 100,000 Vertices 1,000,000 Edges: 5 sec 422 ms

**Running Algorithms:**
**isConnected + load file**:

- 1,000 Vertices 10,000 Edges: 185 ms
- 10,000 Vertices 100,000 Edges: 579 ms
- 100,000 Vertices 2,000,000 Edges: 5 sec 708 ms

**shorterpas + load file**:

- 1,000 Vertices 10,000 Edges: 201 ms
- 10,000 Vertices 100,000 Edges: 1 min 216 sec
- 100,000 Vertices 1,000,000 Edges: timeout

## GUI - graphic interface :
When you open 'GUI' from Main class will open panel thet creat the graph from the json file thet you laod:
![image](https://user-images.githubusercontent.com/92825016/147473194-ee0c4908-db46-4f1f-a75d-68ee6f08a048.png)

you can chose to laod other graph or to operate the functuion(from GraphAlgo) on the graph.

When you finish you can to save the graph or to exit from 'GUI'.
![image](https://user-images.githubusercontent.com/92825016/147473376-3886c907-eca3-4b27-a87f-70bcc1b06bba.png)



**BarNahmias&DorHrizi**
