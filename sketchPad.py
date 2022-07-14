from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

import random
import time

# Sketchpad is a subclass of Canvas, and so inherits all the data
class Sketchpad(Canvas):

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.resultsContents = StringVar()
        self.resultsContents.set("Beginning...")
        self.create_label( parent)
        
        # Bindings
        self.bind("<Button-1>", self.save_posn)
        # self.bind("<B1-Motion>", self.add_line)
        self.draw_ovals()

    def draw_ovals( self):
        rx = random.randrange( 745)
        ry = random.randrange( 427)
        self.create_oval( rx, ry, rx + 5, ry + 5, fill='red', outline='blue')

    def create_text( self, parent):
        self.text = Text( parent, width=40, height=250)
        self.text.grid( column=1, row=0, sticky=(N, W))
        self.text.insert( '1.0', 'hello world')

    def update_text( self):
        self.text.insert( '1.0', " %s, %s"%(self.lastx, self.lasty))
        
    def create_label( self, parent):
        self.label = ttk.Label( parent, text='You\'ve clicked... \n:', width=25)
        self.label.grid( column=1, row=0, sticky=( N, W))
        self.label['textvariable'] = self.resultsContents
        # return None

    # This is a little silly, i wish I could use references but oh well
    def update_label( self):
        self.resultsContents.set("You've clicked on... %s, %s"%(self.lastx, self.lasty))
        
    def save_posn(self, event):
        self.lastx, self.lasty = event.x, event.y
        # sneaky way to do multiple bindings i guess...
        self.update_label()
        self.draw_ovals()
        
    def add_line(self, event):
        self.create_line((self.lastx, self.lasty, event.x, event.y))
        self.save_posn(event)

root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe = ttk.Frame( root, padding="3 3 12 12")
mainframe.grid( column=0, row=0, sticky=( N, W, E, S))

sketch = Sketchpad( mainframe, width=750, height=432)
sketch.grid(column=0, row=0, sticky=(N, W, E, S))

myimg = ImageTk.PhotoImage(Image.open('imgs/world_map.png').resize( (750, 432)))
sketch.create_image(10, 10, image=myimg, anchor='nw')
# sketch.create_oval(10, 10, 15, 15, fill='red', outline='blue')

root.mainloop()
        
