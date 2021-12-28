import copy
import time
import unittest
from unittest import TestCase
# from src.DiGraph import DiGraph
# from src.GraphAlgo import GraphAlgo

from src.My_Graph.DiGraph import DiGraph
from src.My_Graph.GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):
    def test_get_graph(self):
        g1_algo = GraphAlgo()
        g1_algo.load_from_json("../data/A0.json")


        A0=g1_algo.get_graph()

        # self.assertEqual(A0,g1_algo.get_graph())

        # self.fail()

    def test_load_from_json(self):
        self.fail()

    def test_save_to_json(self):
        self.fail()

    def test_shortest_path(self):
        g1_algo = GraphAlgo()
        g1_algo.load_from_json("../data/A0.json")
        A0=(4.3086815935816, [0, 1, 2, 3])

        # self.assertTupleEqual(A0, g1_algo.shortest_path(0,3))

    def test_tsp(self):
        g1_algo = GraphAlgo()
        g1_algo.load_from_json("../src/data/A0.json")
        A0=([{0,35.18753053591606,32.10378225882353,0.0}, {1,35.18958953510896,32.10785303529412,0.0}, { 2,35.19341035835351,32.10610841680672,0.0}, {3,35.197528356739305,32.1053088,0.0}, {4,35.2016888087167,32.10601755126051,0.0}, {5,35.20582803389831,32.10625380168067,0.0}, {6,35.20792948668281,32.10470908739496,0.0}, {7,35.20746249717514,32.10254648739496,0.0}, {8,35.20319591121872,32.1031462,0.0}, {9,35.19597880064568,32.10154696638656,0.0}, {10,35.18910131880549,32.103618700840336,0.0}], 14.470852790366884)
        # self.assertTupleEqual(A0,g1_algo.TSP(g1_algo.graph.get_all_v()))
        #
        # self.fail()

    def test_center_point(self):
        g1_algo = GraphAlgo()
        g1_algo.load_from_json("../src/data/A0.json")
        A0 = (7, 6.806805834715163)
        A1 = 8, 9.925289024973141
        A2 = 0, 7.819910602212574
        A3 = 2, 8.182236568942237
        A4 = 6, 8.071366078651435
        A5 = 40, 9.291743173960954
        # self.assertTupleEqual(A0 , g1_algo.centerPoint())
        # self.assertTupleEqual(A2 , g1_algo.centerPoint())
        # self.assertTupleEqual(A3 , g1_algo.centerPoint())
        # self.assertTupleEqual(A4 , g1_algo.centerPoint())
        # self.assertTupleEqual(A5 , g1_algo.centerPoint())

        # self.fail()

    def test_plot_graph(self):
        self.fail()
