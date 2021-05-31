"""
Question 1

from tkinter import *
from tkinter.ttk import *
def clear_data(data):
    return data.set("")
    
window = Tk()
data = StringVar()
data.set("Data to display")
label = Label(window, textvariable=data)
label.grid(row=0, column=0)
entry = Entry(window, textvariable=data)
entry.grid(row=1, column=0)
clear = Button(window, text="Clear", command=lambda: clear_data(data))
clear.grid(row=2, column=0)
s = Style() 
s.configure('TButton', font='helvetica 24', foreground='green')
quit = Button(window, text="Quit", command=window.destroy)
quit.grid(row=3, column=0)

window.mainloop()
"""

"""
#Packer
from tkinter import *
from tkinter.ttk import * 
window = Tk()
side_labels = ["bottom1", "bottom2", "top1", "top2", "left1", "right1"]
for theside in side_labels:
    button = Button(window, text=theside)
    button.pack(side=theside[0:-1])
window.mainloop()
"""
"""
#Gridder
from tkinter import *
from tkinter.ttk import * 
window = Tk()
for label_num in range(6):
    button = Button(window, text="Button"+str(label_num))
    button.grid(row=label_num // 3, column=label_num % 3)
window.mainloop()
"""
"""
#Gridder continued
from tkinter import *
from tkinter.ttk import * 
window = Tk()
for label_num in range(6):
    button = Button(window, text="Button" + str(label_num))
    button.grid(row=label_num // 2, column=label_num % 3)
    if label_num==1:
        button.grid(columnspan=2, sticky="ew")
    elif label_num==3:
        button.grid(rowspan=2, sticky="ns")
window.columnconfigure(1, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.mainloop()
"""
"""
#Frames
from tkinter import *
from tkinter.ttk import * 
window = Tk()
frame_left = Frame(window, borderwidth=4, relief=RIDGE)
frame_left.pack(side="left", fill="y", padx=5, pady=5)
frame_right = Frame(window)
frame_right.pack(side="right")

button1 = Button(frame_left, text="Button 1")
button1.pack(side="top")
button2 = Button(frame_left, text="Button 2")
button2.pack(side="bottom")

for label_num in range(4):
    button = Button(frame_right, text="Button" + str(label_num + 3))
    button.grid(row=label_num // 2, column=label_num % 2)
window.mainloop()
"""
"""
Question 2

from tkinter import *
from tkinter.ttk import * 
window = Tk()
verticalscrollbar = Scrollbar(window)
verticalscrollbar.pack(side=RIGHT, fill=Y)
horizontalscrollbar = Scrollbar(window, orient=HORIZONTAL)
horizontalscrollbar.pack(side=BOTTOM, fill=X)
text = Text(window, height=10, wrap=NONE, width=24, xscrollcommand=horizontalscrollbar.set, yscrollcommand=verticalscrollbar.set)
horizontalscrollbar.config(command=text.xview)
verticalscrollbar.config(command=text.yview)
text.pack()
window.mainloop()
"""
"""
from tkinter import *
from tkinter.ttk import * 
def add_one():
    value.set(value.get()+1)

def wow(event):
    label2.config(text="WWWWOOOOWWWW")

window = Tk()
value = IntVar(0)
label = Label(window, textvariable=value)
label.pack()
label2 = Label(window)
label2.pack()
button = Button(window, text="Add one", command=add_one)
button.bind("<Shift-Double-Button-1>", wow)
button.pack()
window.mainloop()
"""
"""
from tkinter import *
from tkinter.ttk import * 
def change(the_value, n):
    the_value.set(the_value.get()+n)

window = Tk()
value = IntVar(0)
label = Label(window, textvariable=value)
label.pack()
button = Button(window, text="Left +1, Right -1")
button.bind("<Button-1>", lambda event: change(value, 1))
button.bind("<Button-3>", lambda event: change(value, -1))
button.pack()
window.mainloop()
"""
from tkinter import *
from tkinter.ttk import *

def append(ch):
    thing = labeltext.get()
    labeltext.set(thing + ch)

def clear():
    labeltext.set("")

window = Tk()
frame = Frame(window, borderwidth=1, relief=RIDGE)
frame.pack(side=BOTTOM, padx=10, pady=10)
labeltext = StringVar()
label = Label(window, textvariable=labeltext)
label.pack(side=LEFT, padx=25)
clearbutton = Button(window, text='Clear', command=lambda: clear())
clearbutton.pack(side=RIGHT, padx=30)
board = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
for i in range(len(board)):
    for j in range(len(board[i])):
        button = Button(frame, text=board[i][j], command=lambda x=board[i][j]: append(x))
        button.grid(column=(2 * j)+i, row=i, columnspan=2)
window.mainloop()