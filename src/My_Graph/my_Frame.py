import os
from tkinter import *

####################################### create the main window #########################################################
from tkinter.ttk import Notebook

window = Tk()

# getting screen width and height of display
width_window = window.winfo_screenwidth()
height_window = window.winfo_screenheight()
width_button = (int(width_window/8))
# setting tkinter window size
window.geometry("%dx%d" % (width_window, height_window))
window.title("Directed Weighted Graph Algorithm")
window.config(background="darkgray")
# icon_window = PhotoImage(file='algorithm-icon.png')
# window.iconphoto(False, icon_window)

#################################### label graph our window#############################################################
# frame_graph = Frame(window, bg="darkgray")
# frame_graph.place(x=0, y=30)

#################################### frame top of our window ###########################################################

frame_top = Frame(window, bg="black")
frame_top.pack(side=TOP)


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

center_point = Button(frame_top,
                      text="Center Point",
                      command=clickCenterPoint,
                      font=("Comic Sans", 25),
                      width=10,
                      fg="darkorange",
                      bg="black",
                      activeforeground="darkorange",
                      activebackground="black"
                      )

shortest_path = Button(frame_top,
                       text="Shortest Path",
                       command=clickShortestPath,
                       font=("Comic Sans", 25),
                       width=10,
                       fg="darkorange",
                       bg="black",
                       activeforeground="darkorange",
                       activebackground="black"
                       )

tsp = Button(frame_top,
             text="TSP",
             command=clickTsp,
             font=("Comic Sans", 25),
             width=10,
             fg="darkorange",
             bg="black",
             activeforeground="darkorange",
             activebackground="black"
             )

add_node = Button(frame_top,
                  text="Add Node",
                  command=clickAddNode,
                  font=("Comic Sans", 25),
                  width=10,
                  fg="darkorange",
                  bg="black",
                  activeforeground="darkorange",
                  activebackground="black"
                  )

add_edge = Button(frame_top,
                  text="Add Edge",
                  command=clickAddEdge,
                  font=("Comic Sans", 25),
                  width=10,
                  fg="darkorange",
                  bg="black",
                  activeforeground="darkorange",
                  activebackground="black"
                  )

remove_node = Button(frame_top,
                     text="Remove Node",
                     command=clickRemoveNode,
                     font=("Comic Sans", 25),
                     width=15,
                     fg="darkorange",
                     bg="black",
                     activeforeground="darkorange",
                     activebackground="black"
                     )

remove_edge = Button(frame_top,
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
DataGraphMenu.add_command(label="Vertices", command=Vertices)
DataGraphMenu.add_command(label="Edges", command=Edges)
menuBar.add_cascade(label="Data Of Graph", menu=DataGraphMenu)

window.config(menu=menuBar)

########################################### frame terminal #############################################################
# termf = Frame(window)
#
#
# termf.pack(side=BOTTOM, fill=BOTH, expand=YES)
# wid = termf.winfo_id()
# os.system('xterm -into %d -geometry 100X100 -sb -e "python.exe" &' % wid)


############################################# The end of frame #########################################################
window.mainloop()
