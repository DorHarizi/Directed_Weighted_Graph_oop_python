import os
from sys import getsizeof
from tkinter import *
from tkinter.ttk import Notebook

from src.My_Graph import DiGraph
from src.My_Graph.NodeData import NodeData as n
from matplotlib import pyplot as plt
import matplotlib
import pandas as pd
import numpy as np

matplotlib.use("TkAgg")
import src.My_Graph.GraphAlgo
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

####################################### create the main window #########################################################


window = Tk()

# getting screen width and height of display
width_window = window.winfo_screenwidth()
height_window = window.winfo_screenheight()
# width_button = (int(width_window / 8))
# setting tkinter window size
window.geometry("%dx%d" % (width_window, height_window))
window.title("Directed Weighted Graph Algorithm")
window.config(background="darkgray")

frame_buttons = Frame(window, bg="black")
frame_buttons.pack(side=TOP)
frame_graph = Frame(window)
frame_graph.pack(fill=BOTH, expand=True)


# icon_window = PhotoImage(file='algorithm-icon.png')
# window.iconphoto(False, icon_window)

#################################### label graph our window#############################################################
# g1_algo = GraphAlgo()
# g1_algo.load_from_json(r"C:\Users\dorha\PycharmProjects\Directed_Weighted_Graph_oop_python\src\data\A0.json")


def frameGraph(graphAlgo):
    fig, axes = plt.subplots()
    xMax = -float('inf')
    xMin = float('inf')
    yMax = -float('inf')
    yMin = float('inf')
    for node in graphAlgo.graph.get_all_v().values():
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
    for node_edge in graphAlgo.graph.get_all_v().values():
        src = n.get_key(node_edge)
        src_pos = n.get_pos(node_edge)
        for dest in graphAlgo.graph.all_out_edges_of_node(src):
            dest_pos = n.get_pos(graphAlgo.graph.get_node(dest))
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
    mainWindow = FigureCanvasTkAgg(fig, master=frame_graph)
    mainWindow.draw()
    mainWindow.get_tk_widget().pack(side=TOP)
    window.mainloop()
    plt.show()


#################################### frame top of our window ###########################################################


######################## The functions that make the process after the user click the button ###########################
def clickTsp():
    print("we need to arrange this function after we wrote the TSP")


def clickShortestPath():
    print("we need to arrange this function after we wrote the shortest_path")


def clickCenterPoint():
    print("we need to arrange this function after we wrote the center_point")


def clickAddEdge():
    print("we need to arrange this function after we wrote the add_edge")


def clickAddNode():
    print("we need to arrange this function after we wrote the add_node")


def clickRemoveNode():
    print("we need to arrange this function after we wrote the remove_node")


def clickRemoveEdge():
    print("we need to arrange this function after we wrote the remove_edge")


#################################### buttons of our window ###########################################################

center_point = Button(frame_buttons,
                      text="Center Point",
                      command=clickCenterPoint,
                      font=("Comic Sans", 25),
                      width=10,
                      fg="darkorange",
                      bg="black",
                      activeforeground="darkorange",
                      activebackground="black"
                      )

shortest_path = Button(frame_buttons,
                       text="Shortest Path",
                       command=clickShortestPath,
                       font=("Comic Sans", 25),
                       width=10,
                       fg="darkorange",
                       bg="black",
                       activeforeground="darkorange",
                       activebackground="black"
                       )

tsp = Button(frame_buttons,
             text="TSP",
             command=clickTsp,
             font=("Comic Sans", 25),
             width=10,
             fg="darkorange",
             bg="black",
             activeforeground="darkorange",
             activebackground="black"
             )

add_node = Button(frame_buttons,
                  text="Add Node",
                  command=clickAddNode,
                  font=("Comic Sans", 25),
                  width=10,
                  fg="darkorange",
                  bg="black",
                  activeforeground="darkorange",
                  activebackground="black"
                  )

add_edge = Button(frame_buttons,
                  text="Add Edge",
                  command=clickAddEdge,
                  font=("Comic Sans", 25),
                  width=10,
                  fg="darkorange",
                  bg="black",
                  activeforeground="darkorange",
                  activebackground="black"
                  )

remove_node = Button(frame_buttons,
                     text="Remove Node",
                     command=clickRemoveNode,
                     font=("Comic Sans", 25),
                     width=15,
                     fg="darkorange",
                     bg="black",
                     activeforeground="darkorange",
                     activebackground="black"
                     )

remove_edge = Button(frame_buttons,
                     text="Remove Edge",
                     command=clickRemoveEdge,
                     font=("Comic Sans", 25),
                     width=15,
                     fg="darkorange",
                     bg="black",
                     activeforeground="darkorange",
                     activebackground="black"
                     )

center_point.pack(side=LEFT)
shortest_path.pack(side=LEFT)
tsp.pack(side=LEFT)
add_node.pack(side=LEFT)
add_edge.pack(side=LEFT)
remove_node.pack(side=RIGHT)
remove_edge.pack(side=RIGHT)


################################### tab control ########################################################################
# tabControl = Notebook(window)
# tabControl.pack(side=LEFT)
# # make frame
# leftFrame = Frame(tabControl,width=width_window-100,height=height_window-100)
# leftFrame.pack(side=TOP)
# # add to tab controll
# tabControl.add(leftFrame, text="Frame 1")
# # add seccond frame
# rightFrame = Frame(tabControl,width=width_window-100,height=height_window-100)
# rightFrame.pack(side=TOP)
# tabControl.add(rightFrame, text="Frame 2")
# tabControl.config(background="black")

################### The functions that make the process after the user click the menubar Options #######################
def new():
    pass


def load():
    pass


def save():
    pass


def clear():
    pass


def Vertices():
    pass


def Edges():
    pass


def Graph():
    pass


################################################### menubar ###########################################################

menuBar = Menu(window)

fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New", command=new)
fileMenu.add_command(label="Load", command=load)
fileMenu.add_command(label="Save", command=save)

fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=window.quit)

menuBar.add_cascade(label="File", menu=fileMenu)

editMenu = Menu(menuBar, tearoff=0)
editMenu.add_command(label="Add Node", command=add_node)
editMenu.add_command(label="Add Edge", command=add_edge)
editMenu.add_command(label="Remove Node", command=remove_node)
editMenu.add_command(label="Remove Edge", command=remove_edge)
editMenu.add_command(label="Clear", command=clear)

menuBar.add_cascade(label="Edit", menu=editMenu)

DataGraphMenu = Menu(menuBar, tearoff=0)
DataGraphMenu.add_command(label="Graph", command=Graph)
DataGraphMenu.add_command(label="Vertices", command=Vertices)
DataGraphMenu.add_command(label="Edges", command=Edges)
menuBar.add_cascade(label="Data Of Graph", menu=DataGraphMenu)

window.config(menu=menuBar)

########################################### pyplotGraph #############################################################


############################################# The end of frame #########################################################

# window.mainloop()
