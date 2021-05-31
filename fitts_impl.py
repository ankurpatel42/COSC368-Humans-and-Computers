#!/usr/bin/python3

# Note: Updated in 2016 to Python 3, from the original 
#       Python2 version that was used in COSC368 in 2015

from tkinter import *

import sys
import time
import random
import getpass


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

USERNAME = getpass.getuser() # use the user's own username (works for Unix and Windows) - http://stackoverflow.com/a/842096/6531515

AMPLITUDES = [64, 128, 256, 512]
WIDTHS = [4, 8, 16, 32]
REPETITIONS = 8

class FittsWidget(Widget):   
    def __init__(self, master):
        self._master  = master
        
        self._command = None
        self._surface = Canvas(master, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg='white')
        self._surface.pack()
        
        self._surface.create_rectangle(0,0,0,0, tag='left', fill='blue', outline='')
        self._surface.create_rectangle(0,0,0,0, tag='right', fill='green', outline='')
        self._surface.tag_bind('left', '<1>', lambda e: self._hit('left'))
        self._surface.tag_bind('right', '<1>', lambda e: self._hit('right'))
        
    def show_targets(self, a, w):
        # Place targets around the centre of the window
        x = (WINDOW_WIDTH/2) - (a/2)
        self._surface.coords('left', x, 0, x+w, WINDOW_HEIGHT)
        self._surface.coords('right', x+a, 0, x+a+w, WINDOW_HEIGHT)
        
    def set_command(self, c):
        self._command = c
        
    def _hit(self, item):
        if not self._surface.itemcget(item, 'fill') == 'green':
            return
        # Swap colours
        if item == 'right':
            self._surface.itemconfigure('left', fill='green')
            self._surface.itemconfigure('right', fill='blue')
        else:
            self._surface.itemconfigure('left', fill='blue')
            self._surface.itemconfigure('right', fill='green')   
        if callable(self._command): 
            self._command()

class Experiment(object):
    def __init__(self, widget):
        self._widget = widget
        self._widget.set_command(self._click)
        
        self._log = open('experiment_fitts_log.txt', 'a')
        
        self._combos = [(a,w) for a in AMPLITUDES for w in WIDTHS]
        random.shuffle(self._combos)
        
    def _click(self):
        total_time = (time.time() - self._start_time) * 1000
        self._log.write('%s\t%d\t%d\t%d\t%.2f\n' % (USERNAME, 
                                                    self._target[0], self._target[1],
                                                    self._block_count, total_time))

        self._block_count += 1
        if self._block_count == REPETITIONS:
            self._next_target()
        else:
            self._start_time = time.time()

    def start(self):
        self._next_target()

    def _next_target(self):
        if not len(self._combos):
            # Finished experiment
            from tkinter import messagebox
            self._log.close()
            messagebox.showinfo(message='Finished.')
            self._widget._master.destroy()
        else:
            # Next set of targets
            self._start_time = time.time()
            self._block_count = 0
            self._target = self._combos.pop()
            self._widget.show_targets(*self._target)

def main():
    master = Tk()
    master.title("Click on the green bar...")
    master.resizable(0,0)

    fitts = FittsWidget(master)
    e = Experiment(fitts)
    e.start()

    master.mainloop()

if __name__ == '__main__':
    main()
