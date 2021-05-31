from tkinter import *
from tkinter.ttk import *
import time
import random
import csv

class Fitts:
    
    def __init__(self, master):
        self.master = master
        
        self.start = time.time()
        self.file = open('fitts_experiment.txt', 'w')
        self.spamwriter = csv.writer(self.file, delimiter=' ',
                                           quotechar='|', quoting=csv.QUOTE_MINIMAL)
        self.canvas_width = 700
        self.canvas_height = 525
        self.distances = [64, 128, 256, 512]
        self.widths = [4, 8, 16, 32]
        self.all_combinations = self.all_combinations_distance_and_width()
        self.margin, self.corner1, self.distance, self.width = self.setup_elements()
        self.c, self.rect1, self.rect2 = self.setup_canvas(self.margin, self.corner1, self.distance)
        self.c.tag_bind(self.rect1, "<ButtonPress-1>", self.click_rectangle) 
        self.c.tag_bind(self.rect2, "<ButtonPress-1>", self.click_rectangle)
        
        self.n = 4
        self.n_repetitions_of_distance_and_length = self.n
        self.one_counter = 1
        
        
    def setup_elements(self):
        distance, width = self.get_distance_and_width()
        total_span = distance + width
        margin = (self.canvas_width - (total_span)) / 2
        corner1 = margin + width       
        return margin, corner1, distance, width
    
    def rect_color(self, left_rect_color, right_rect_color):
        if left_rect_color == 'blue' and right_rect_color == 'green':
            l_color = 'green'
            r_color = 'blue'
        else:
            l_color = 'blue'
            r_color = 'green'
        return l_color, r_color

    def click_rectangle(self, event):
        total_time = "{:.1f}".format((time.time() - self.start) * 1000)
        self.log_time(total_time)
        self.one_counter += 1
        left_rect_color = self.c.itemcget(self.rect1, "fill")
        right_rect_color = self.c.itemcget(self.rect2, "fill")
        l_color, r_color = self.rect_color(left_rect_color, right_rect_color)
        if self.n == 1:
            if self.all_combinations == []:
                self.file.close()
                self.master.destroy()
            else:
                margin, corner1, self.distance, self.width = self.setup_elements()
                self.c.coords(self.rect1, margin, 0, corner1, self.canvas_height)
                self.c.coords(self.rect2, margin + self.distance, 0, corner1 + self.distance, self.canvas_height)
                self.c.itemconfig(self.rect1, fill=l_color)
                self.c.itemconfig(self.rect2, fill=r_color)
                self.start = time.time()
        elif self.n_repetitions_of_distance_and_length != 1:
            self.c.itemconfig(self.rect1, fill=l_color)
            self.c.itemconfig(self.rect2, fill=r_color)
            self.n_repetitions_of_distance_and_length -= 1
        else:
            if self.all_combinations == []:
                self.file.close()
                self.master.destroy()
            else:
                self.n_repetitions_of_distance_and_length = self.n
                margin, corner1, self.distance, self.width = self.setup_elements()
                self.c.coords(self.rect1, margin, 0, corner1, self.canvas_height)
                self.c.coords(self.rect2, margin + self.distance, 0, corner1 + self.distance, self.canvas_height)
                self.c.itemconfig(self.rect1, fill=l_color)
                self.c.itemconfig(self.rect2, fill=r_color)
                self.start = time.time()       
        
    def setup_canvas(self, margin, corner1, distance):
        c = Canvas(self.master, width=self.canvas_width, height=self.canvas_height)
        c.pack()
        rect1 = c.create_rectangle(margin, 0, corner1, self.canvas_height, fill="blue") #x1, y1 (top left corner) x2, y2 (bottom right corner)
        rect2 = c.create_rectangle(margin + distance, 0, corner1 + distance, self.canvas_height, fill="green")     
        return c, rect1, rect2
                    
    def log_time(self, total_time):
        if self.n == 1:
            self.spamwriter.writerow(["Ankur"] + [self.distance] + [self.width] + 
                            [self.one_counter] + [total_time])
        else:
            self.spamwriter.writerow(["Ankur"] + [self.distance] + [self.width] + 
                            [(self.n - self.n_repetitions_of_distance_and_length) + 1] + [total_time])            
        
        
    def all_combinations_distance_and_width(self):
        all_combinations = []
        
        for i in self.distances:
            for j in self.widths:
                all_combinations.append((i, j))
                
        return all_combinations
    
    def get_distance_and_width(self):
        random.shuffle(self.all_combinations)
        distance, width = self.all_combinations[0]
        self.all_combinations.pop(0)
        return distance, width
    
    
master = Tk()
fitts = Fitts(master)
master.mainloop()