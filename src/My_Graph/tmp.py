# import matplotlib
#
# matplotlib.use("TkAgg")
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
# from matplotlib.figure import Figure
#
# import tkinter as tk
# from tkinter import ttk
#
# LARGE_FONT = ("Verdana", 12)
#
#
# class SeaofBTCapp(tk.Tk):
#
#     def __init__(self, *args, **kwargs):
#         tk.Tk.__init__(self, *args, **kwargs)
#
#         tk.Tk.iconbitmap(self, default="clienticon.ico")
#         tk.Tk.wm_title(self, "Sea of BTC client")
#
#         container = tk.Frame(self)
#         container.pack(side="top", fill="both", expand=True)
#         container.grid_rowconfigure(0, weight=1)
#         container.grid_columnconfigure(0, weight=1)
#
#         self.frames = {}
#
#         for F in (StartPage, PageOne, PageTwo, PageThree):
#             frame = F(container, self)
#
#             self.frames[F] = frame
#
#             frame.grid(row=0, column=0, sticky="nsew")
#
#         self.show_frame(StartPage)
#
#     def show_frame(self, cont):
#         frame = self.frames[cont]
#         frame.tkraise()
#
#
# class StartPage(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = tk.Label(self, text="Start Page", font=LARGE_FONT)
#         label.pack(pady=10, padx=10)
#
#         button = ttk.Button(self, text="Visit Page 1",
#                             command=lambda: controller.show_frame(PageOne))
#         button.pack()
#
#         button2 = ttk.Button(self, text="Visit Page 2",
#                              command=lambda: controller.show_frame(PageTwo))
#         button2.pack()
#
#         button3 = ttk.Button(self, text="Graph Page",
#                              command=lambda: controller.show_frame(PageThree))
#         button3.pack()
#
#
# class PageOne(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
#         label.pack(pady=10, padx=10)
#
#         button1 = ttk.Button(self, text="Back to Home",
#                              command=lambda: controller.show_frame(StartPage))
#         button1.pack()
#
#         button2 = ttk.Button(self, text="Page Two",
#                              command=lambda: controller.show_frame(PageTwo))
#         button2.pack()
#
#
# class PageTwo(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
#         label.pack(pady=10, padx=10)
#
#         button1 = ttk.Button(self, text="Back to Home",
#                              command=lambda: controller.show_frame(StartPage))
#         button1.pack()
#
#         button2 = ttk.Button(self, text="Page One",
#                              command=lambda: controller.show_frame(PageOne))
#         button2.pack()
#
#
# class PageThree(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
#         label.pack(pady=10, padx=10)
#
#         button1 = ttk.Button(self, text="Back to Home",
#                              command=lambda: controller.show_frame(StartPage))
#         button1.pack()
#
#         f = Figure(figsize=(5, 5), dpi=100)
#         a = f.add_subplot(111)
#         a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])
#
#         canvas = FigureCanvasTkAgg(f, self)
#         canvas.show()
#         canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
#
#         toolbar = NavigationToolbar2Tk(canvas, self)
#         toolbar.update()
#         canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
#
#
# app = SeaofBTCapp()
# app.mainloop()
import tkinter as tk
from tkinter import TOP


def show_frame(frame):
    frame.tkraise()


window = tk.Tk()
window.state('zoomed')

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)

for frame in (frame1, frame2, frame3):
    frame.grid(row=0, column=0, sticky='nsew')

# ==================Frame 1 code
frame1_title = tk.Label(frame1, text='Page 1', font='times 35', bg='red')
frame1_title.pack(fill='both', expand=True)

frame1_btn = tk.Button(frame1, text='Enter', command=lambda: show_frame(frame2))
frame1_btn.pack(fill='x', ipady=15)

# ==================Frame 2 code
frame2_title = tk.Label(frame2, text='Page 2', font='times 35', bg='yellow')
frame2_title.pack(fill='both', expand=True)

frame2_btn = tk.Button(frame2, text='Enter', command=lambda: show_frame(frame3))
frame2_btn.pack(fill='x', ipady=15)

# ==================Frame 3 code
frame3_title = tk.Label(frame3, text='Page 3', font='times 35', bg='green')
frame3_title.pack(fill='both', expand=True)

frame3_btn = tk.Button(frame3, text='Enter', command=lambda: show_frame(frame1))
frame3_btn.pack(fill='x', ipady=15)

show_frame(frame1)

window.mainloop()