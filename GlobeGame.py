from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

import random
import time

# Sizing
WIDTH = 1200
HEIGHT = int(WIDTH * 0.516)

# Sketchpad is a subclass of Canvas, and so inherits all the data
class Sketchpad(Canvas):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        # Setup
        self.resultsContents = StringVar()
        self.resultsContents.set("Beginning...")
        self.create_label( parent)
        self.create_button( parent)
        
        # Bindings
        self.bind("<Button-1>", self.save_posn)
        self.draw_random_ovals()

    def draw_ovals( self, event):
        rx = self.lastx / 2
        ry = self.lasty / 2
        self.create_oval( rx, ry, rx + 5, ry + 5, fill='blue', outline='red')
        
    def draw_random_ovals( self):
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
        # self.draw_random_ovals( )
        self.draw_ovals( event)
        
    def add_line(self, event):
        self.create_line((self.lastx, self.lasty, event.x, event.y))
        self.save_posn(event)

    def create_button(self, parent):
        self.close_button = ttk.Button(parent, text='Close!', command= root.destroy)
        self.close_button.grid( column=1, row=0, sticky=( S))

root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe = ttk.Frame( root, padding="12 12 12 12")
mainframe.grid( column=0, row=0, sticky=( N, W, E, S))

sketch = Sketchpad( mainframe, width=(WIDTH + 10), height=(HEIGHT + 10))
sketch.grid(column=0, row=0, sticky=(N, W, E, S))

myimg = ImageTk.PhotoImage(Image.open('imgs/Blank_map_of_the_world.jpg').resize( (WIDTH, HEIGHT)))
sketch.create_image(10, 10, image=myimg, anchor='nw')
# sketch.create_oval(10, 10, 15, 15, fill='red', outline='blue')

root.mainloop()
        
