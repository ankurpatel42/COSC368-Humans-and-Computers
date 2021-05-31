from tkinter import *
from tkinter.ttk import *
import time
import random
import csv

#Keyboard implemented as a Class

class Keyboard:
    
    def __init__(self, window, configuration):
        
        self.window = window
        self.configuration = configuration
        
        self.file = open('experiment_{}_log.txt'.format(self.configuration), 'w')
        self.spamwriter = csv.writer(self.file, delimiter=' ',
                                           quotechar='|', quoting=csv.QUOTE_MINIMAL) 
  
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.block = []
        self.n_blocks = []
        self.n = 2
        self.num_letters = 6
        
        self.start = time.time()
        self.letters_seen = {}
        self.frame = Frame(self.window, borderwidth=1, relief=RIDGE, height=32, width=32)
        self.frame.pack(side=BOTTOM, padx=10, pady=10)
        self.labeltext = StringVar()
        self.label = Label(self.window, textvariable=self.labeltext)
        self.label.pack()
        self.letter_to_find = self.letter_to_click()
        self.labeltext.set(self.letter_to_find)
        self.board = self.create_keyboard()
        self.populate_keyboard()
        
    def letter_to_click(self):
        while len(self.block) != self.num_letters:
            letter_to_add_to_block = self.letters[random.randrange(0, len(self.letters))]
            self.letters.pop(self.letters.index(letter_to_add_to_block))
            self.block.append(letter_to_add_to_block)
        while self.n > 0:
            random.shuffle(self.block)
            self.n_blocks += self.block
            self.n -= 1
        return self.n_blocks[0]
    
    def create_keyboard(self):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        list_alphabet = list(alphabet)
        random.shuffle(list_alphabet)
        first_row = ''.join(list_alphabet[0:10])
        second_row = ''.join(list_alphabet[10:19])
        third_row = ''.join(list_alphabet[19:])
        board = [first_row, second_row, third_row]
        return board
    
    def populate_keyboard(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                buttonframe = Frame(self.frame, height=32, width=32)
                if i == 2:
                    buttonframe.grid(column= 1 + ((2 * j)+i), row=i, columnspan=2)
                else:
                    buttonframe.grid(column= (2 * j)+i, row=i, columnspan=2)
                buttonframe.pack_propagate(0)        
                button = Button(buttonframe, text=self.board[i][j],command=lambda x=self.board[i][j]:self.click_button(x))
                button.pack(fill=BOTH, expand=1)
                
    def click_button(self, character_clicked):
        
        self.letter_to_find = self.labeltext.get()
        
        if character_clicked == self.letter_to_find:
            total_time = "{:.1f}".format((time.time() - self.start) * 1000)
            self.character_click_count()
            self.log_time(total_time)
            self.n_blocks.pop(self.n_blocks.index(self.letter_to_find))      
            if self.n_blocks == []:          
                self.labeltext.set("All blocks complete!")
                self.file.close()
            else:
                self.letter_to_find = self.n_blocks[0]
                self.labeltext.set(self.letter_to_find)
                if self.configuration == "dynamic":
                    self.board = self.create_keyboard()     
                    self.populate_keyboard()
                self.start = time.time()
    
    def character_click_count(self):
        if self.letter_to_find in self.letters_seen:
            self.letters_seen[self.letter_to_find] += 1
        else:
            self.letters_seen[self.letter_to_find] = 1 
            
    def log_time(self, total_time):
        self.spamwriter.writerow(["Ankur"] + [self.configuration] + [self.letter_to_find] + 
                            [self.letters_seen[self.letter_to_find]] + [total_time])    
            

configuration = "dynamic"
window = Tk()
keyboard = Keyboard(window, configuration)
window.mainloop()