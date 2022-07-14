# first use of tkinter
# JNatoli, 2022

from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float( feet.get())
        meters.set( int( 0.03048* value * 10000.0 + 0.5) / 10000.0)
    except ValueError:
        pass

def Tutorial():
    # Main Application
    root = Tk()
    root.title("My Feet to Meters")
    
    # Content Frame
    mainframe = ttk.Frame( root, padding="3 3 12 12")
    mainframe.grid( column=0, row=0, sticky=( N, W, E, S))
    root.columnconfigure( 0, weight=1)
    root.rowconfigure( 0, weight=1)

    # Create 1st Widget
    feet = StringVar()
    # mainframe is parent widget, shows up as "width" characters
    feet_entry = ttk.Entry( mainframe, width=7, textvariable=feet)
    # now place the widget somewhere on the 3x3 grid, sticky is alignment
    feet_entry.grid( column=2, row=1, sticky=( W, E))

    # Next Widget
    meters = StringVar()
    ttk.Label( mainframe, textvariable=meters).grid( column=2, row=2, sticky=( W, E))

    # Button Widget
    ttk.Button( mainframe, text="Calculate Please :)", command=calculate).grid( column=3, row=3, sticky=E)
    
    # Create and place all at once (.grid( ... ))
    ttk.Label( mainframe, text="feet").grid(             column=3, row=1, sticky=W)
    ttk.Label( mainframe, text="is equivalent to").grid( column=1, row=2, sticky=E)
    ttk.Label( mainframe, text="meters").grid(           column=3, row=2, sticky=W)
    
    # prevents scrunching
    for child in mainframe.winfo_children():
        child.grid_configure( padx=5, pady=5)
        
    # Cursor starts on this widget
    feet_entry.focus()
    # Links the Return Key action to the calculate routine, same as if button is pressed
    root.bind("<Return>", calculate)

    # Start your engines!
    root.mainloop()

def grid():
    root = Tk()
    # mainframe = ttk.Frame( root, width=600, height=500).grid()
    canvas = Canvas( root, width=500, height=400, background='gray75')
    # l = ttk.Label( mainframe, text="Starting...")
    # l.grid()
    # canvas.bind('<ButtonPress-1>', lambda e: canvas.configure(text='Clicked at %d,%d' % (e.x, e.y)))
    canvas.create_line(10, 5, 200, 50)
    # canvas.bind('<ButtonPress-1>', lambda e: canvas.create_line(10, 5, 200, 50))
    root.mainloop()


if __name__ == "__main__":
    # grid()
    Tutorial()
