from tkinter import *

import matplotlib
from matplotlib import pyplot as plt

from src.My_Graph import GraphAlgo
from src.My_Graph.NodeData import NodeData as n

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


####################################### create the main window #########################################################
class my_frame:
    def __init__(self, myGraphAlgo: GraphAlgo = None):
        self.graphAlgo = myGraphAlgo
        self.window = Tk()
        self.width_window = self.window.winfo_screenwidth()
        self.height_window = self.window.winfo_screenheight()
        self.window.geometry("%dx%d" % (self.width_window, self.height_window))
        self.window.title("Directed Weighted Graph Algorithm")
        self.menuBar = Menu(self.window)
        self.frame_buttons = Frame(self.window, bg="black")
        self.frame_buttons.pack(side=TOP)
        self.frame_graph = Frame(self.window)
        self.frame_graph.pack(fill=BOTH, expand=True)
        self.windowMenuBar()
        self.windowFrameButtons()
        self.windowFrameGraph()

    ################### The functions that make the process after the user click the menubar Options #######################
    def new(self):
        print("we need to arrange this function after we wrote the remove_edge")

    def load(self):
        print("we need to arrange this function after we wrote the remove_edge")

    def save(self):
        print("we need to arrange this function after we wrote the remove_edge")

    def clear(self):
        print("we need to arrange this function after we wrote the remove_edge")

    def Vertices(self):
        windowNodes = Tk()
        nodesString = {}
        for node in self.graphAlgo.graph.list_Of_Nodes.values:
            strTmp = {'{"id" =%d,"pos"=%s}' % (n.get_key(node), n.get_pos(node))}
            nodesString.update(strTmp)
        labelNodes = Label(windowNodes,
                           font=('Ariel', 20, 'bold'),
                           fg='white',
                           bg='black',
                           relife=RAISED,
                           padx=20,
                           pady=20)
        labelNodes.pack()

    def Edges(self):
        windowEdges = Tk()
        labelEdges = Label(windowEdges,
                           font=('Ariel', 20, 'bold'),
                           fg='white',
                           bg='black',
                           relife=RAISED,
                           padx=20,
                           pady=20)
        labelEdges.pack()

    def Graph(self):
        windowGraph = Tk()
        labelGraph = Label(windowGraph,
                           font=('Ariel', 20, 'bold'),
                           fg='white',
                           bg='black',
                           relife=RAISED,
                           padx=20,
                           pady=20)
        labelGraph.pack()

    ######################## The functions that make the process after the user click the button ######################

    def clickCenterPoint(self):
        print("we need to arrange this function after we wrote the center_point")

    def clickShortestPath(self):
        print("we need to arrange this function after we wrote the shortest_path")

    def clickTsp(self):
        print("we need to arrange this function after we wrote the TSP")

    def clickAddEdge(self):
        print("we need to arrange this function after we wrote the add_edge")

    def clickAddNode(self):
        print("we need to arrange this function after we wrote the add_node")

    def clickRemoveNode(self):
        print("we need to arrange this function after we wrote the remove_node")

    def clickRemoveEdge(self):
        print("we need to arrange this function after we wrote the remove_edge")

    ########################################## menubar of our window ##################################################
    def windowMenuBar(self):

        fileMenu = Menu(self.menuBar, tearoff=0)
        fileMenu.add_command(label="New", command=self.new)
        fileMenu.add_command(label="Load", command=self.load)
        fileMenu.add_command(label="Save", command=self.save)

        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self.window.quit)

        self.menuBar.add_cascade(label="File", menu=fileMenu)

        editMenu = Menu(self.menuBar, tearoff=0)
        editMenu.add_command(label="Add Node", command=self.clickAddNode)
        editMenu.add_command(label="Add Edge", command=self.clickAddEdge)
        editMenu.add_command(label="Remove Node", command=self.clickRemoveNode)
        editMenu.add_command(label="Remove Edge", command=self.clickRemoveEdge)
        editMenu.add_command(label="Clear", command=self.clear)

        self.menuBar.add_cascade(label="Edit", menu=editMenu)

        DataGraphMenu = Menu(self.menuBar, tearoff=0)
        DataGraphMenu.add_command(label="Graph", command=self.Graph)
        DataGraphMenu.add_command(label="Vertices", command=self.Vertices)
        DataGraphMenu.add_command(label="Edges", command=self.Edges)
        self.menuBar.add_cascade(label="Data Of Graph", menu=DataGraphMenu)

        self.window.config(menu=self.menuBar)

    #################################### buttons of our window ########################################################
    def windowFrameButtons(self):
        center_point = Button(self.frame_buttons,
                              text="Center Point",
                              command=self.clickCenterPoint,
                              font=("Comic Sans", 25),
                              width=10,
                              fg="darkorange",
                              bg="black",
                              activeforeground="darkorange",
                              activebackground="black"
                              )
        center_point.pack(side=LEFT)

        shortest_path = Button(self.frame_buttons,
                               text="Shortest Path",
                               command=self.clickShortestPath,
                               font=("Comic Sans", 25),
                               width=10,
                               fg="darkorange",
                               bg="black",
                               activeforeground="darkorange",
                               activebackground="black"
                               )
        shortest_path.pack(side=LEFT)

        tsp = Button(self.frame_buttons,
                     text="TSP",
                     command=self.clickTsp,
                     font=("Comic Sans", 25),
                     width=10,
                     fg="darkorange",
                     bg="black",
                     activeforeground="darkorange",
                     activebackground="black"
                     )
        tsp.pack(side=LEFT)

        add_node = Button(self.frame_buttons,
                          text="Add Node",
                          command=self.clickAddNode,
                          font=("Comic Sans", 25),
                          width=10,
                          fg="darkorange",
                          bg="black",
                          activeforeground="darkorange",
                          activebackground="black"
                          )
        add_node.pack(side=LEFT)

        add_edge = Button(self.frame_buttons,
                          text="Add Edge",
                          command=self.clickAddEdge,
                          font=("Comic Sans", 25),
                          width=10,
                          fg="darkorange",
                          bg="black",
                          activeforeground="darkorange",
                          activebackground="black"
                          )
        add_edge.pack(side=LEFT)

        remove_node = Button(self.frame_buttons,
                             text="Remove Node",
                             command=self.clickRemoveNode,
                             font=("Comic Sans", 25),
                             width=15,
                             fg="darkorange",
                             bg="black",
                             activeforeground="darkorange",
                             activebackground="black"
                             )
        remove_node.pack(side=RIGHT)

        remove_edge = Button(self.frame_buttons,
                             text="Remove Edge",
                             command=self.clickRemoveEdge,
                             font=("Comic Sans", 25),
                             width=15,
                             fg="darkorange",
                             bg="black",
                             activeforeground="darkorange",
                             activebackground="black"
                             )
        remove_edge.pack(side=RIGHT)

    #################################### frame graph of our window########################################################
    def windowFrameGraph(self):
        fig, axes = plt.subplots()
        xMax = -float('inf')
        xMin = float('inf')
        yMax = -float('inf')
        yMin = float('inf')
        for node in self.graphAlgo.graph.get_all_v().values():
            pos_tmp = n.get_pos(node)
            id_tmp = n.get_key(node)
            if xMax < pos_tmp[0]:
                xMax = pos_tmp[0]
            if pos_tmp[0] < xMin:
                xMin = pos_tmp[0]
            if yMax < pos_tmp[1]:
                yMax = pos_tmp[1]
            if pos_tmp[1] < yMin:
                yMin = pos_tmp[0]
            axes.scatter(pos_tmp[0], pos_tmp[1], color="yellow", zorder=15)
            axes.annotate(id_tmp, (pos_tmp[0] + 0.0001, pos_tmp[1] + 0.00015), color="orange",
                          fontsize=15)  # draw the Nodes of the graph
        for node_edge in self.graphAlgo.graph.get_all_v().values():
            src = n.get_key(node_edge)
            src_pos = n.get_pos(node_edge)
            for dest in self.graphAlgo.graph.all_out_edges_of_node(src):
                dest_pos = n.get_pos(self.graphAlgo.graph.get_node(dest))
                xSrc = src_pos[0]
                ySrc = src_pos[1]
                xDest = dest_pos[0]
                yDest = dest_pos[1]
                plt.plot([xSrc, xDest], [ySrc, yDest], color="white")
        axes.set_facecolor('xkcd:black')
        plt.tick_params(axis='x', which='both', bottom=False,
                        top=False, labelbottom=False)
        plt.tick_params(axis='y', which='both', right=False,
                        left=False, labelleft=False)
        for pos in ['right', 'top', 'bottom', 'left']:
            plt.gca().spines[pos].set_visible(False)
        l = axes.figure.subplotpars.left
        r = axes.figure.subplotpars.right
        t = axes.figure.subplotpars.top
        b = axes.figure.subplotpars.bottom
        figw = float(xMax) / (r - l)
        figh = float((yMin) / (t - b) + 5)
        axes.figure.set_size_inches(figw, figh)
        mainWindow = FigureCanvasTkAgg(fig, master=self.frame_graph)
        mainWindow.draw()
        mainWindow.get_tk_widget().pack(side=TOP)
        self.window.mainloop()

    ################################### new graph after click ########################################################################
    def frameGraphAfterChange(self):
        fig, ax = plt.subplots()
        for node in self.graphAlgo.get_all_v().values():
            pos_tmp = n.get_pos(node)
            id_tmp = n.get_key(node)
            ax.scatter(pos_tmp[0], pos_tmp[1], color="blue", zorder=10)
            ax.annotate(id_tmp, (pos_tmp[0], pos_tmp[1]))  # draw the Nodes of the graph
        for node_edge in self.graphAlgo.get_all_v().values():
            src = n.get_key(node_edge)
            src_pos = n.get_pos(node_edge)
            for dest in self.graphAlgo.all_out_edges_of_node(src):
                dest_pos = n.get_pos(self.graphAlgo.get_node(dest))
                xSrc = src_pos[0]
                ySrc = src_pos[1]
                xDest = dest_pos[0]
                yDest = dest_pos[1]
                plt.plot([xSrc, xDest], [ySrc, yDest], color="black")
        plt.title("Directed Graph")
        plt.show()

    ########################################### pyplotGraph #############################################################

    ############################################# The end of frame #########################################################

    # window.mainloop()
